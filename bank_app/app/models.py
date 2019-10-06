from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Banks_branches(models.Model):
    ifsc=models.CharField(max_length=20)
    bank_id=models.BigIntegerField()
    branch=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=30)
    bank_name=models.CharField(max_length=100)


    def __str__(self):
        return ("%s %s %s %s %s %s %s,%s" %(self.ifsc,self.bank_id,self.branch,self.address,
        self.city,self.district,self.state,self.bank_name
        ))
