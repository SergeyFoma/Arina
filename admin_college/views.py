from django.shortcuts import render
from admin_college.models import Teacher
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

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
        check = request.POST.get('check','')
        print(check)
        te=[]
        teach=Teacher.objects.all()
        for t in teach:
            te.append(t.verification_number)
        
        if check in te:
            return redirect('users:login_users')
        else:
            messages.success(request, 'Не верный номер')
            return redirect('admin_college:check')
    
    context={
        # 'teach':teach,
        # 'te':te,
        # 'vv':vv,
    }
    return render(request,"admin_college/check.html", context)

