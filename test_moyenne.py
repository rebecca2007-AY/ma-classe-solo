import unittest

from moyenne import moyenne_ponderee, mention


class TestMoyenne(unittest.TestCase):
    def test_moyenne_simple(self):
        self.assertEqual(moyenne_ponderee([(10, 1), (20, 1)]), 15.0)

    def test_coefficients(self):
        self.assertEqual(moyenne_ponderee([(10, 1), (16, 2)]), 14.0)

    def test_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne_ponderee([])

class TestMention(unittest.TestCase):
    def test_seuils(self):
        self.assertEqual(mention(9.99), "Insuffisant")
        self.assertEqual(mention(10), "Passable")
        self.assertEqual(mention(12), "Assez bien")
        self.assertEqual(mention(14), "Bien")
        self.assertEqual(mention(16), "Très bien")


if __name__ == "__main__":
    unittest.main()
