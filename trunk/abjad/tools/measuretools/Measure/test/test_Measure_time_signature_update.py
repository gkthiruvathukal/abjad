from abjad import *


def test_Measure_time_signature_update_01():
    r'''Measures allow time signature update.
    '''

    t = Measure((4, 8), "c'8 d'8 e'8 f'8")

    r'''
    {
        \time 4/8
        c'8
        d'8
        e'8
        f'8
    }
    '''

    t.pop()
    t.select().detach_marks(contexttools.TimeSignatureMark)
    contexttools.TimeSignatureMark((3, 8))(t)

    r'''
    {
        \time 3/8
        c'8
        d'8
        e'8
    }
    '''

    assert t.lilypond_format == "{\n\t\\time 3/8\n\tc'8\n\td'8\n\te'8\n}"
