# -*- encoding: utf-8 -*-
from abjad.tools import mathtools
from abjad.tools.pitchtools.NumberedInterval import NumberedInterval
from abjad.tools.pitchtools.MelodicInterval import MelodicInterval


class MelodicChromaticInterval(NumberedInterval, MelodicInterval):
    '''Abjad model of melodic chromatic interval:

    ::

        >>> mci = pitchtools.MelodicChromaticInterval(-14)
        >>> mci
        MelodicChromaticInterval(-14)

    Melodic chromatic intervals are immutable.
    '''

    ### INITIALIZER ###

    def __init__(self, arg):
        from abjad.tools import pitchtools
        if isinstance(arg, (int, float, long)):
            number = arg
        elif isinstance(arg, pitchtools.Interval):
            number = arg.semitones
        else:
            raise TypeError('%s must be number or interval.' % arg)
        object.__setattr__(self, '_number', number)

    ### SPECIAL METHODS ###

    def __abs__(self):
        return self.harmonic_chromatic_interval

    def __ge__(self, arg):
        if not isinstance(arg, type(self)):
            raise TypeError('%s must be melodic chromatic interval.' % arg)
        if not self.direction_number == arg.direction_number:
            raise ValueError(
                'can only compare melodic intervals of same direction.')
        return abs(self.number) >= abs(arg.number)

    def __gt__(self, arg):
        if not isinstance(arg, type(self)):
            raise TypeError('%s must be melodic chromatic interval.' % arg)
        if not self.direction_number == arg.direction_number:
            raise ValueError(
                'can only compare melodic intervals of same direction.')
        return abs(self.number) > abs(arg.number)

    def __hash__(self):
        return hash(repr(self))

    def __le__(self, arg):
        if not isinstance(arg, type(self)):
            raise TypeError('%s must be melodic chromatic interval.' % arg)
        if not self.direction_number == arg.direction_number:
            raise ValueError(
                'can only compare melodic intervals of same direction.')
        return abs(self.number) <= abs(arg.number)

    def __lt__(self, arg):
        if not isinstance(arg, type(self)):
            raise TypeError('%s must be melodic chromatic interval.' % arg)
        if not self.direction_number == arg.direction_number:
            raise ValueError(
                'can only compare melodic intervals of same direction.')
        return abs(self.number) < abs(arg.number)

    def __neg__(self):
        return type(self)(-self._number)

    def __repr__(self):
        return '%s(%s)' % (self._class_name, self._format_string)

    def __str__(self):
        return self._format_string

    ### PRIVATE PROPERTIES ###

    @property
    def _format_string(self):
        return '%s%s' % (self._direction_symbol, abs(self.number))

    ### PUBLIC METHODS ###

    @classmethod
    def from_pitch_carriers(cls, pitch_carrier_1, pitch_carrier_2):
        '''Calculate melodic chromatic interval from `pitch_carrier_1` to
        `pitch_carrier_2`:

        ::

            >>> pitchtools.MelodicChromaticInterval.from_pitch_carriers(
            ...     pitchtools.NamedChromaticPitch(-2), 
            ...     pitchtools.NamedChromaticPitch(12),
            ...     )
            MelodicChromaticInterval(+14)

        Return melodic chromatic interval.
        '''
        from abjad.tools import pitchtools
        # get pitches
        pitch_1 = pitchtools.get_named_chromatic_pitch_from_pitch_carrier(
            pitch_carrier_1)
        pitch_2 = pitchtools.get_named_chromatic_pitch_from_pitch_carrier(
            pitch_carrier_2)
        # get difference in semitones
        number = abs(pitch_2.numbered_chromatic_pitch) - \
            abs(pitch_1.numbered_chromatic_pitch)
        # change 1.0, 2.0, ... into 1, 2, ...
        number = mathtools.integer_equivalent_number_to_integer(number)
        # make melodic chromatic interval
        mci = pitchtools.MelodicChromaticInterval(number)
        # return melodic chromatic interval
        return mci

    ### PUBLIC PROPERTIES ###

    @property
    def chromatic_interval_number(self):
        r'''Chromatic interval number:

        ::

            >>> mci.chromatic_interval_number
            -14

        Return integer or float.
        '''
        return self._number

    @property
    def direction_number(self):
        r'''Numeric sign:

        ::

            >>> mci.direction_number
            -1

        Return integer.
        '''
        return mathtools.sign(self.number)

    @property
    def harmonic_chromatic_interval(self):
        r'''Harmonic chromatic interval:

        ::

            >>> mci.harmonic_chromatic_interval
            HarmonicChromaticInterval(14)

        Return harmonic chromatic interval.
        '''
        from abjad.tools import pitchtools
        number = abs(self.number)
        return pitchtools.HarmonicChromaticInterval(number)

    @property
    def melodic_chromatic_interval_class(self):
        r'''Melodic chromatic interval-class:

        ::

            >>> mci.melodic_chromatic_interval_class
            MelodicChromaticIntervalClass(-2)

        Return melodic chromatic interval-class.
        '''
        from abjad.tools import pitchtools
        return pitchtools.MelodicChromaticIntervalClass(self)
