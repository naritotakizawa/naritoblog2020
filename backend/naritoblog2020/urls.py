from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'naritoblog2020'

router = DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('', include(router.urls)),
]
