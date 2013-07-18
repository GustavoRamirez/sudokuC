from coverage import coverage

cov = coverage()
cov.start()

import unittest
from test_recursive_solver import Testrecursive
from test_string import TestString
from test_peter_algorithm import TestPeterAlgorithm
from test_backtraking import UnitTestBacktrak


suite = unittest.TestSuite()

suite.addTests(unittest.makeSuite(Testrecursive))
suite.addTests(unittest.makeSuite(TestString))
suite.addTests(unittest.makeSuite(TestPeterAlgorithm))
suite.addTests(unittest.makeSuite(UnitTestBacktrak))


#
unittest.TextTestRunner(verbosity=2).run(suite)

cov.stop()
cov.html_report(directory='covhtml')