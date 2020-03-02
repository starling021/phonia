#!/usr/bin/env python3

# MIT License
#
# Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import json
from lib.colors import *
from lib.args import args
from lib.logger import Logger

def plus(string):
    print("%s[+]%s %s%s" % (G % 1, S, string, E))

def warn(string):
    print("%s[!]%s %s%s" % (Y % 1, S, string, E))

def error(string):
    print("%s[-]%s %s%s" % (R % 1, S, string, E))

def test(string):
    print("%s[*]%s %s%s" % (B % 1, S, string, E))

def info(string):
    print("%s[i]%s %s%s" % (W % 1, S, string, E))

def more(string):
    print(" %s|%s  %s%s" % (W % 0, string, E))

def title(string):
    print("%s%s%s%s" % (BOLD, Y % 1, string, E))


def throw(string):
    error(string)
    sys.exit()


def askForExit():
    user_input = ask('\033[1;77m'+'[?]'+'\033[0m'+' Continue scanning? (y/N): '+'\033[0m')

    if user_input.lower() == 'y' or user_input.lower() == 'yes':
        return -1
    else:
        info("Good bye!")
        sys.exit()

def ask(text):
    sys.stdout = sys.__stdout__
    res = input(text)
    sys.stdout = Logger()

    return res
