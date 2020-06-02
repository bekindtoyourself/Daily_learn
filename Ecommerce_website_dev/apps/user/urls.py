from djanog.conf.urls import url
from django.contrib.auth.decorators import login_required
from user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

urlpatterns = [
    url(r'^register$', RegisterView.as_view(), name='register'),
    
]
