#!/bin/python

import argparse, random
from lib import primes, rsa

parser = argparse.ArgumentParser(description='Generate an SSH RSA key pair.')
parser.add_argument('--out', '-o', metavar='output-file', default='id_rsa',
                    help='File prefix for the key generated (output-file and output-file.pub)')
parser.add_argument('--bits', '-b', default=4096, type=int,
                    help='Length (in bits) of the key generated')
parser.add_argument('--verbose', '-v', default=False, action="store_true",
                    help='If the current state should be printed as the keys are generated.')

args = parser.parse_args()


rand = random.SystemRandom()

if args.verbose: print('Generating p...')
p = primes.random_prime(rand, args.bits)

if args.verbose: print('Generating q...')
q = primes.random_prime(rand, args.bits)

if args.verbose: print('Calculating RSA parameters...')
keys = rsa.RsaParams(p, q)

if args.verbose: print('Outputing to file...')
print("#TODO output to file here")

if args.verbose: print('Done!')
