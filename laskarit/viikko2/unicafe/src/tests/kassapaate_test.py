import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kassassa_rahaa_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_myytyja_edullisia_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyja_maukkaita_alussa_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_kasvattaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_kateisosto_edullinen_palauttaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_kateisosto_edullinen_kasvattaa_myytuja(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullinen_ei_riita_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kateisosto_edullinen_ei_riita_palauttaa_koko_maksun(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_edullinen_ei_riita_ei_kasvata_myytuja(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_kasvattaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_kateisosto_maukas_palauttaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_maukas_kasvattaa_myytuja(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukas_ei_riita_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kateisosto_maukas_ei_riita_palauttaa_koko_maksun(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_kateisosto_maukas_ei_riita_ei_kasvata_myytuja(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_veloittaa_korttia(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 7.6)

    def test_korttiosto_edullinen_palauttaa_true(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(tulos)

    def test_korttiosto_edullinen_kasvattaa_myytuja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_edullinen_ei_riita_ei_muuta_korttia(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 1.0)

    def test_korttiosto_edullinen_ei_riita_palauttaa_false(self):
        kortti = Maksukortti(100)
        tulos = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(tulos)

    def test_korttiosto_edullinen_ei_riita_ei_kasvata_myytuja(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_edullinen_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttiosto_maukas_veloittaa_korttia(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_korttiosto_maukas_palauttaa_true(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(tulos)

    def test_korttiosto_maukas_kasvattaa_myytuja(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_maukas_ei_riita_ei_muuta_korttia(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 1.0)

    def test_korttiosto_maukas_ei_riita_palauttaa_false(self):
        kortti = Maksukortti(100)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(tulos)

    def test_korttiosto_maukas_ei_riita_ei_kasvata_myytuja(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_maukas_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_lataus_kortille_muuttaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo_euroina(), 15.0)

    def test_lataus_kortille_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.0)

    def test_negatiivinen_lataus_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)

    def test_negatiivinen_lataus_ei_muuta_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
