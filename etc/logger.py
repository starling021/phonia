#!/usr/bin/env python3

import sys
import os
from lib.args import args

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        out = args.output
        import os
        import os.path
        if (os.path.exists("/tmp/phonia")):
            time.sleep(0)
        else:
            os.system("mkdir /tmp/phonia")

        if (os.path.exists("/tmp/phonia/phpath.temp")):
            os.system("rm /tmp/phonia/phpath.temp")
            os.system("echo $OLDPWD >> /tmp/phonia/phpath.temp")
        else:
            os.system("echo $OLDPWD >> /tmp/phonia/phpath.temp")

        if not '/' in args.output:
            output = open('/tmp/phonia/phpath.temp').read().split('\n')[-2]+'/'+args.output
            os.system("rm -rf /tmp/phonia")
        else:
            output = args.output
            os.system("rm -rf /tmp/phonia")
            
        self.log = open(output, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass
