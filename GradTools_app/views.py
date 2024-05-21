from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Department, Course, Purpose, Material


# Create your views here.

def Greet(request):
    return HttpResponse("<h1>GradTools Will launch here!</h1>")


# def base(request):
#     return render(request,'base.html')


def home(request):
    courses = Course.objects.all()

    top_courses = Course.objects.filter(top=True)

    context = {'courses': courses,
               'top_courses': top_courses}

    return render(request, 'home.html', context)


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


@login_required(login_url="/login/", redirect_field_name='next')
def new_page(request):
    return render(request, 'new-page.html')


@login_required(login_url="/login/", redirect_field_name='next')
def form(request):
    template_name = "form.html"
    deptcontext = Department.objects.all()
    crscontext = Course.objects.all()
    prpscontext = Purpose.objects.all()
    matcontext = Material.objects.all()
    return render(request, template_name, {'Department': deptcontext, 'Course': crscontext,
                                           'Purpose': prpscontext, 'Materials': matcontext})

#
# def studForm(request):
#     form=forms.StudentForm()
#     my_dict={'form':form}
#     return render(request,'forms.html',context=my_dict)
