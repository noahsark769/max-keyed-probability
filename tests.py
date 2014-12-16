import unittest
from keyedmarkov import KeyedMarkovEmitter

class KeyedMarkovTestCase(unittest.TestCase):
    def test_normal(self):
        emitter = KeyedMarkovEmitter()
        emitter.setup(4, ["hihat", "snare", "kick"], 2000)

        emitter.train("hihat", 0)
        emitter.train("hihat", 500)
        emitter.train("hihat", 1000)
        emitter.train("hihat", 1500)

        emitter.train("kick", 0)
        emitter.train("kick", 100)

        emitter.train("snare", 500)
        emitter.train("snare", 1500)
        emitter.end_sequence()

    def test_slightly_offset(self):
        pass

if __name__ == '__main__':
    unittest.main()