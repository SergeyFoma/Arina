from django.shortcuts import render
from admin_college.models import Teacher
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.db import transaction

def check(request):
    #print(request.GET)
    # a=request.GET
    # #print('Value: ', a.value)
    # te=[]
    # teach=Teacher.objects.all()
    # #print(teach)
    # for t in teach:
    #     te.append(t.verification_number)
    # print('T: ', te)

    # vv=''
    # for k,v in a.items():
    #     vv=v
    #     print('V: ', vv)

    # if vv in te:
    #     return redirect('users:login_users')

    if request.method=='POST':
        #check = request.POST.get('check','')
        #print(check)
        code = request.POST.get('invite_code')
        print(code)
        try:
            # select_for_update блокирует запись до конца транзакции
            with transaction.atomic():
                teacher = Teacher.objects.select_for_update().get(invite_code=code, is_active=True)
                # Код найден и активен. Помечаем его как использованный.
                teacher.use_code()
                
                # Здесь создаете пользователя, так как код валиден
                # ... ваша логика создания пользователя ...
                
                return redirect('users:register_user')
                
        except Teacher.DoesNotExist:
            # Код не найден или уже неактивен
            return redirect('admin_college:check')
        
        # te=[]
        # teach=Teacher.objects.all()
        # for t in teach:
        #     te.append(t.verification_number)
        
        # if check in te:
        #     return redirect('users:register_user')
        # else:
        #     messages.success(request, 'Не верный номер')
        #     return redirect('admin_college:check')


    context={
        # 'teach':teach,
        # 'te':te,
        # 'vv':vv,
    }
    return render(request,"admin_college/check.html", context)

