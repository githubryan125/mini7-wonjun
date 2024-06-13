from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *


def login_page(request):
    return render(request, 'login/login_page.html')


def join_page(request):
    return render(request, 'login/join_page.html')


def logout(request):
    response = redirect('/')
    response.delete_cookie('login')
    return response


@csrf_exempt
def join_chk(request):
    result = 'success'
    try:
        input_id = request.POST['id']
        # 기존에 해당 ID가 있는지 확인
        if User.objects.filter(id=input_id).exists():
            result = 'id overlap'  # 이미 존재하는 ID인 경우
        else:
            # 존재하지 않는 경우, 새로운 User 객체 생성 및 저장
            _user = User()
            _user.id = input_id
            _user.pw = request.POST['pw']
            _user.save()
    except Exception as e:
        print(e)
        result = 'error'
    context = {'result': result}
    return JsonResponse(context)



@csrf_exempt
def login_chk(request):
    if request.method == 'POST':
        result = 'success'
        _user = User.objects.filter(id=request.POST['id'], pw=request.POST['pw'])
        if not _user.exists():
            result = 'id or pw mistake'
            context = {'result': result}
            return JsonResponse(context, status=401)
        else:
            response = JsonResponse({'result': result})
            response.set_cookie('login', request.POST['id'], max_age=3600)
            request.user = request.POST['id']
            return response
    else:
        return JsonResponse({'result': 'invalid request method'}, status=400)

