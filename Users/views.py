from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginUserForm, SignupUserForm, UserProfileForm, UserPasswordChangeForm


USERMODEL = get_user_model()


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy("blog:home")
    extra_context = {
        'title': "Авторизация",
    }


class UserSignupView(CreateView):
    form_class = SignupUserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy("users:profile")
    extra_context = {
        'title': "Регистрация",
    }


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = USERMODEL
    form_class = UserProfileForm
    template_name = 'profile/profile.html'
    success_url = reverse_lazy("users:profile")
    extra_context = {
        'title': "Профиль",
    }

    def get_object(self):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = 'password/password_change_form.html'


def logoutview(request):
    logout(request)
    return reverse_lazy('users:login')