#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: firsttouch.py
@time: 2019/4/1 18:49
"""
import tensorflow as tf
from tensorflow import keras
import pymongo
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)
fash_minist=keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_label)=fash_minist.load_data()
