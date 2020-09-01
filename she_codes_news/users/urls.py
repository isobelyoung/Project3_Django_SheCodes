from django.urls import path
from .views import CreateAccountView
from .views import AccountView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('account/<int:pk>/', AccountView.as_view(), name='account'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)