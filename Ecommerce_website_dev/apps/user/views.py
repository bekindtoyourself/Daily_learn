from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.views.generic import View
from django.conf import settings

from user.models import User, Address
from goods.models import GoodsSKU
from order.models import OrderInfo, OrderGoods

from celery_tasks.tasks import send_register_active_email
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from utils.mixin import LoginRequiredMixin
from django_redis import get_redis_connection
import re

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg':'用户名已存在 '})

        user = User.objects.create_user(username, email, password)

        user.is_active = 0
        user.save()

        return redirect(reverse('goods:index'))

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg':  '数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {
                'errmsg': '邮箱格式不正确'
            })

        if allow != 'on':
            return render(request, 'register.html', {
                'errmsg': '请同意协议'
                })

        if user:
            return render(request, 'register.html', {
                'errmsg': '用户名已存在'
                })

        user.is_active = 0
        user.save()

        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)
        token = token.decode('utf8')

        send_register_active_email.delay(email, username, token)

        return redirect(reverse('goods:index'))

class ActiveView(View):

    def get(self, request, token):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']

            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            return redirect(reverse('user:login'))

        except SignatureExpired as e:
            return HttpResponse('激活链接已过期')

class LoginView(View):
    def get(self, request):
        if 'username' in request.COOKIES：
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        return render(request, 'login.html', {
            'username': username,
            'checked': checked
            })
        
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                next_url = request.GET.get('next', reverse('goods:index'))

                response = redirect(next_url)

                remember = request.POST.get('remember')

                if remember == 'on':
                    response.set_cookie('username', username, max_age=7*24*3600)
                else:
                    response.delete_cookie('username')

                return response
            else:
                return render(request, 'login.html', {'errmsg':'账号未激活'})
        else:
            return render(request, 'login.html', {'errmsg':'用户名或密码错误'})

class LogoutView(View):

    def get(self, request):
        logout(request)

    return redirect(reverse('goods:index'))



