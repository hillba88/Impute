#! /usr/bin/env python3

import argparse
import numpy as np
from pomegranate import *

parser = argparse.ArgumentParser()
parser.add_argument('path', help='VCF path')
parser.add_argument('--ref', help='Reference haplotypes')
parser.add_argument('-o', help='Output file path')
parser.add_argument('-q', help='Minimum quality score')

args = parser.parse_args()

class variants():

    def __init__(self, file, chr):
        self.file = file
        self.chr = chr

    '''
    loops through self.file and populates a dictionary with self.chr and a list
    of the samples as the keys and values, respectively
    '''
    def sample_list(self):
        samples = []

        try:
            with open(self.file, 'r') as snp_file:
                for line in snp_file:

                    if line.startswith("#") and not line.startswith("##"):
                        line = line.split()
                        for x in range(9, len(line)):
                            samples.append(line[x])

        except IOError:
            print("Invalid file path!")

        return samples

    '''
    loops through self.file and populates a dictionary with each chromosome
    position and the corresponding sample genotypes
    '''
    def genotype_dict(self):
        geno_dict = {}
        try:
            with open(self.file, 'r') as snp_file:
                for line in snp_file:
                    if not line.startswith("#"):
                        line = line.split()
                        geno_dict.setdefault(line[1], [])

                        for x in range(9, len(line)):
                            geno_dict[line[1]].append(line[x])

        except IOError:
            print("Invalid file path!")

        return geno_dict

    def parse_genotypes(self):
        genotypes = []

        for vals_list in self.genotype_dict().values():
            for sample in vals_list:
                genotypes.append(sample.split(':')[0])

        return genotypes


'''
This function creates states based on two input parameters: a
list of state names, and an optional parameter specifying a probability
distribution to use for each state. The default distribution specifies
equal probabilities for all nucleotide bases. Returns list of states
'''
def states(name_states, dist=DiscreteDistribution({'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25})):

    count = 0
    state_list = []

    try:
        for x in range(len(name_states)):
            state = "s{0}".format(x)
            state = State(dist, name=name_states[counter])
            state_list.append('s{0}'.format(x))
            count += 1

    except TypeError:
        print('{0} must be in list format'.format(states))

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
        for y in range(len(states)):
            hmm.add_transition(states[x], states[y], transition[y,x])

    hmm.bake()


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

hapmap = variants(args.path, 1)
print(hapmap.parse_genotypes())
