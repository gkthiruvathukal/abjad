from abjad.tools.pitchtools.CounterpointInterval import CounterpointInterval
from abjad.tools.pitchtools.HarmonicInterval import HarmonicInterval


class HarmonicCounterpointInterval(CounterpointInterval, HarmonicInterval):
    '''.. versionadded:: 2.0

    Abjad model of harmonic counterpoint interval:

    ::

        >>> pitchtools.HarmonicCounterpointInterval(-9)
        HarmonicCounterpointInterval(9)

    Harmonic counterpoint intervals are immutable.
    '''

    ### INITIALIZER ###

    def __init__(self, token):
        from abjad.tools import pitchtools
        if isinstance(token, int):
            _number = abs(token)
        elif isinstance(token, pitchtools.DiatonicInterval):
            _number = abs(token.number)
        else:
            raise TypeError('must be number or diatonic interval.')
        object.__setattr__(self, '_number', _number)

    ### SPECIAL METHODS ###

    def __eq__(self, arg):
        if isinstance(arg, type(self)):
            if self.number == arg.number:
                return True
        return False

    def __ne__(self, arg):
        return not self == arg

    ### PUBLIC PROPERTIES ###

    @property
    def harmonic_counterpoint_interval_class(self):
        from abjad.tools import pitchtools
        return pitchtools.HarmonicCounterpointIntervalClass(self)
