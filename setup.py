# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 12:26:28 2023

@author: Fei-y
"""

from setuptools import setup

setup(
    name='gym_fast_car_racing',
    version='0.0.1',
    url='https://github.com/vFf0621/FastCarRacing-v0',
    description='Easy to train CarRacing-v2 Environment',
    packages=['gym_fast_car_racing'],
    install_requires=[
        'gymnasium[Box2d]',
	'torchvision',
	    'torch'
    ]
)


