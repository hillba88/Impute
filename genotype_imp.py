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

'''
This function creates states based on two input parameters: a
list of state names, and an optional parameter specifying a probability
distribution to use for each state. The default distribution specifies
equal probabilities for all nucleotide bases. Returns list of states
'''
def states(name_states, dist=DiscreteDistribution({'A': 0.25, 'C': 0.25,
                                                   'G': 0.25, 'T': 0.25}))
    count = 0
    state_list = []
    try:
        for x in range(len(name_states)):
            "s{0}".format(x) = State(dist, name=name_states[counter])
            state_list.append("s{0}".format(x))
            count += 1

    except TypeError:
        print("{0} must be in list format".format(states))

    return state_list

'''
This function creates a HMM, adds states and state transitions. The function
takes two arguments, a list of states and a transition probability matrix.
'''
def transition(states, transition):
    start_prob = float(100/states)
    hmm = HiddenMarkovModel

    for item in states:
        hmm.add_states(item)
        hmm.add_transition(hmm.start, item, start_prob)

    for x in range(len(states)):
        hmm.add_transition(states[x], states[x], transition[x,x])
        for y in range(x+1, len(states)):
            hmm.add_transition(states[x], states[y], transition[y,x])

    hmm.bake()


'''
Transition and emission probabilities obtained from
    Swarts et al. (2014) Novel Methods to Optimize Genotypic Imputation for
    Low-Coverage, Next-Generation Sequence Data in Crop Plants. The Plant
    Genome, doi:10.3835/plantgenome2014.05.0023
''''
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
