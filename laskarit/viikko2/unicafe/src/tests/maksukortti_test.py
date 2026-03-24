import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)
        
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(500)
        self.assertEqual(self.kortti.saldo_euroina(), 15.0)
        
    def test_rahan_ottaminen_vahentaa_saldoa_oikein(self):
        self.kortti.ota_rahaa(500)
        self.assertEqual(self.kortti.saldo_euroina(), 5.0)
        
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.kortti.ota_rahaa(2000)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)
        
    def test_ota_rahaa_palauttaa_true_jos_rahat_riittaa(self):
        tulos = self.kortti.ota_rahaa(500)
        self.assertEqual(tulos, True)
        
    def test_ota_rahaa_palauttaa_false_jos_rahat_ei_riita(self):
        tulos = self.kortti.ota_rahaa(2000)
        self.assertEqual(tulos, False)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)

    def test_str_palauttaa_oikean_merkkijonon(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
