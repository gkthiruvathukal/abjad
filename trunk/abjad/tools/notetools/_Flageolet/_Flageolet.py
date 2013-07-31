import abc
from abjad.tools.abctools.AbjadObject import AbjadObject


class _Flageolet(AbjadObject):
    r'''Abjad model of both natural and artificial harmonics.
    Abstract base class.
    '''

    __metaclass__ = abc.ABCMeta
    __slots__ = ()

    ### PUBLIC PROPERTIES ###

    @property
    def suono_reale(self):
        r'''Actual sound of the harmonic when played.
        '''
        raise Exception('Not Implemented')
