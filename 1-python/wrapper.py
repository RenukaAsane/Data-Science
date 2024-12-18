# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:55:12 2024

@author: Admin
"""
'''modular programming'''
#its use is reusability


import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f" took {total_time}mil sec")
        return result
    return wrapper