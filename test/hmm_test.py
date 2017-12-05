#! /usr/bin/env python3

import argparse
import genotype_imp as gen
import numpy as np
from pomegranate import *

parser = argparse.ArgumentParser()
parser.add_argument('path', help='VCF path')
parser.add_argument('--ref', help='Reference haplotypes')
parser.add_argument('-o', help='Output file path')
parser.add_argument('-q', help='Minimum quality score')

args = parser.parse_args()
'''
Transition and emission probabilities obtained from:
    Swarts et al. (2014) Novel Methods to Optimize Genotypic Imputation for
    Low-Coverage, Next-Generation Sequence Data in Crop Plants. The Plant
    Genome, doi:10.3835/plantgenome2014.05.0023
'''
transition = np.matrix([[0.9990, 0.00010, 0.00300, 0.00010, 0.0005],
                        [0.0002, 0.99900, 0.00005, 0.00005, 0.0002],
                        [0.0002, 0.00005, 0.99900, 0.00005, 0.0002],
                        [0.0002, 0.00005, 0.00005, 0.99900, 0.0002],
                        [0.0005, 0.00010, 0.00030, 0.00010, 0.9990]])

emission = np.matrix([[0.998, 0.001, 0.001],
                      [0.600, 0.200, 0.200],
                      [0.400, 0.200, 0.400],
                      [0.200, 0.200, 0.600],
                      [0.001, 0.001, 0.998]])
