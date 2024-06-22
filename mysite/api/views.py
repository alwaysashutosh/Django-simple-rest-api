from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.ojeccts.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class BlogPostReteriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer  
    lookup_field = 'pk' 


#class BlogPostList(APIview) :
