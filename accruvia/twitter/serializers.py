from rest_framework import serializers
from .models import Tweets


#serializer class for tweet
class TweetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    tweet = serializers.CharField(max_length=50) 

    class Meta:
        fields = '__all__'
        model = Tweets