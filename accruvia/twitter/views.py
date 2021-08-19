from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer
from .models import Tweets
# Create your views here.

class Tweet(APIView):

    # post request for tweets
    def post(self, request): 
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # get request for tweets
    def get(self, request, pk=None):
        queryset = Tweets.objects.all()

        if self.request.query_params.get('sort')==  'name':
            queryset=queryset.order_by('name')
        elif self.request.query_params.get('sort')=='date':
            queryset=queryset.order_by('-date_created')
        serializer = TweetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)