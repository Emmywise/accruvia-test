from django.test import TestCase
from .models import Tweets


class TestOrder(TestCase):
   
    def test_successful_tweet(self):
        data= {
            'name':'wednesdayweu',
            'tweet': 'ih',

        }
        res=self.client.post("/api/tweet/",  format="json", data=data)      
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['name'], data['name'])
        self.assertEqual(res.data['tweet'], data['tweet'])
      