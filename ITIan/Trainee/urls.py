from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.traineelist, name='traineelist'),
    path('list/', views.TraineeListView.as_view(), name='traineelist'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('register/', views.register, name='register'),
    path('add/modelform/', views.add_trainee_modelform, name='add_trainee_modelform'), # المسار الجديد
    path('details/<int:id>/', views.trainee_details, name='trainee_details'),
    path('update/<int:id>/', views.update_trainee, name='update_trainee'),
    path('delete/<int:id>/', views.delete_trainee, name='delete_trainee'),
    path('delete/soft/<int:id>/', views.soft_delete_trainee, name='soft_delete_trainee'),
]