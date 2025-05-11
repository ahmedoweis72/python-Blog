from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostsViewSet,CommentViewSet,AuthorViewSet
from . import views 




router = DefaultRouter()
router.register(r'posts', views.PostsViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
#    path('', views.all_posts),
#    path('post/<int:id>', views.post, name='post'),
#    path('author/<int:id>', views.author_view, name='author_view'),
   path('', include(router.urls)),
]