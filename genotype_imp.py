#! /usr/bin/env python3

import argparse
from pomegranate import *
import numpy as np

parser = argparse.ArumentParser()
parser.add_argument("path", help="VCF path")
parser.add_argument("ref", help="Reference haplotypes")
parser.add_argument("-o", help="Output file path")
parser.add_argument("-q", help="Minimum quality score")

args = parser.parse_args()
