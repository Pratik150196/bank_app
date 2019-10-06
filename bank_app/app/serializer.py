from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Banks_branches
from django.contrib.auth import authenticate

class Banks_branchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Banks_branches
        fields=('ifsc','bank_id','branch','address','city','district','state','bank_name')


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    '''def valiadate(self,data):
        username=data.get("username","")
        password=data.get("password","")
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"]=user
            else:
                    msg1 ="wrong"
                    raise exceptions.ValidationError(msg1)

        else:

            msg="Provide username"
            raise exceptions.ValidationError(msg)

        return data'''
