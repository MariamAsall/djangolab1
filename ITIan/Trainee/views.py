from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from Course.models import Course

def traineelist(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def add_trainee(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        Trainee.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            course_id=request.POST.get('course_id') # Linking the foreign key
        )
        return redirect('traineelist')
    return render(request, 'trainee/add.html', {'courses': courses})

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        trainee.first_name = request.POST.get('first_name')
        trainee.last_name = request.POST.get('last_name')
        trainee.email = request.POST.get('email')
        trainee.course_id = request.POST.get('course_id')
        trainee.save()
        return redirect('traineelist')
    return render(request, 'trainee/update.html', {'trainee': trainee, 'courses': courses})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('traineelist')