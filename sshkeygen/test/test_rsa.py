from ..rsa import RsaParams
import unittest

class TestRsa(unittest.TestCase):
    def test_rsa_params_sample_key(self):
        n = 0x00DD5B6EF58D30D64AE50715752515382A1A356D04CD53AA77330A1D597144B5AABB2CAFD8DFA4B6B7806838F5A450B6338AB0797664ECA6FBF1F9961CAE4B6CD590DC19ED252A9B08E1C018907E67B8D1914A1E9EAEAF13B9EFEFA58DEC27805DB4CABD6D40236AE3F6034DFE1D37DFD5EAFFC490FD5C0564BF14C0A63F6B2F90748EF30F35F4443C348581B9755DE1ED04F47C5D23EBFBEB21970422C0C9AA5A74C868FF19E1F435527B33BE5C291CE13E8B573438DCB6D0925075A75ECFA0514E6729FEAC3A492A0D8B4A833EBFC786B95C95296CE24F45B9E0207FD2AE152B594E044A94E43EF5B96081CCB728D66C676AB5759A52592A28C53D38CCD69977
        e = 0x010001
        d = 0x00C19C399F18D1807D9D78E6B1C1AF9FA263AE1B1EBA20D5D6D093A63C17304BDD7B3D88C91E43C975132115C0F4E98B93E55899C48E5DD76842AB553ADCD027EF5C76C74E7ED59728DB9BD3607ECF65FE1720474BEFEA3E4CC1AA5099A3D6A116550D8745C975B10696A529507C69E4A40C998D6A6BD052FF5D8A5F3E89F5CC70E2ADB852C5B0B44E55D46C2A842B625CF5369984D4C6C1C655F2F5F5986EEA212EDDBEC82B8F32E38D470F109E3EEC3F09A90071B40B552A6C38CE1B7A9831812B554F65B1B5175D758F2C2781D116554713ABCC37F272E316149BE499E273B74F5B06F7D823B652F5BB898D051D9663FB65BC09C419B3BF734D3989CE956281
        p = 0x00F0DAF9306BE54EE3E66B9A8ACF4F93245050B49682B330A9D9C4C7C408DFABD20D96372FDD0CE6935A9DDA269774EA3E39104D796C846D25AF6E02935362074BFB3A8F70BB4C4DDF59AEDFCB50B9E0E831ABB14E7ED6E659935F736AFE08B176E292A07B76C2BA4B62A4766AE468BB77FEF231A20088592881415EFA3A8A36D7
        q = 0x00EB4699695313DEF97DC6DCBED61E920EEC05275C18B4FFF77E9AB4BC30A544DAA06B534055439A437E654B1FDC00273FA98B1B3047532EA3F09DD2D1B1D2E2DB04EB3A27E5A51E56A88CDEA965C58DD7ADFA6C5D08D4228A57381844D50B150193F0289F2A70F2CB3E7917E946262C669D12939A4ADBFFA972394A8807167E61
        exp1 = 0x166A1A74A225E5F09999FBF8DD1027BE626710574D74859BD8F3522FF12F779B05BEAC061D493D100B87D32C723DE42AC43EBB2708AD4E470A8B6F5BEC8F9BE43B4E18D941E4F8FE47275A165EBDDDAB5E2BFF4531D2A7FF4012CAF7F30A3611BD462DFF2F6F31CD2031F3FF40A06A89E14502CF73C33CA0E35E850B3E756C63
        exp2 = 0x50B4C21148274BD88795BCC955C7DCD07393FD0171943D2DD7E717D26A5976FA0C0764E26F9D2600BB0DE22C469A62DC4ABB661334944B2E7F6E940FCC910BB297C85D05AC97EC854B822F2B2AB70EC60A6F19D6FC1D50CFE5C55F45D552DCDCD2B3922BAF325986F0A2375A94EEA95275D5167ED9E9079547927187A1EECC61
        coef = 0x5DD334247203C66E367E3BC0302CB1334C33F6AAD3178A05EA4A0F3DFA3ADB4E8354C9B6A7D330F9AF57E2769D13517E193B4655BDBE81261D6C672171C9C69B1893EC432DC83E949080DEF2044463B8D18A5855445A354878FC9FC095D2B35007D31D4373212836B6C4D0D1343813F415D9D0C74E0065631EBF695875999DB7

        params = RsaParams(p, q)

        self.assertEqual(p, params.prime1)
        self.assertEqual(q, params.prime2)
        self.assertEqual(n, params.modulus)
        self.assertEqual(e, params.publicExponent)
        self.assertEqual(d, params.privateExponent)
        self.assertEqual(exp1, params.exponent1)
        self.assertEqual(exp2, params.exponent2)
        self.assertEqual(coef, params.coefficient)