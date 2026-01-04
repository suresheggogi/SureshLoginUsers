
from django.shortcuts import render, redirect
from django.http import HttpResponse
from postgresApp.models import student
from dataBaseProject import settings
# Create your views here.

def signup(request):
    return render(request, 'Signup.html')

def writefile(request):
        login = student(
             stu_name = request.GET['fnm'],
             stu_mail= request.GET['email'],
             stu_pwd = request.GET['pwd']
             )
        login.save()
        return redirect('../show')

def alll(request):
    objs = student.objects.all()
    root = '''
    <table border='1'>
    <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Email</th>
    <th>passwd</th>
    </tr>'''
    res = ""
    for val in objs:
         res = res+"<tr><td>"+str(val.id)+"</td><td>"+val.stu_name+"</td><td>"+val.stu_mail+"</td><td>"+val.stu_pwd+"</tr>"
                
    root = root+""+res+"</table>"
    root = root+"<a href = '../'> Go to Register </a>"
    return HttpResponse(root)

