#!/usr/bin/env python

import subprocess
import sys

result = subprocess.call(
    "tdm_build.py --ddds basic_action -asr android -L eng",
    shell=True)
sys.exit(result)
