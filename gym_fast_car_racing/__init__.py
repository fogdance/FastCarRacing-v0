# -*- coding: utf-8 -*-
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

"""
Created on Wed Aug  9 12:36:38 2023

@author: Fei-y
"""
from gymnasium.envs.registration import register
from gym_fast_car_racing.FastCarRacing import FastCarRacing

register(
    id='FastCarRacing-v0',
    entry_point='gym_fast_car_racing:FastCarRacing',
    max_episode_steps=1000000000,
    reward_threshold=1500
)

