from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format = None):
        an_apiview = [
            'Uses HTTP methods as functions (GET,POST,PUT,PATCH,DELETE).',
            'It is similar to a traditional Django view',
            'Gives you the most control over the logic',
            'Is mapped mannually to URLs'
        ]

        return Response({"message":"Hello!!","Apiview": an_apiview})