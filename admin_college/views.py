from django.shortcuts import render
from admin_college.models import Teacher
from django.shortcuts import redirect

def check(request):
    #print(request.GET)
    a=request.GET
    #print('Value: ', a.value)
    te=[]
    teach=Teacher.objects.all()
    #print(teach)
    for t in teach:
        te.append(t.verification_number)
    print('T: ', te)

    vv=''
    for k,v in a.items():
        vv=v
        print('V: ', vv)
    if vv in te:
        print('YES: ', vv)

    if vv in te:
        return redirect('users:login_users')

    
    context={
        'teach':teach,
        'te':te,
        'vv':vv,
    }
    return render(request,"admin_college/check.html", context)

