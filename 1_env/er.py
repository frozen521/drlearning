#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: er.py
@time: 2019/4/18 10:35
"""
import  time
N_STATES=6
FRESH_TIME=3
def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        print(interaction)
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print(interaction)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


if __name__ == "__main__":
    update_env('terminal',13,1)
