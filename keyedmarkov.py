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
        4 points every training sequence that we want to output.

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
    """
    pass