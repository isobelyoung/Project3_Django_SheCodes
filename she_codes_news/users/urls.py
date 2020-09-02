from django.urls import path
from .views import CreateAccountView, ChangeAccountView, AuthorView, AccountView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    path('account/<int:pk>/', AccountView.as_view(), name='account'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('author/<int:pk>', AuthorView.as_view(), name='author'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)