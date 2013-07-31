from abjad.tools.pitchtools.DiatonicPitch import DiatonicPitch


class NamedDiatonicPitch(DiatonicPitch):
    '''.. versionadded:: 2.0

    Abjad model of a named diatonic pitch:

    ::

        >>> pitch = pitchtools.NamedDiatonicPitch("c''")

    ::

        >>> pitch
        NamedDiatonicPitch("c''")

    ::

        >>> print pitch
        c''

    Named diatonic pitches are immutable.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_diatonic_pitch_name',
        )

    _default_positional_input_arguments = (
        repr("c''"),
        )

    ### INITIALIZER ###

    def __init__(self, arg):
        from abjad.tools import pitchtools
        if hasattr(arg, '_diatonic_pitch_name'):
            diatonic_pitch_name = arg._diatonic_pitch_name
        elif hasattr(arg, '_diatonic_pitch_number'):
            tmp = pitchtools.diatonic_pitch_number_to_diatonic_pitch_name
            diatonic_pitch_name = tmp(arg._diatonic_pitch_number)
        elif pitchtools.is_diatonic_pitch_name(arg):
            diatonic_pitch_name = arg
        elif pitchtools.is_diatonic_pitch_number(arg):
            diatonic_pitch_name = \
                pitchtools.diatonic_pitch_number_to_diatonic_pitch_name(arg)
        else:
            raise TypeError(
                'can not initialize named diatonic pitch: "%s".' % arg)
        tmp = pitchtools.diatonic_pitch_name_to_diatonic_pitch_number
        diatonic_pitch_number = tmp(diatonic_pitch_name)
        object.__setattr__(self, '_diatonic_pitch_name', diatonic_pitch_name)
        object.__setattr__(
            self, '_comparison_attribute', diatonic_pitch_number)
        object.__setattr__(self, '_format_string', repr(diatonic_pitch_name))

    ### SPECIAL METHODS ###

    def __abs__(self):
        return abs(self.numbered_diatonic_pitch)

    def __float__(self):
        return float(self.numbered_diatonic_pitch)

    def __int__(self):
        return int(self.numbered_diatonic_pitch)

    def __repr__(self):
        return '%s(%r)' % (self._class_name, str(self))

    def __str__(self):
        return self._diatonic_pitch_name

    ### PUBLIC PROPERTIES ###

    @property
    def chromatic_pitch_class_name(self):
        r'''Chromatic pitch-class name:

        ::

            >>> pitch.chromatic_pitch_class_name
            'c'

        Return string.
        '''
        from abjad.tools import pitchtools
        return pitchtools.diatonic_pitch_name_to_chromatic_pitch_class_name(
            self.diatonic_pitch_name)

    @property
    def chromatic_pitch_class_number(self):
        r'''Chromatic pitch-class number:

        ::

            >>> pitch.chromatic_pitch_class_number
            0

        Return integer.
        '''
        from abjad.tools import pitchtools
        return pitchtools.diatonic_pitch_name_to_chromatic_pitch_class_number(
            self.diatonic_pitch_name)

    @property
    def chromatic_pitch_name(self):
        r'''Chromatic pitch name:

        ::

            >>> pitch.chromatic_pitch_name
            "c''"

        Return string.
        '''
        from abjad.tools import pitchtools
        return pitchtools.diatonic_pitch_name_to_chromatic_pitch_name(
            self.diatonic_pitch_name)

    @property
    def chromatic_pitch_number(self):
        r'''Chromatic pitch number:

        ::

            >>> pitch.chromatic_pitch_number
            12

        Return integer.
        '''
        from abjad.tools import pitchtools
        return pitchtools.diatonic_pitch_name_to_chromatic_pitch_number(
            self.diatonic_pitch_name)

    @property
    def diatonic_pitch_class_name(self):
        r'''Diatonic pitch-class name:

        ::

            >>> pitch.diatonic_pitch_class_name
            'c'

        Return string.
        '''
        from abjad.tools import pitchtools
        return pitchtools.diatonic_pitch_name_to_diatonic_pitch_class_name(
            self.diatonic_pitch_name)

    @property
    def diatonic_pitch_class_number(self):
        r'''Diatonic pitch-class number:

        ::

            >>> pitch.diatonic_pitch_class_number
            0

        Return integer.
        '''
        from abjad.tools import pitchtools
        return pitchtools.diatonic_pitch_name_to_diatonic_pitch_class_number(
            self.diatonic_pitch_name)

    @property
    def diatonic_pitch_name(self):
        r'''Diatonic pitch name:

        ::

            >>> pitch.diatonic_pitch_name
            "c''"

        Return string.
        '''
        return self._diatonic_pitch_name

    @property
    def diatonic_pitch_number(self):
        r'''Diatonic pitch number:

        ::

            >>> pitch.diatonic_pitch_number
            7

        Return integer.
        '''
        from abjad.tools import pitchtools
        return pitchtools.diatonic_pitch_name_to_diatonic_pitch_number(
            self.diatonic_pitch_name)

    @property
    def lilypond_format(self):
        r'''LilyPond input format of named diatonic pitch:

        ::

            >>> pitch.lilypond_format
            "c''"

        Return string.
        '''
        return self._diatonic_pitch_name

    @property
    def named_chromatic_pitch(self):
        r'''Named chromatic pitch:

        ::

            >>> pitch.named_chromatic_pitch
            NamedChromaticPitch("c''")

        Return named chromatic pitch.
        '''
        from abjad.tools import pitchtools
        return pitchtools.NamedChromaticPitch(self.chromatic_pitch_name)

    @property
    def named_chromatic_pitch_class(self):
        r'''Named chromatic pitch-class:

        ::

            >>> pitch.named_chromatic_pitch_class
            NamedChromaticPitchClass('c')

        Return named chromatic pitch-class.
        '''
        from abjad.tools import pitchtools
        return pitchtools.NamedChromaticPitchClass(
            self.chromatic_pitch_class_name)

    @property
    def named_diatonic_pitch_class(self):
        r'''Named diatonic pitch-class:

        ::

            >>> pitch.named_diatonic_pitch_class
            NamedDiatonicPitchClass('c')

        Return named diatonic pitch-class.
        '''
        from abjad.tools import pitchtools
        tmp = pitchtools.diatonic_pitch_name_to_diatonic_pitch_class_name
        return pitchtools.NamedDiatonicPitchClass(
            tmp(self._diatonic_pitch_name))

    @property
    def numbered_chromatic_pitch(self):
        r'''Numbered chromatic pitch:

        ::

            >>> pitch.numbered_chromatic_pitch
            NumberedChromaticPitch(12)

        Return numbered chromatic pitch.
        '''
        from abjad.tools import pitchtools
        return pitchtools.NumberedChromaticPitch(self.chromatic_pitch_number)

    @property
    def numbered_chromatic_pitch_class(self):
        r'''Numbered chromatic pitch-class:

        ::

            >>> pitch.numbered_chromatic_pitch_class
            NumberedChromaticPitchClass(0)

        Return numbered chromatic pitch-class.
        '''
        from abjad.tools import pitchtools
        return pitchtools.NumberedChromaticPitchClass(
            self.chromatic_pitch_class_number)

    @property
    def numbered_diatonic_pitch(self):
        r'''Numbered diatonic pitch:

        ::

            >>> pitch.numbered_diatonic_pitch
            NumberedDiatonicPitch(7)

        Return numbered diatonic pitch.
        '''
        from abjad.tools import pitchtools
        tmp = pitchtools.diatonic_pitch_name_to_diatonic_pitch_number
        return pitchtools.NumberedDiatonicPitch(tmp(self._diatonic_pitch_name))

    @property
    def numbered_diatonic_pitch_class(self):
        r'''Numbered diatonic pitch-class:

        ::

            >>> pitch.numbered_diatonic_pitch_class
            NumberedDiatonicPitchClass(0)

        Return numbered diatonic pitch-class.
        '''
        from abjad.tools import pitchtools
        tmp = pitchtools.diatonic_pitch_name_to_diatonic_pitch_class_number
        return pitchtools.NumberedDiatonicPitchClass(
            tmp(self._diatonic_pitch_name))
