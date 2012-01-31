import unittest
import rigor


class PreconditionTests(unittest.TestCase):
    def test_true_does_nothing(self):
        rigor.precond(True)

    def test_false_throws_precondition_error(self):
        self.assertRaises(rigor.PreconditionError, rigor.precond, (False))


class PostconditionTests(unittest.TestCase):
    def test_true_does_nothing(self):
        rigor.postcond(True)

    def test_false_throws_postcondition_error(self):
        self.assertRaises(rigor.PostconditionError, rigor.postcond, (False))


if __name__ == "__main__":
    unittest.main()
