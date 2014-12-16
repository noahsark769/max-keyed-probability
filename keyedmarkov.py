from random import random

class KeyedMarkovEmitter(object):
    """The keyed markov emitter is an object which can accept training data
    based on different keys and can emit back a probabalistic model of the given
    keys.

    To train the emitter, we can call something like this:

    emitter.train("key", 1234)

    where "key" is the key we observed from training data, and 1234 is the
    millisecond offset that we observed it at. The emitter can then emit
    interpolated data. It must be:

    (1) Configured with an interval to look for: this will denote how much
        interpolated data it outputs. For example, if we wanted to implement
        a drum machine that played intstuments probabilstcally every beat of
        a measure, we would set the interal to 0.25 to denote that there are
        4 points every training sequence that we want to output. We an also
        set this interval implicitly using the number of buckets which we
        want to divide the training sequence into.

        If this was the case, then the emitter would output an array of four
        dictionaries, where the keys of the dictionaries might be something
        like "snare", "hihat", etc, and the values would be a boolean stating
        whether to play that instrument on that beat. Additionally, we could
        output the values as floats representing the probability of playing
        that instrument.

    (2) Told what keys it is looking for. Technically, it could just add a new
        key every time it sees a new one, but requiring it to know about all
        keys it will see will make it a little better and easier to debug.

    (3) Told when it's done with a training sequence. This is because, in order
        to interpolate the probability of seeing a key at a specified time
        interval, the emitter must also know when it has NOT seen that key in
        that interval. You can also use the emitter.train_sequence method to
        train an entire sequence at once.

    (4) Told how long, in milliseconds, the training sequences will be.
    """

    def __init__(self):
        self.sequences_seen = 0
        self.known_keys = set()
        self.num_buckets = 0
        self.sequence_length = 0

    def setup(self, num_buckets, keys, sequence_length):
        self.add_keys(*keys)
        self.set_sequence_length(sequence_length)
        self.set_num_buckets(num_buckets)

    def set_num_buckets(self, num_buckets):
        """Important: MUST BE CALLED AFTER ADD_KEYS"""
        self.num_buckets = num_buckets
        self.buckets = dict((i, (dict((key, []) for key in self.known_keys))) for i in range(0, self.num_buckets))

    def add_keys(self, *args):
        for key in args:
            self.known_keys.add(key)

    def set_sequence_length(self, length):
        self.sequence_length = length

    def end_sequence(self):
        self.sequences_seen += 1

    def train(self, key, offset):
        """Train the emitter on a specific key seen at a specific offset.

        This should be called in the following way:

        emitter.train(...)
        emitter.train(...)
        emitter.train(...)
        ...
        emitter.end_sequence()
        """
        # ratio = offset / self.sequence_length
        interval_length = self.sequence_length / float(self.num_buckets)
        # print "Offset: " + str(offset)
        # print "Interval length: " + str(interval_length)
        if offset < interval_length / 2 or offset >= (self.num_buckets * 2 - 1) * interval_length / 2:
            correct_bucket = 0
        else:
            for i in range(2, self.num_buckets + 1):
                # print "i: " + str(i)
                # print "Lower bound: " + str(float((i - 1) * 2 - 1) / 2 * interval_length)
                # print "Upper bound bound: " + str(float((i) * 2 - 1) / 2 * interval_length)
                if offset >= float((i - 1) * 2 - 1) / 2 * interval_length and offset < float((i) * 2 - 1) / 2 * interval_length:
                    correct_bucket = i - 1 # oh god i hope this is right
                    break
        self.buckets[correct_bucket][key].append(offset)

    def train_sequence(self, sequence):
        for training in sequence:
            self.train(training["key"], training["offset"])
        self.end_sequence()

    def get_data(self, use_probability_instead=False, return_buckets=False):
        result = []
        for bucket_index in self.buckets.keys():
            bucket_result = {}
            for key in self.known_keys:
                probability = float(len(self.buckets[bucket_index][key])) / self.sequences_seen
                if use_probability_instead:
                    bucket_result[key] = probability
                else:
                    rand_float = random()
                    bucket_result[key] = rand_float <= probability
            result.append(bucket_result)
        if return_buckets:
            return result, self.buckets
        return result

