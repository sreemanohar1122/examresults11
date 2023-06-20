from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.http import HttpResponse
from .models import Student

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method=='POST':
        rollNo=int(request.POST['roll_no'])
        student=Student.objects.get(roll_no=rollNo)
        telugu=student.telugu
        maths=student.maths
        stat=student.stat
        science=student.science
        total=telugu+maths+stat+science
        percent=total/400*100
        if (percent<33):
            status = 'Fail'
        else:
            status = 'Pass'
        params={
            'roll_no':rollNo,
            'name':student.name,
            'telugu':telugu,
            'maths':maths,
            'stat':stat,
            'science':science,
            'percent': percent,
            'status':status,
        }

        return render(request, 'result.html', params)
    else:
        print('get method')
    return render(request,'result.html')

def admin_login(request):
    if 'user' in request.session:
        return render(request, 'admin_panel.html')
    else:
        return render(request, 'admin-login.html')

def admin_panel(request):
    if 'user' in request.session:
        students=Student.objects.all()
        params={'students': students}
        return render(request, 'admin_panel.html',params)
    else:
        if request.method=='POST':
            user_name=request.POST['uname']
            pass_word=request.POST['pwd']
            if user_name=='manu' and pass_word=='Manu@123':
                request.session['user']=user_name
                students=Student.objects.all()
                params={'students':students}
                return render(request, 'admin_panel.html', params)
            else:
                return render(request,'admin-login.html')
        else:
            return render(request, 'admin-login.html')


def delete_student(request,id):
    get_stu=Student.objects.get(id=id)
    get_stu.delete()
    return redirect('/admin_panel')

def edit_student(request,id):
    get_stu=Student.objects.get(id=id)
    params={'student':get_stu}
    return render(request, 'edit.html', params)

def edit_confirm(request,id):
    if request.method=='POST':
        get_stu=Student.objects.get(id=id)
        get_stu.name=request.POST['sname']
        get_stu.roll_no=request.POST['roll-no']
        get_stu.telugu=request.POST['telugu']
        get_stu.maths=request.POST['maths']
        get_stu.stat=request.POST['stat']
        get_stu.science=request.POST['science']
        total=int(request.POST['telugu'])+int(request.POST['maths'])+int(request.POST['stat'])+int(request.POST['science'])
        get_stu.total=total
        get_stu.percent=total/4
        get_stu.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_login')

def admin_logout(request):
    del request.session['user']
    return redirect('/')

def add_student(request):
    return render(request,'add_student.html')


def add_confirm(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        roll_no = request.POST['roll-no']
        telugu = int(request.POST['telugu'])
        maths = int(request.POST['maths'])
        stat = int(request.POST['stat'])
        science = int(request.POST['science'])
        total = telugu++maths+stat+science
        percent = total/400*100
        add_student = Student.objects.create(name=sname,roll_no=roll_no,
                        telugu=telugu,maths=maths,stat=stat,science=science,
                        total=total,percent=percent)
        add_student.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_panel')


