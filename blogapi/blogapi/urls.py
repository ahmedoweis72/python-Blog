from django.contrib import admin
from django.urls import path, include
from posts import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/posts/', views.PostListCreate.as_view()),
    path('api/posts/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view()),
    path('api/posts/<int:post_id>/comments/', views.CommentListCreate.as_view()),
    path('api/comments/<int:pk>/', views.CommentRetrieveUpdateDestroy.as_view()),
]