
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.forms import PasswordResetForm
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html') ,name='login'),
    
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html') ,name='logout'),
    path('register',views.signup,name='register'),
    path('reset_pasword',auth_views.PasswordResetView.as_view(template_name='passwords/reset_pasword.html'),name='reset_pasword'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='passwords/pasword_sent.html'),name='pasword_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwords/confirm.html'),name='pasword_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='passwords/ResetDone.html'),name='password_reset_complete'),
    
    path('profile',views.viewProfile,name='viewe_profile'),
    path('update_user_info',views.updateinfo ,name='update_info'),
    path('update_profilePic',views.updatePic,name='update-pic'),
    path('view_user_profile/<int:user_id>',views.view_user_profile,name='view_user_profile'),
    path('follow_user',views.follow,name='follow_user'),
    path('update_profile',views.updateProfile,name='update_profile'),
    path('update_company',views.updateCompany,name='update_company'),


]

