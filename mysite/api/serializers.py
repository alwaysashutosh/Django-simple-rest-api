 # it makes the data readable by the front end that is jason format data

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields =[ 'id', 'title', 'content', 'published_date']