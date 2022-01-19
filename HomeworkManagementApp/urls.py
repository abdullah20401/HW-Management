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
    
    path('assignment/list/missing/', views.AssignmentListView.as_view(), name='assignment-list-missing'),
    path('assignment/list/upcoming/', views.AssignmentListView.as_view(), name='assignment-list-upcoming'),
    path('assignment/list/completed/', views.AssignmentListView.as_view(), name='assignment-list-completed'),

    path('assignment/new/', views.AssignmentCreateView.as_view(), name='new-assignment'),
    path('assignment/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignment/<int:pk>/completed/', views.AssignmentMarkAsComplete.as_view(), name='assignment-complete'),
    path('assignment/<int:pk>/edit/', views.AssignmentUpdateView.as_view(), name='assignment-update'),
    path('assignment/<int:pk>/edit/delete/', views.AssignmentDeleteView.as_view(), name='assignment-delete'),

    path('course/', views.CourseView.as_view(), name='course'),
    path('instructor/', views.InstructorView.as_view(), name='instructor'),

    path('account/', views.AccountView.as_view(), name='account'),
    path('account/update/', views.AccountUpdateView.as_view(), name='account-update'),
    path('account/update/password/', views.AccountPasswordUpdateView.as_view(), name='account-password'),
    path('account/delete/', views.AccountDeleteView.as_view(), name='account-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
