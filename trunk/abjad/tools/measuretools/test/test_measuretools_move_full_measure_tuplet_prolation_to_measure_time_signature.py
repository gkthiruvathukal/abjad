from abjad import *


def test_measuretools_move_full_measure_tuplet_prolation_to_measure_time_signature_01():
    r'''Move prolation of full-measure power-of-two tuplet to time signature.
    '''

    t = Measure((2, 8), [tuplettools.FixedDurationTuplet(Duration(2, 8), "c'8 d'8 e'8")])
    measuretools.move_full_measure_tuplet_prolation_to_measure_time_signature(t)

    r'''
    {
        \time 3/12
        \scaleDurations #'(2 . 3) {
            c'8
            d'8
            e'8
        }
    }
    '''

    assert select(t).is_well_formed()
    assert t.lilypond_format == "{\n\t\\time 3/12\n\t\\scaleDurations #'(2 . 3) {\n\t\tc'8\n\t\td'8\n\t\te'8\n\t}\n}"


def test_measuretools_move_full_measure_tuplet_prolation_to_measure_time_signature_02():
    r'''Move prolation of full-measure non-power-of-two tuplet to time signature.
    '''

    t = Measure((3, 16), [
        tuplettools.FixedDurationTuplet(Duration(3, 16), "c'16 d'16 e'16 f'16 g'16")])
    measuretools.move_full_measure_tuplet_prolation_to_measure_time_signature(t)

    r'''
    {
        \time 15/80
        \scaleDurations #'(4 . 5) {
            c'32.
            d'32.
            e'32.
            f'32.
            g'32.
        }
    }
    '''

    assert select(t).is_well_formed()
    assert t.lilypond_format == "{\n\t\\time 15/80\n\t\\scaleDurations #'(4 . 5) {\n\t\tc'32.\n\t\td'32.\n\t\te'32.\n\t\tf'32.\n\t\tg'32.\n\t}\n}"


def test_measuretools_move_full_measure_tuplet_prolation_to_measure_time_signature_03():
    r'''Subsume 7:6 tuplet.
    '''

    t = Measure((6, 8), [
        tuplettools.FixedDurationTuplet(Duration(6, 8), "c'8 d'8 e'8 f'8 g'8 a'8 b'8")])
    measuretools.move_full_measure_tuplet_prolation_to_measure_time_signature(t)

    r'''
    {
        \time 21/28
        \scaleDurations #'(4 . 7) {
            c'8.
            d'8.
            e'8.
            f'8.
            g'8.
            a'8.
            b'8.
        }
    }
    '''

    assert select(t).is_well_formed()
    assert t.lilypond_format == "{\n\t\\time 21/28\n\t\\scaleDurations #'(4 . 7) {\n\t\tc'8.\n\t\td'8.\n\t\te'8.\n\t\tf'8.\n\t\tg'8.\n\t\ta'8.\n\t\tb'8.\n\t}\n}"


def test_measuretools_move_full_measure_tuplet_prolation_to_measure_time_signature_04():
    r'''Subsume tuplet in nonassignable measure.
    '''

    t = Measure((5, 8), [
        tuplettools.FixedDurationTuplet(Duration(5, 8), "c'8 d'8 e'8 f'8 g'8 a'8")])
    measuretools.move_full_measure_tuplet_prolation_to_measure_time_signature(t)

    r'''
    {
        \time 15/24
        \scaleDurations #'(2 . 3) {
            c'8 ~
            c'32
            d'8 ~
            d'32
            e'8 ~
            e'32
            f'8 ~
            f'32
            g'8 ~
            g'32
            a'8 ~
            a'32
        }
    }
    '''

    assert select(t).is_well_formed()
    assert t.lilypond_format == "{\n\t\\time 15/24\n\t\\scaleDurations #'(2 . 3) {\n\t\tc'8 ~\n\t\tc'32\n\t\td'8 ~\n\t\td'32\n\t\te'8 ~\n\t\te'32\n\t\tf'8 ~\n\t\tf'32\n\t\tg'8 ~\n\t\tg'32\n\t\ta'8 ~\n\t\ta'32\n\t}\n}"



def test_measuretools_move_full_measure_tuplet_prolation_to_measure_time_signature_05():
    r'''Subsume nested tuplet.
    '''

    inner = tuplettools.FixedDurationTuplet(Duration(2, 16), notetools.make_repeated_notes(3, Duration(1, 16)))
    notes = notetools.make_repeated_notes(2)
    outer = tuplettools.FixedDurationTuplet(Duration(2, 8), [inner] + notes)
    t = Measure((2, 8), [outer])
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)

    r'''
    {
        \time 2/8
        \times 2/3 {
            \times 2/3 {
                c'16
                d'16
                e'16
            }
            f'8
            g'8
        }
    }
    '''

    measuretools.move_full_measure_tuplet_prolation_to_measure_time_signature(t)

    r'''
    {
        \time 3/12
        \scaleDurations #'(2 . 3) {
            \times 2/3 {
                c'16
                d'16
                e'16
            }
            f'8
            g'8
        }
    }
    '''

    assert select(t).is_well_formed()
    assert t.lilypond_format == "{\n\t\\time 3/12\n\t\\scaleDurations #'(2 . 3) {\n\t\t\\times 2/3 {\n\t\t\tc'16\n\t\t\td'16\n\t\t\te'16\n\t\t}\n\t\tf'8\n\t\tg'8\n\t}\n}"


def test_measuretools_move_full_measure_tuplet_prolation_to_measure_time_signature_06():
    r'''Submsume 6:5. Time signature should go from 5/16 to 15/48.
    '''

    tuplet = tuplettools.FixedDurationTuplet(Duration(5, 16), "c'8 d'8 e'8")
    t = Measure((5, 16), [tuplet])

    r'''
    {
        \time 5/16
        \tweak #'text #tuplet-number::calc-fraction-text
        \times 5/6 {
            c'8
            d'8
            e'8
        }
    }
    '''

    measuretools.move_full_measure_tuplet_prolation_to_measure_time_signature(t)

    r'''
    {
        \time 15/48
        \scaleDurations #'(2 . 3) {
            c'8 ~
            c'32
            d'8 ~
            d'32
            e'8 ~
            e'32
        }
    }
    '''

    assert select(t).is_well_formed()
    assert t.lilypond_format == "{\n\t\\time 15/48\n\t\\scaleDurations #'(2 . 3) {\n\t\tc'8 ~\n\t\tc'32\n\t\td'8 ~\n\t\td'32\n\t\te'8 ~\n\t\te'32\n\t}\n}"
