1、Python 函数参数传递
Python 函数中，参数的传递本质上是一种赋值操作。
变量指向对象的。

```python

# 用可变(mutable)对象作为参数的默认值。函数定义好之后，默认参数 a_list 就会指向（绑定）到一个空列表对象，每次调用函数时，都是对同一个对象进行 append 操作。因此这样写就会有潜在的bug，同样的调用方式返回了不一样的结果。
def bad_append(new_item, a_list=[]):
    print(a_list)
    a_list.append(new_item)
    return a_list

print(bad_append('one')) # one
print(bad_append('one')) # one, one

def good_append(new_item, a_list=None):
    print(a_list)
    if a_list is None:
        a_list = []
    a_list.append(new_item)
    return a_list

print(good_append('one')) # one
print(good_append('one')) # one

# 在python中，strings, tuples, 和numbers是不可更改的对象，而list,dict等则是可以修改的对象。
def ChangeInt( a ):
    a = 10
nfoo = 2 
ChangeInt(nfoo)
print(nfoo) #结果是2


def ChangeList( a ):
    a[0] = 10
lstFoo = [2]
ChangeList(lstFoo )
print lstFoo #结果是[10]

```




