#!/usr/local/opt/python/bin/python3.7
# -*- coding: utf-8 -*-
import re
import sys

from flask.cli import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    if len(sys.argv) < 2:
	    sys.argv.append("run")
    sys.exit(main())
