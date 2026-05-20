from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from django.contrib.auth.forms import UserCreationForm

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CourseSerializer

def courselist(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Course.objects.create(name=name, description=description)
        return redirect('courselist')
    return render(request, 'course/add.html')

def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.save()
        return redirect('courselist')
    return render(request, 'course/update.html', {'course': course})

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('courselist')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]