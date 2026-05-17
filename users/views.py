from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, UserProfileForm
from .models import CustomUser


class RegisterView(CreateView):
    """Контролер для создания пользователя"""
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Сначала сохраняем пользователя
        user = form.save()

        # Отправляем приветственное письмо
        send_mail(
            subject='Добро пожаловать в Skystore!',
            message=f'Здравствуйте, {user.email}! Спасибо за регистрацию на нашей платформе.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return super().form_valid(form)

class ProfileView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """Возвращает текущего авторизованного пользователя"""
        return self.request.user