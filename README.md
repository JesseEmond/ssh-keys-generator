# SSH RSA key-pair generation
Generates an SSH RSA key-pair for **educational purposes** only.

*This originated from a friend offering to create a user for me on his
server and asking for generated SSH keys. I was working on an assignment
related to Miller-Rabin at the time and jokingly said that I would make the
generator myself. I ended up thinking that the experience would be worth it
figured that I would really do it. A couple of classes and late hours later,
her it is.*

Do not use in any serious context. Feel free to open issues or pull requests
if you want to improve this as a learning resource.

## Usage
```
> ./gen-ssh-keys.py --help
$ usage: gen-ssh-keys.py [-h] [--out output-file] [--bits BITS] [--verbose]
$                        [--comment COMMENT]
$
$ Generate an SSH RSA key pair.
$
$ optional arguments:
$   -h, --help            show this help message and exit
$   --out output-file, -o output-file
$                         File prefix for the key generated (output-file and
$                         output-file.pub)
$   --bits BITS, -b BITS  Length (in bits) of the key generated
$   --verbose, -v         If the current state should be printed as the keys are
$                         generated.
$   --comment COMMENT, -c COMMENT
$                         Comment to put in the public key file generated.
```

**Note**: assumes that you are using Python 3.

## Example
**Note**: can take multiple (>10-15) minutes to run with a relatively high amount
of bits for the prime numbers (e.g. 4096).
```
> ./gen-ssh-keys.py --verbose
$ Generating p...
$ Generating q...
$ Calculating RSA parameters...
$ Outputing private key to file...
$ Private key saved to: id_rsa
$ Outputing public key to file...
$ Public key saved to: id_rsa.pub
$ Done!
```

Public key generated:
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAEAQCIqB+ ... gYInDMtwHet4vwOmMublq9RxCCgK1FVkMmtvQeYq8JTywDcg2XbUF04wrCHXr 
```

Private key generated:
```
-----BEGIN RSA PRIVATE KEY-----
MIISJwIBAAKCBAEAiKgfrZnsSRXfY1SIdvB+ ... OAj4ktw1PPIzxx9sWgNL5DUbYBqMbdeuVf47iTEFNVT3ac2NfEltpQ==
-----END RSA PRIVATE KEY-----
```

## Setup
Run `./setup` to download the required dependencies (might need `sudo`).

**Note**: assumes that you have
[`pip`](https://pypi.python.org/pypi/pip) available.

## Running Unit Tests
Use `./run-tests` to execute the unit tests (conveniently does
`python -m unittest discover` for you).

## Documentation
For additional documentation on Miller-Rabin, see this other repository
related to primality testing: 
[benchmarkus-prime](https://github.com/JesseEmond/benchmarkus-prime).

### todo
- [x] Primality testing
- [x] Prime generation
- [x] RSA parameters generation
- [x] RSA public key format output
- [x] RSA private key format output
- [ ] Test with OpenSSH
