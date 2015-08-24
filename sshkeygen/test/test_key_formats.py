from .. import key_formats, rsa
import unittest

class TestKeyFormats(unittest.TestCase):
    p = 0x00F0DAF9306BE54EE3E66B9A8ACF4F93245050B49682B330A9D9C4C7C408DFABD20D96372FDD0CE6935A9DDA269774EA3E39104D796C846D25AF6E02935362074BFB3A8F70BB4C4DDF59AEDFCB50B9E0E831ABB14E7ED6E659935F736AFE08B176E292A07B76C2BA4B62A4766AE468BB77FEF231A20088592881415EFA3A8A36D7
    q = 0x00EB4699695313DEF97DC6DCBED61E920EEC05275C18B4FFF77E9AB4BC30A544DAA06B534055439A437E654B1FDC00273FA98B1B3047532EA3F09DD2D1B1D2E2DB04EB3A27E5A51E56A88CDEA965C58DD7ADFA6C5D08D4228A57381844D50B150193F0289F2A70F2CB3E7917E946262C669D12939A4ADBFFA972394A8807167E61
    params = rsa.RsaParams(p, q)

    def test_public_key_blob(self):
        blob = key_formats.public_key_blob(self.params)

        self.assertEqual("AAAAB3NzaC1yc2EAAAADAQABAAABAQDdW271jTDWSuUHFXUlFTgqGjVtBM1TqnczCh1ZcUS1qrssr9jfpLa3gGg49aRQtjOKsHl2ZOym+/H5lhyuS2zVkNwZ7SUqmwjhwBiQfme40ZFKHp6urxO57++ljewngF20yr1tQCNq4/YDTf4dN9/V6v/EkP1cBWS/FMCmP2svkHSO8w819EQ8NIWBuXVd4e0E9HxdI+v76yGXBCLAyapadMho/xnh9DVSezO+XCkc4T6LVzQ43LbQklB1p17PoFFOZyn+rDpJKg2LSoM+v8eGuVyVKWziT0W54CB/0q4VK1lOBEqU5D71uWCBzLco1mxnarV1mlJZKijFPTjM1pl3", blob) 
