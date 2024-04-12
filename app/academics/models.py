from django.db import models
import datetime
# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        abstract = True

class User(DateTimeModel):
    email = models.EmailField(null = True, blank = True, default = True)
    password = models.CharField(null = True, blank = True, default = True)
    status = models.BooleanField(null = True, blank = True, default = True)
    def __str__(self):
        return self.email
    
class Person(DateTimeModel):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length=12, blank=True)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE, blank = False, null = False, default = 1)

class Student(DateTimeModel):
    code = models.CharField(max_length=50)
    id_person = models.IntegerField()
    status = models.BooleanField(null = True, blank = True, default = True)

class Countrie(DateTimeModel):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)

class Department(DateTimeModel):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_country = models.IntegerField()

class Citie(DateTimeModel):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_dept = models.IntegerField()

class Identification_types(DateTimeModel):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)