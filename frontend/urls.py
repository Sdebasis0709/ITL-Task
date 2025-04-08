from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.task_home, name='task-home'),
     path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True,
    next_page='/'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]



