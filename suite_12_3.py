import unittest
import test_runner
import test_tournament

tour_run_ST = unittest.TestSuite()

tour_run_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
tour_run_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(tour_run_ST)