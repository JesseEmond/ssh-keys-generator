#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Generate an SSH RSA key pair.')
parser.add_argument('--out', '-o', metavar='output-file', default='id_rsa',
                    help='File prefix for the key generated (output-file and output-file.pub)')
parser.add_argument('--bits', '-b', default=4096, type=int,
                    help='Length (in bits) of the key generated')
parser.add_argument('--verbose', '-v', default=False, type=bool,
                    help='If the current state should be print as the keys are generated.')

args = parser.parse_args()

print(args)
#TODO

