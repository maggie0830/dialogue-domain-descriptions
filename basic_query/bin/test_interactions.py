#!/usr/bin/env python
import subprocess
import sys
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-t", dest="test_name")

args = vars(parser.parse_args())

def extract_argument_value(argument):
    if "test_name" == argument and args[argument]:
        return ' -t "%s"' % args[argument]
    else:
        return ""

selected_test = extract_argument_value('test_name')

for language_code in ["eng", "fre", "dut"]:
    print "[%s] Running interaction tests" % language_code
    result = subprocess.call(
        "tdm_test_interactions.py -L %s" % language_code +
        " -f basic_query/test/interaction_tests_%s.txt" % language_code +
        selected_test,
        shell=True)
    if result:
        sys.exit(result)

sys.exit(0)
