from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.courselist, name='courselist'),
    path('add/', views.add_course, name='add_course'),
    path('update/<int:id>/', views.update_course, name='update_course'),
    path('delete/<int:id>/', views.delete_course, name='delete_course'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]