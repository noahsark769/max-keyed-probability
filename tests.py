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
        emitter.train("kick", 1000)

        emitter.train("snare", 500)
        emitter.train("snare", 1500)
        emitter.end_sequence()

        data, buckets = emitter.get_data(True, True)
        # print buckets

        self.assertEquals(data[0]["hihat"], 1)
        self.assertEquals(data[0]["snare"], 0)
        self.assertEquals(data[0]["kick"], 1)

        self.assertEquals(data[1]["hihat"], 1)
        self.assertEquals(data[1]["snare"], 1)
        self.assertEquals(data[1]["kick"], 0)

        self.assertEquals(data[2]["hihat"], 1)
        self.assertEquals(data[2]["snare"], 0)
        self.assertEquals(data[2]["kick"], 1)

        self.assertEquals(data[3]["hihat"], 1)
        self.assertEquals(data[3]["snare"], 1)
        self.assertEquals(data[3]["kick"], 0)

        emitter.train("hihat", 0)
        emitter.train("hihat", 500)
        emitter.train("hihat", 1000)
        emitter.train("hihat", 1500)

        emitter.train("snare", 0)
        emitter.train("snare", 1000)

        emitter.train("kick", 500)
        emitter.train("kick", 1500)
        emitter.end_sequence()

        data, buckets = emitter.get_data(True, True)
        # print buckets

        self.assertEquals(data[0]["hihat"], 1)
        self.assertEquals(data[0]["snare"], 0.5)
        self.assertEquals(data[0]["kick"], 0.5)

        self.assertEquals(data[1]["hihat"], 1)
        self.assertEquals(data[1]["snare"], 0.5)
        self.assertEquals(data[1]["kick"], 0.5)

        self.assertEquals(data[2]["hihat"], 1)
        self.assertEquals(data[2]["snare"], 0.5)
        self.assertEquals(data[2]["kick"], 0.5)

        self.assertEquals(data[3]["hihat"], 1)
        self.assertEquals(data[3]["snare"], 0.5)
        self.assertEquals(data[3]["kick"], 0.5)

        emitter.train("hihat", 25)
        emitter.train("hihat", 531)
        emitter.train("hihat", 991)
        emitter.train("hihat", 1474)

        emitter.train("snare", 527)
        emitter.train("snare", 1502)

        emitter.train("kick", 13)
        emitter.train("kick", 1200)
        emitter.end_sequence()

        emitter.train("hihat", 173)
        emitter.train("hihat", 478)
        emitter.train("hihat", 1100)
        emitter.train("hihat", 1670)

        emitter.train("snare", 501)
        emitter.train("snare", 1471)

        emitter.train("kick", 1)
        emitter.train("kick", 1024)
        emitter.end_sequence()

        data, buckets = emitter.get_data(True, True)
        # print buckets

        self.assertEquals(data[0]["hihat"], 1)
        self.assertEquals(data[0]["snare"], 0.25)
        self.assertEquals(data[0]["kick"], 0.75)

        self.assertEquals(data[1]["hihat"], 1)
        self.assertEquals(data[1]["snare"], 0.75)
        self.assertEquals(data[1]["kick"], 0.25)

        self.assertEquals(data[2]["hihat"], 1)
        self.assertEquals(data[2]["snare"], 0.25)
        self.assertEquals(data[2]["kick"], 0.75)

        self.assertEquals(data[3]["hihat"], 1)
        self.assertEquals(data[3]["snare"], 0.75)
        self.assertEquals(data[3]["kick"], 0.25)

if __name__ == '__main__':
    unittest.main()