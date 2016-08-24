from Library_management.models import User
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import response

def login_service(request):
    UserNumber = request.GET.get('UserNumber')
    PassWord = request.GET.get('PassWord')
    u = User.objects.filter(UserNumber=UserNumber, PassWord=PassWord).first()
    if u is not None:
        if u.IsManager == 1:
            msg = '管理员登陆'
            state = 1
        else:
            request.session['UserNumber'] = UserNumber
            msg = '学生登陆'
            state = 1
    else:
        request.session['UserNumber'] = ""
        msg = '账号或密码错误'
        state = 0
    array = {
        'msg': msg,
        'state': state
    }
    return array