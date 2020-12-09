from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('assignment/', views.AssignmentView.as_view(), name='assignment'),
    path('assignment/new/', views.AssignmentCreate.as_view(), name='new-assignment'),
    path('course/', views.CourseView.as_view(), name='course'),
    path('instructor/', views.InstructorView.as_view(), name='instructor'),
]