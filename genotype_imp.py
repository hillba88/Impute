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

'''
function takes two arguments: a list of state names, and an optional parameter
specifying a probability distribution to use for each state. The default
distribution specifies equal probabilities for all nucleotide bases
'''
def states(name_states, dist=DiscreteDistribution({'A': 0.25, 'C': 0.25,
                                                   'G': 0.25, 'T': 0.25}))
    count = 0

    try:
        for x in range(len(name_states)):
            "s{0}".format(x) = State(dist, name=name_states[counter])
            count += 1

    except TypeError:
        print("{0} must be in list format".format(states))

def transition_probs(num_states, ):
    start_prob = float(100/states)
    hmm = HiddenMarkovModel

    for x in range(states):
        hmm.add_states(x)
        hmm.add_transition(hmm.start, x, start_prob)

    for x in range(states):





hmm.add_transition( s1, s1, 0.5 )
hmm.add_transition( s1, s2, 0.5 )
hmm.add_transition( s2, s1, 0.5 )
hmm.add_transition( s2, s2, 0.5 )
hmm.bake()
