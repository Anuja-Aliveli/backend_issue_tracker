import os
from django.db import connection
from django.core.mail import send_mail
from django.conf import settings

# Return All the Model fields
def get_model_fields(model_class):
    fields = model_class.__doc__.split(')')[0].split('(')[1].split(',')
    model_fields = []
    for field in fields:
        model_fields.append(field.lstrip(' '))
    return tuple(model_fields)

# Generate 13 length id based on previous id
def generate_id(type, latest_id):
    if latest_id is not None:
        sequential_number = int(latest_id[3:]) + 1
    else:
        sequential_number = 1
    sequential_number = f'{sequential_number:010d}'  # 10 digits
    new_user_id = f'{type}{sequential_number}'
    return new_user_id

# Gives the Latest ID of that particular table
def get_latest_id(model_name,field_name):
    latest_id = model_name.objects.order_by(f'-{field_name}').first()
    if latest_id:
        latest_id = getattr(latest_id, field_name)
    else:
        latest_id = None
    return latest_id
