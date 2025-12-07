from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from .views import UserLoginView, UserPasswordChangeView, UserProfileView, UserSignupView, logoutview


app_name = "users"


urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('profile/password-change/done/', PasswordChangeDoneView.as_view(template_name='password/password_change_done.html'), name='password_change_done'),
]

urlpatterns += [
]