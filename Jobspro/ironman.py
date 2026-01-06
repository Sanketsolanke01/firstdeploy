import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Jobspro.settings")

import django
django.setup()

from faker import Faker
print("bye")
fake=Faker()
from random import randint
#hi
def phone():
    num=randint(1000000000,9999999999)
    return num

from jobsapp.models import Bangjobs,Punejobs,Biharjobs

def inserting(n):
    for i in range(n):  
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(['software devloper','phd','bca','mca'])
        fadd=fake.address()
        fsal=fake.random_int(min=20000,max=800000)
        femail=fake.email()
        fphone=phone()
        Bangjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,address=fadd,salary=fsal,email=femail,phone=fphone)
num=eval(input("Enter number of records to be inserted: "))
inserting(num)
print(f"{num} records inserted successfully")


def inserting(n):
    for i in range(n):  
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(['software devloper','phd','bca','mca'])
        fadd=fake.address()
        fsal=fake.random_int(min=20000,max=800000)
        femail=fake.email()
        fphone=phone()
        Punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,address=fadd,salary=fsal,email=femail,phone=fphone)
num=eval(input("Enter number of records to be inserted: "))
inserting(num)
print(f"{num} records inserted successfully")



def inserting(n):
    for i in range(n):  
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(['software devloper','phd','bca','mca'])
        fadd=fake.address()
        fsal=fake.random_int(min=20000,max=800000)
        femail=fake.email()
        fphone=phone()
        Biharjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,address=fadd,salary=fsal,email=femail,phone=fphone)
num=eval(input("Enter number of records to be inserted: "))
inserting(num)
print(f"{num} records inserted successfully")


