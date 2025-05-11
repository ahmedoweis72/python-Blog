from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Post
from .models import Author
from .models import Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets
from .serializers import PostSerializer, AuthorSerializer, CommentSerializer

# def all_posts(request):
#     posts=Post.objects.all()
#     return render(request,'posts/posts_list.html',context={
#         "posts":posts
#     })
# def post(request,id):
#     post = Post.objects.get(id=id) 
#     return render(request,'posts/post.html',context={
#         "post": post
#     })
# def author_view(request,id):
#     author = Author.objects.get(id=id)
#     return render(request,'posts/author.html',context={
#         'author': author
#     }) 


class PostsViewSet(viewsets.ModelViewSet):
    queryset =Post.objects.all()
    serializer_class = PostSerializer



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer