# simple demo for read txt file
import os
import sys
import time


def resource_path(relative_path):
    """get absolute path of resource"""
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    time.sleep(1)

# open bundle file
with open(resource_path('test_bundle.txt'), 'r', encoding='utf-8') as f:
    print(f.read())
    time.sleep(10)
