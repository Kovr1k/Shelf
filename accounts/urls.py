from django.urls import path, include
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('register', Register.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view
         (template_name='registration/recovery/password_reset_form.html',
         email_template_name='registration/recovery/password_reset_email.html',
         success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view
         (template_name='registration/recovery/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view
         (template_name='registration/recovery/password_reset_confirm.html',
          success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view
         (template_name='registration/recovery/password_reset_complete.html'), name='password_reset_complete'),
     path("profile/", ProfileNull.as_view(), name="profileNull"),
     path("profile/<filter>", Profile.as_view(), name="profile"),
     path("profileUser/<id>/<filter>", ProfileAnyUser.as_view(), name="profileAnyUser"),
     path('exit/', logout_view, name='exit'),
]