import os
from django.db import connection
from django.core.mail import send_mail
from django.conf import settings
from collections import defaultdict
import bisect

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

# Send Email
def send_email(subject, message, to_id):
    send_mail(
    subject=subject,
    message=None,
    from_email="noreply.test.issuetracker@gmail.com",
    recipient_list=[to_id],
    fail_silently=False,
    html_message=message,
)
    
# Return Paginated data based on limit and page
def get_paginated_data(data, page = 1, limit = 10):
    start = (page - 1) * limit
    end = start + limit
    return data[start:end]

# Perform Search on list of dictionaries using inverted index
def build_inverted_index(list_data):
    inverted_index = defaultdict(set)
    for idx, project in enumerate(list_data):
        for value in project.values():
            words = str(value).lower().split()
            for word in words:
                inverted_index[word].add(idx)
    return inverted_index

def get_search_results(search_input, list_data):
    inverted_index = build_inverted_index(list_data)
    search_words = search_input.lower().split()
    
    if not search_words:
        return []

    result_indices = set(inverted_index[search_words[0]])
    for word in search_words[1:]:
        result_indices &= inverted_index[word]

    search_results = [list_data[i] for i in result_indices]
    return search_results

# Perform custom sort based on quick sort
def partition(data, low, high, key):
    pivot = data[(low + high) // 2].get(key, '')
    i, j = low - 1, high + 1
    while True:
        i += 1
        while data[i].get(key, '') < pivot:
            i += 1
        j -= 1
        while data[j].get(key, '') > pivot:
            j -= 1
        if i >= j:
            return j
        data[i], data[j] = data[j], data[i]

def quicksort(data, low, high, key):
    if low < high:
        split = partition(data, low, high, key)
        quicksort(data, low, split, key)
        quicksort(data, split + 1, high, key)

def custom_sort(data, key, reverse=False):
    quicksort(data, 0, len(data) - 1, key)
    return data if not reverse else data[::-1]

# Perform Filter using binary search
def create_index(data, keys):
    index = {key: defaultdict(list) for key in keys}
    for i, item in enumerate(data):
        for key in keys:
            value = str(item.get(key, '')).lower()
            index[key][value].append(i)
    return index

def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    return -1

def apply_filters(data, filters):
    if not filters:
        return data

    # Create an index for faster lookups
    index = create_index(data, filters.keys())

    # Find common indices that satisfy all filters
    common_indices = set(range(len(data)))
    for key, value in filters.items():
        filter_value = str(value).lower()
        if key in index and filter_value in index[key]:
            common_indices &= set(index[key][filter_value])
        else:
            return []

    return [data[i] for i in sorted(common_indices)]

# Apply search sort filter
def apply_search_sort_filter_pagination(list_data, filters='{}',search_input='',sort_param='created_at desc',page = '1',limit='10'):
    page = int(page)
    limit = int(limit)
    sort_by, sort_order = sort_param.split()
    reverse = sort_order.lower() == 'desc'
    list_data = apply_filters(list_data, filters)
    if search_input:
        list_data = get_search_results(search_input, list_data)
    list_data = custom_sort(list_data, key=sort_by, reverse=reverse)
    list_data = get_paginated_data(list_data, page, limit)
    return list_data