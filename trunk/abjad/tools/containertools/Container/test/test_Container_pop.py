from abjad import *


def test_Container_pop_01():
    r'''Containers pop leaves correctly.
        Popped leaves detach from parent.
        Popped leaves withdraw from crossing spanners.
        Popped leaves carry covered spanners forward.'''

    t = Voice("c'8 d'8 e'8 f'8")
    spannertools.SlurSpanner(t[:])
    spannertools.BeamSpanner(t[1])

    r'''
    \new Voice {
        c'8 (
        d'8 [ ]
        e'8
        f'8 )
    }
    '''

    result = t.pop(1)

    r'''
    \new Voice {
        c'8 (
        e'8
        f'8 )
    }
    '''

    assert select(t).is_well_formed()
    assert t.lilypond_format == "\\new Voice {\n\tc'8 (\n\te'8\n\tf'8 )\n}"

    "Result is now d'8 [ ]"

    assert select(result).is_well_formed()
    assert result.lilypond_format == "d'8 [ ]"


def test_Container_pop_02():
    r'''Containers pop nested containers correctly.
        Popped containers detach from both parent and spanners.'''

    t = Staff(Container(notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    p = spannertools.BeamSpanner(t[:])

    r'''
    \new Staff {
        {
            c'8 [
            d'8
        }
        {
            e'8
            f'8 ]
        }
    }
    '''

    sequential = t.pop()

    r'''
    \new Staff {
        {
            c'8 [
            d'8 ]
        }
    }
    '''

    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\tc'8 [\n\t\td'8 ]\n\t}\n}"
    assert select(t).is_well_formed()

    r'''
    {
        e'8
        f'8
    }
    '''

    assert sequential.lilypond_format == "{\n\te'8\n\tf'8\n}"
    assert select(sequential).is_well_formed()
