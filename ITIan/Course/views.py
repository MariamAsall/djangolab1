from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

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