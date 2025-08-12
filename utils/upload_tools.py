#coding:UTF-8
__author__ = 'dj'

import random

# Validate upload file extension
def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['pcap', 'cap'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Get file extension
def get_filetype(filename):
    return '.' + filename.rsplit('.', 1)[1]

# Generate a random string filename
def random_name():
    return ''.join(random.sample('1234567890qazxswedcvfrtgbnhyujmkiolp', 10))