import re
from django.core.urlresolvers import reverse
from user.models import User
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    return render(request, 'register.html')


def register_handle(request):
    ''''注册处理'''
    # 1.接受数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    password2 = request.POST.get('cpwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
    # 2.进行数据的校验
    if not all([username, password, password2, email]):
        # 数据不完整
        return render(request, 'register.html', {'errmsg': '数据不完整'})

    if not password2 == password:
        # 两次密码不一致
        return render(request, 'register.html', {'errmsg': '两次密码不一致'})

    # 校验邮箱
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'register.html', {'errmsg': '请同意协议'})

    # 校验用户名是否重复
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # 用户名不存在
        user = None
    if user:
        # 用户名已存在
        return render(request, 'register.html', {'errmsg': '用户名已存在'})
    # 3.进行业务处理(进行用户注册)
    user = User.objects.create_user(username, email, password)
    user.is_active = 0  # 新注册的用户使其处于没有激活的状态
    user.save()

    # 4.返回应答,跳转到首页
    return redirect(reverse('goods:index'))
