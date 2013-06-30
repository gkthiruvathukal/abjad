from abjad.tools.pitchtools.IntervalSegment import IntervalSegment


class HarmonicChromaticIntervalSegment(IntervalSegment):
    '''.. versionadded:: 2.0

    Abjad model of harmonic chromatic interval segment:

    ::

        >>> pitchtools.HarmonicChromaticIntervalSegment([10, -12, -13, -13.5])
        HarmonicChromaticIntervalSegment(10, 12, 13, 13.5)

    Harmonic chromatic interval segments are immutable.
    '''

    ### CONSTRUCTOR ###

    def __new__(self, hci_tokens):
        from abjad.tools import pitchtools
        hcis = []
        for token in hci_tokens:
            hci = pitchtools.HarmonicChromaticInterval(token)
            hcis.append(hci)
        return tuple.__new__(self, hcis)
