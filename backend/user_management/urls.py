from django.contrib import admin
# Add the following to the list of previous imports
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users.forms import LoginForm
from users.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # This is what we added
    # Add this path
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]