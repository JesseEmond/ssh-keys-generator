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
TODO

**Note**: assumes that you are using Python 3.

## Example
TODO

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
[benchmarkus-prime](https://github.com/JesseEmond/benchmarkus-prime)

### todo
- [x] Primality testing
- [x] Prime generation
- [x] RSA parameters generation
- [x] RSA public key format output
- [x] RSA private key format output
- [ ] Test with OpenSSH
