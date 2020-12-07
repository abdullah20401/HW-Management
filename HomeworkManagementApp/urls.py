from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('assignments/', views.AssignmentsView.as_view(), name='assignments'),
    path('courses/', views.CoursesView.as_view(), name='courses'),
    path('instructors/', views.InstructorsView.as_view(), name='instructors'),
]