from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from Course.models import Course
from .forms import TraineeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import TraineeSerializer

def traineelist(request):
    trainees = Trainee.objects.filter(is_deleted=False) 
    return render(request, 'trainee/list.html', {'trainees': trainees})

def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/details.html', {'trainee': trainee})

def add_trainee(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        f_name = request.POST.get('first_name') 
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        c_id = request.POST.get('course_id')

        Trainee.objects.create(
            first_name=f_name,
            last_name=l_name,
            email=email,
            course_id=c_id
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

def add_trainee_modelform(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('traineelist')
    else:
        form = TraineeForm()
    return render(request, 'trainee/add_modelform.html', {'form': form})


def soft_delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.is_deleted = True  
    trainee.save()
    return redirect('traineelist')

class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee/list.html'
    context_object_name = 'trainees'

    def get_queryset(self):
        return Trainee.objects.filter(is_deleted=False)
    
class TraineeCreateView(CreateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/add_modelform.html'
    success_url = reverse_lazy('traineelist')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class TraineeViewSet(viewsets.ModelViewSet):
    queryset = Trainee.objects.filter(is_deleted=False)
    serializer_class = TraineeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]