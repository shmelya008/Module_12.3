from tournament import Runner
from tournament import Tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print(i)

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        self.t1 = Tournament(90, self.r1, self.r3)
        self.results = (Tournament.start(self.t1))
        TournamentTest.all_results['a'] = self.results
        self.loser = max(self.results.keys())
        self.assertTrue(self.results.get(self.loser) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        self.t2 = Tournament(90, self.r2, self.r3)
        self.results = (Tournament.start(self.t2))
        TournamentTest.all_results['b'] = self.results
        self.loser = max(self.results.keys())
        self.assertTrue(self.results.get(self.loser) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        self.t3 = Tournament(90, self.r1, self.r2, self.r3)
        self.results = (Tournament.start(self.t3))
        TournamentTest.all_results['c'] = self.results
        self.loser = max(self.results.keys())
        self.assertTrue(self.results.get(self.loser) == 'Ник')


if __name__ == '__main__':
    unittest.main()



