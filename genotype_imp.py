#! /usr/bin/env python3

import argparse
import numpy as np
from collections import counter
from pomegranate import *

parser = argparse.ArumentParser()
parser.add_argument("path", help="VCF path")
parser.add_argument("ref", help="Reference haplotypes")
parser.add_argument("-o", help="Output file path")
parser.add_argument("-q", help="Minimum quality score")

args = parser.parse_args()

d1 = DiscreteDistribution({'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25})
d2 = DiscreteDistribution({'A': 0.10, 'C': 0.40, 'G': 0.40, 'T': 0.10})

def states(dist, states)
    count = 0
    if type(states) is not list: states = [ states ]

    for x in range(states):
        "s{0}".format(x) = State(dist, name=states[counter])
        count += 1

s1 = State( d1, name='AA' )
s2 = State( d1, name='3A:1B' )
s3 = State( d1, name='1A:1B' )
s4 = State( d1, name='1A:3B' )
s5 = State( d1, name='BB' )

def transition_probs(states):
    start_prob = float(100/states)
    hmm = HiddenMarkovModel

    for x in range(states):
        hmm.add_states(x)
        hmm.add_transition(hmm.start, x, start_prob)




hmm.add_transition( s1, s1, 0.5 )
hmm.add_transition( s1, s2, 0.5 )
hmm.add_transition( s2, s1, 0.5 )
hmm.add_transition( s2, s2, 0.5 )
hmm.bake()
