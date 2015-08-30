#!/bin/python

import argparse, random
from sshkeygen import primes, rsa, key_formats

parser = argparse.ArgumentParser(description='Generate an SSH RSA key pair.')
parser.add_argument('--out', '-o', metavar='output-file', default='id_rsa',
                    help='File prefix for the key generated (output-file and output-file.pub)')
parser.add_argument('--bits', '-b', default=4096, type=int,
                    help='Length (in bits) of the key generated')
parser.add_argument('--verbose', '-v', default=False, action="store_true",
                    help='If the current state should be printed as the keys are generated.')
parser.add_argument('--comment', '-c', default="", type=str,
                    help='Comment to put in the public key file generated.')

args = parser.parse_args()


rand = random.SystemRandom()

if args.verbose: print('Generating p...')
p = primes.random_prime(rand, args.bits)

if args.verbose: print('Generating q...')
q = primes.random_prime(rand, args.bits)

if args.verbose: print('Calculating RSA parameters...')
keys = rsa.RsaParams(p, q)

if args.verbose: print('Outputing private key to file...')
privateKey = key_formats.private_key(keys)
privateFileName = args.out
with open(privateFileName, 'w') as privateFile:
    privateFile.write(privateKey)
if args.verbose: print('Private key saved to: ' + privateFileName)

if args.verbose: print('Outputing public key to file...')
publicKey = key_formats.public_key(keys, args.comment)
publicFileName = args.out + '.pub'
with open(publicFileName, 'w') as publicFile:
    publicFile.write(publicKey)
if args.verbose: print('Public key saved to: ' + publicFileName)

if args.verbose: print('Done!')
