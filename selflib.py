__author__ = 'tommy'
from hashlib import md5
def get_md5(string):
    return md5(string).hexdigest()