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
import os
from lib.args import args

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        
        error = '\033[1;31m[-] \033[0m'
        
        outputfile = str(args.outputfile)
	
        if outputfile != "":
	    w = os.environ['OLDPWD']
    	    os.chdir(w)
            if os.path.isdir(outputfile):
	        if os.path.exists(outputfile):
	            if outputfile[-1:] == "/":
                        outputfile = outputfile + 'output.txt'
                        self.log = open(outputfile, "a")
                    else:
                        outputfile = outputfile + '/output.txt'
                        self.log = open(outputfile, "a")
	        else:
	            print(error+"Local directory: "+outputfile+": does not exist!")
		    g = os.environ['HOME']
    	    	    os.chdir(g + "/phonia")
                    sys.exit()
            else:
	        direct = os.path.split(outputfile)[0]
                if direct == "":
                    direct = "."
                else:
                    pass
	        if os.path.exists(direct):
                    if os.path.isdir(direct):
                        self.log = open(outputfile, "a")
                    else:
                        print(error+"Error: "+direct+": not a directory!")
			g = os.environ['HOME']
    	    	    	os.chdir(g + "/phonia")
                        sys.exit()
	        else:
	            print(error+"Local directory: "+direct+": does not exist!")
		    g = os.environ['HOME']
    	    	    os.chdir(g + "/phonia")
                    sys.exit()
	    g = os.environ['HOME']
    	    os.chdir(g + "/phonia")
        else:
            pass
            
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass
