#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** MikrotikHack ***
# * Version:
#   v0.1

#  Ahmed Ameen 
# *******************************************************************


import sys,os
sys.path.append('./modules/')
from home import RunScript


class MIK(object):
    def __init__(self):
        pass

    def HOME(self):
        script, *values = sys.argv
        RunScript().run2() \
        if values == [] \
        else RunScript().run3()


if __name__ == '__main__':

    try:
        _FIND_ = os.listdir("..")
        if "logs" not in _FIND_: os.system("mkdir logs")

    except OSError:
        print(f"{W}[{R} - {W}]{B} Error mkdir logs ")
        exit()

    MIK().HOME()
