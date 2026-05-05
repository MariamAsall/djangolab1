from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.traineelist, name='traineelist'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('update/<int:id>/', views.update_trainee, name='update_trainee'),
    path('delete/<int:id>/', views.delete_trainee, name='delete_trainee'),

    path('accounts/', include('django.contrib.auth.urls')), # Handles login/logout
    path('register/', course_views.register, name='register'),
]