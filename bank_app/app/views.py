from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render_to_response
from .models import Banks_branches
from rest_framework.views import APIView
global permission_classes
from .serializer import Banks_branchesSerializer
from django.contrib.auth.models import User
import requests

from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class AppView(APIView):
    data=Banks_branches.objects.all()
    serializer_class1=Banks_branchesSerializer
    permission_classes = (IsAuthenticated,)
    def get(self,request):
         query=self.request.GET.get("ifsc")
         if request.method=="GET":
               data_ifsc=Banks_branches.objects.filter(ifsc=query)
               return render_to_response("home.html",{'data_ifsc':data_ifsc})


class AppView1(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):

           bank_in_city=[]
           bank_name=self,request.GET.get("bank_name")
           city=self.request.GET.get("city")
           if request.method=="GET":
                    bank_in_city=Banks_branches.objects.filter(bank_name=bank_name,city=city)
                   # for i in range(len(bank_city)):
                    #          if bank_name in str(bank_city[i]):
                     #              bank_in_city.append(bank_city[i])

           return  render_to_response('temp.html',{'list':bank_in_city[:6]})
