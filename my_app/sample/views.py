from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import MyModel

# Create your views here.

class HomeView(APIView):

    def get(self, request, format=None):
        return JsonResponse({"message":'Hello World From Django And Docker!'})
    
class UserView(APIView):

    def get(self, request, format=None):
        MyModel('janic', '22')
        qs = MyModel.objects.all()
        data = [{'name': user.name, 'age': user.age} for user in qs]
        return JsonResponse(data, safe=False)
