from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from .views import CategoryView, DigitalView, PhotographyView, PaintingView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/digital/', DigitalView.as_view(), name='digital'),
    path('category/painting/',PaintingView.as_view(), name='painting'),
    path('category/photography/',PhotographyView.as_view(), name='photography'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)

