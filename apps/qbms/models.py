from uuid import uuid4

from django.db import models

def generate_random_uuid():
    return str(uuid4())

# Create your models here.

class Transaction(models.Model):
    customer_name = models.CharField(max_length=80)
    customer_street = models.CharField(max_length=80)
    customer_city = models.CharField(max_length=40)
    customer_postal_code = models.CharField(max_length=10)
    comment = models.CharField(max_length=2048)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    masked_ccn = models.CharField(max_length=7)
    user_data = models.CharField(max_length=2048)
    auth_code = models.CharField(max_length=6)
    status = models.CharField(max_length=2048)
    status_code = models.CharField(max_length=4)
    status_message = models.CharField(max_length=2048)
    opid = models.CharField(max_length=50)
    txn_id = models.CharField(max_length=12)
    txn_timestamp = models.CharField(max_length=24)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uuid = models.CharField(max_length=36,default=generate_random_uuid)