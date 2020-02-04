#!/usr/bin/env python3

import argparse
from lib.banner import __version__

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--number', dest='number', help='The phone number to scan.')

parser.add_argument('-i', '--input', dest="inputfile", help='List of phone numbers to scan.')

parser.add_argument('-o', '--output', dest="outputfile", help='Output to save scan results.')

parser.add_argument('-s', '--scanner', dest="scanner", default="all", help='The scanner to use.')

parser.add_argument('--recon', action='store_true', help='Launch custom format reconnaissance.')

parser.add_argument('--no-ansi', action='store_true', help='Disable colored output.')

parser.add_argument('-u', '--update', action='store_true', help='Update Phonia Toolkit.')

args = parser.parse_args()
