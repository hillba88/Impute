#! /usr/bin/env python3
import numpy as np
from pomegranate import *

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
                        # makes dictionary with pos:ref:alt as key, and list of genotypes as values
                        key = "{0}:{1}:{2}".format(line[1], line[3], line[4])
                        geno_dict.setdefault(key, [])

                        for x in range(9, len(line)):
                            geno_dict[key].append(line[x])

        except IOError:
            print("Invalid file path!")

        return geno_dict

    '''
    parses genotype_dict, extracts genotypes for each sample, and replaces
    binary format with corresponding alleles for each SNP
    '''
    def parse_genotypes(self):
        genotypes = []

        for idx, vals in enumerate(self.genotype_dict().values()):
            for sample in vals:
                genotype = sample.split(':')[0]

                nucs = ''
                key = self.genotype_dict()
                for allele in genotype.split('/'):
                    if allele == 0:
                        nucs += key[idx].split(':')[1]
                    elif allele == 1:
                        nucs += key[idx].split(':')[2][0]
                    elif allele == 2:
                        nucs += key[idx].split(':')[2][1]
                    elif allele == '.':
                        nucts += '-'

                genotypes.append(nucs)

        return genotypes

'''
This function creates HMM states based on two input parameters: a
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
