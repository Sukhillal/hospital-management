from django.db import models


# Create your models here.
class Dep(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_desc=models.TextField(max_length=100)
    
    def __str__(self) :
        return self.dep_name
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=50)
    doc_space=models.CharField(max_length=50)
    dep_name=models.ForeignKey(Dep,on_delete=models.CASCADE)
    dep_image=models.ImageField(upload_to="doctors")

    def __str__(self):
        return self.doc_name +"-("+self.doc_space+")"


class Booking(models.Model):
    p_name=models.CharField(max_length=25)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)  