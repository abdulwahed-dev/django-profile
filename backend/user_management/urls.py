from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# Add the following to the list of previous imports
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.urls import re_path as url
from users.forms import LoginForm
from users.views import ChangePasswordView, CustomLoginView, ResetPasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # This is what we added
    # Add this path
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
     path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    
] 

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)