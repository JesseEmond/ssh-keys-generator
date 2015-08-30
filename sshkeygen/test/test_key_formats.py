from .. import key_formats, rsa
import unittest

class TestKeyFormats(unittest.TestCase):
    p = 0x00F0DAF9306BE54EE3E66B9A8ACF4F93245050B49682B330A9D9C4C7C408DFABD20D96372FDD0CE6935A9DDA269774EA3E39104D796C846D25AF6E02935362074BFB3A8F70BB4C4DDF59AEDFCB50B9E0E831ABB14E7ED6E659935F736AFE08B176E292A07B76C2BA4B62A4766AE468BB77FEF231A20088592881415EFA3A8A36D7
    q = 0x00EB4699695313DEF97DC6DCBED61E920EEC05275C18B4FFF77E9AB4BC30A544DAA06B534055439A437E654B1FDC00273FA98B1B3047532EA3F09DD2D1B1D2E2DB04EB3A27E5A51E56A88CDEA965C58DD7ADFA6C5D08D4228A57381844D50B150193F0289F2A70F2CB3E7917E946262C669D12939A4ADBFFA972394A8807167E61
    params = rsa.RsaParams(p, q)

    def test_sample_public_key_blob(self):
        blob = key_formats.public_key_blob(self.params)

        self.assertEqual(b"AAAAB3NzaC1yc2EAAAADAQABAAABAQDdW271jTDWSuUHFXUlFTgqGjVtBM1TqnczCh1ZcUS1qrssr9jfpLa3gGg49aRQtjOKsHl2ZOym+/H5lhyuS2zVkNwZ7SUqmwjhwBiQfme40ZFKHp6urxO57++ljewngF20yr1tQCNq4/YDTf4dN9/V6v/EkP1cBWS/FMCmP2svkHSO8w819EQ8NIWBuXVd4e0E9HxdI+v76yGXBCLAyapadMho/xnh9DVSezO+XCkc4T6LVzQ43LbQklB1p17PoFFOZyn+rDpJKg2LSoM+v8eGuVyVKWziT0W54CB/0q4VK1lOBEqU5D71uWCBzLco1mxnarV1mlJZKijFPTjM1pl3", blob) 

    def test_sample_public_key(self):
        key = key_formats.public_key(self.params, 'dysleixa@arch')

        self.assertEqual("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdW271jTDWSuUHFXUlFTgqGjVtBM1TqnczCh1ZcUS1qrssr9jfpLa3gGg49aRQtjOKsHl2ZOym+/H5lhyuS2zVkNwZ7SUqmwjhwBiQfme40ZFKHp6urxO57++ljewngF20yr1tQCNq4/YDTf4dN9/V6v/EkP1cBWS/FMCmP2svkHSO8w819EQ8NIWBuXVd4e0E9HxdI+v76yGXBCLAyapadMho/xnh9DVSezO+XCkc4T6LVzQ43LbQklB1p17PoFFOZyn+rDpJKg2LSoM+v8eGuVyVKWziT0W54CB/0q4VK1lOBEqU5D71uWCBzLco1mxnarV1mlJZKijFPTjM1pl3 dysleixa@arch", key)

    def test_sample_private_key_blob(self):
        blob = key_formats.private_key_blob(self.params)

        self.assertEqual(b"MIIEowIBAAKCAQEA3Vtu9Y0w1krlBxV1JRU4Kho1bQTNU6p3MwodWXFEtaq7LK/Y36S2t4BoOPWkULYzirB5dmTspvvx+ZYcrkts1ZDcGe0lKpsI4cAYkH5nuNGRSh6erq8Tue/vpY3sJ4BdtMq9bUAjauP2A03+HTff1er/xJD9XAVkvxTApj9rL5B0jvMPNfREPDSFgbl1XeHtBPR8XSPr++shlwQiwMmqWnTIaP8Z4fQ1UnszvlwpHOE+i1c0ONy20JJQdadez6BRTmcp/qw6SSoNi0qDPr/HhrlclSls4k9FueAgf9KuFStZTgRKlOQ+9blggcy3KNZsZ2q1dZpSWSooxT04zNaZdwIDAQABAoIBAQDBnDmfGNGAfZ145rHBr5+iY64bHrog1dbQk6Y8FzBL3Xs9iMkeQ8l1EyEVwPTpi5PlWJnEjl3XaEKrVTrc0CfvXHbHTn7Vlyjbm9Ngfs9l/hcgR0vv6j5MwapQmaPWoRZVDYdFyXWxBpalKVB8aeSkDJmNamvQUv9dil8+ifXMcOKtuFLFsLROVdRsKoQrYlz1NpmE1MbBxlXy9fWYbuohLt2+yCuPMuONRw8Qnj7sPwmpAHG0C1UqbDjOG3qYMYErVU9lsbUXXXWPLCeB0RZVRxOrzDfycuMWFJvkmeJzt09bBvfYI7ZS9buJjQUdlmP7ZbwJxBmzv3NNOYnOlWKBAoGBAPDa+TBr5U7j5muais9PkyRQULSWgrMwqdnEx8QI36vSDZY3L90M5pNandoml3TqPjkQTXlshG0lr24Ck1NiB0v7Oo9wu0xN31mu38tQueDoMauxTn7W5lmTX3Nq/gixduKSoHt2wrpLYqR2auRou3f+8jGiAIhZKIFBXvo6ijbXAoGBAOtGmWlTE975fcbcvtYekg7sBSdcGLT/936atLwwpUTaoGtTQFVDmkN+ZUsf3AAnP6mLGzBHUy6j8J3S0bHS4tsE6zon5aUeVqiM3qllxY3XrfpsXQjUIopXOBhE1QsVAZPwKJ8qcPLLPnkX6UYmLGadEpOaStv/qXI5SogHFn5hAoGAFmoadKIl5fCZmfv43RAnvmJnEFdNdIWb2PNSL/Evd5sFvqwGHUk9EAuH0yxyPeQqxD67JwitTkcKi29b7I+b5DtOGNlB5Pj+RydaFl693ateK/9FMdKn/0ASyvfzCjYRvUYt/y9vMc0gMfP/QKBqieFFAs9zwzyg416FCz51bGMCgYBQtMIRSCdL2IeVvMlVx9zQc5P9AXGUPS3X5xfSall2+gwHZOJvnSYAuw3iLEaaYtxKu2YTNJRLLn9ulA/MkQuyl8hdBayX7IVLgi8rKrcOxgpvGdb8HVDP5cVfRdVS3NzSs5IrrzJZhvCiN1qU7qlSddUWftnpB5VHknGHoe7MYQKBgF3TNCRyA8ZuNn47wDAssTNMM/aq0xeKBepKDz36OttOg1TJtqfTMPmvV+J2nRNRfhk7RlW9voEmHWxnIXHJxpsYk+xDLcg+lJCA3vIERGO40YpYVURaNUh4/J/AldKzUAfTHUNzISg2tsTQ0TQ4E/QV2dDHTgBlYx6/aVh1mZ23", blob)

    def test_sample_private_key(self):
        key = key_formats.private_key(self.params)

        self.assertEqual("-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA3Vtu9Y0w1krlBxV1JRU4Kho1bQTNU6p3MwodWXFEtaq7LK/Y36S2t4BoOPWkULYzirB5dmTspvvx+ZYcrkts1ZDcGe0lKpsI4cAYkH5nuNGRSh6erq8Tue/vpY3sJ4BdtMq9bUAjauP2A03+HTff1er/xJD9XAVkvxTApj9rL5B0jvMPNfREPDSFgbl1XeHtBPR8XSPr++shlwQiwMmqWnTIaP8Z4fQ1UnszvlwpHOE+i1c0ONy20JJQdadez6BRTmcp/qw6SSoNi0qDPr/HhrlclSls4k9FueAgf9KuFStZTgRKlOQ+9blggcy3KNZsZ2q1dZpSWSooxT04zNaZdwIDAQABAoIBAQDBnDmfGNGAfZ145rHBr5+iY64bHrog1dbQk6Y8FzBL3Xs9iMkeQ8l1EyEVwPTpi5PlWJnEjl3XaEKrVTrc0CfvXHbHTn7Vlyjbm9Ngfs9l/hcgR0vv6j5MwapQmaPWoRZVDYdFyXWxBpalKVB8aeSkDJmNamvQUv9dil8+ifXMcOKtuFLFsLROVdRsKoQrYlz1NpmE1MbBxlXy9fWYbuohLt2+yCuPMuONRw8Qnj7sPwmpAHG0C1UqbDjOG3qYMYErVU9lsbUXXXWPLCeB0RZVRxOrzDfycuMWFJvkmeJzt09bBvfYI7ZS9buJjQUdlmP7ZbwJxBmzv3NNOYnOlWKBAoGBAPDa+TBr5U7j5muais9PkyRQULSWgrMwqdnEx8QI36vSDZY3L90M5pNandoml3TqPjkQTXlshG0lr24Ck1NiB0v7Oo9wu0xN31mu38tQueDoMauxTn7W5lmTX3Nq/gixduKSoHt2wrpLYqR2auRou3f+8jGiAIhZKIFBXvo6ijbXAoGBAOtGmWlTE975fcbcvtYekg7sBSdcGLT/936atLwwpUTaoGtTQFVDmkN+ZUsf3AAnP6mLGzBHUy6j8J3S0bHS4tsE6zon5aUeVqiM3qllxY3XrfpsXQjUIopXOBhE1QsVAZPwKJ8qcPLLPnkX6UYmLGadEpOaStv/qXI5SogHFn5hAoGAFmoadKIl5fCZmfv43RAnvmJnEFdNdIWb2PNSL/Evd5sFvqwGHUk9EAuH0yxyPeQqxD67JwitTkcKi29b7I+b5DtOGNlB5Pj+RydaFl693ateK/9FMdKn/0ASyvfzCjYRvUYt/y9vMc0gMfP/QKBqieFFAs9zwzyg416FCz51bGMCgYBQtMIRSCdL2IeVvMlVx9zQc5P9AXGUPS3X5xfSall2+gwHZOJvnSYAuw3iLEaaYtxKu2YTNJRLLn9ulA/MkQuyl8hdBayX7IVLgi8rKrcOxgpvGdb8HVDP5cVfRdVS3NzSs5IrrzJZhvCiN1qU7qlSddUWftnpB5VHknGHoe7MYQKBgF3TNCRyA8ZuNn47wDAssTNMM/aq0xeKBepKDz36OttOg1TJtqfTMPmvV+J2nRNRfhk7RlW9voEmHWxnIXHJxpsYk+xDLcg+lJCA3vIERGO40YpYVURaNUh4/J/AldKzUAfTHUNzISg2tsTQ0TQ4E/QV2dDHTgBlYx6/aVh1mZ23\n-----END RSA PRIVATE KEY-----", key)


