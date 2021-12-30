from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    
    path('', views.HomeView.as_view(), name='home'),
    path('assignment/', views.AssignmentView.as_view(), name='assignment'),
    path('assignment/new/', views.AssignmentCreate.as_view(), name='new-assignment'),
    path('assignment/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('course/', views.CourseView.as_view(), name='course'),
    path('instructor/', views.InstructorView.as_view(), name='instructor'),
    path('account/', views.AccountView.as_view(), name='account'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)