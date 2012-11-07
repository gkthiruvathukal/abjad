from abjad import *
from abjad.tools import verticalitytools


def test_labeltools_label_vertical_moments_in_expr_with_interval_class_vectors_01():

    score = Score(Staff([]) * 3)
    notes = [Note("c'8"), Note("d'8"), Note("e'8"), Note("f'8")]
    score[0].extend(notes)
    contexttools.ClefMark('alto')(score[1])
    score[1].extend([Note(-5, (1, 4)), Note(-7, (1, 4))])
    contexttools.ClefMark('bass')(score[2])
    score[2].append(Note(-24, (1, 2)))
    labeltools.label_vertical_moments_in_expr_with_interval_class_vectors(score)

    r'''
    \new Score <<
        \new Staff {
            c'8
            d'8
                _ \markup {
                    \tiny
                        0010020
                    }
            e'8
            f'8
                _ \markup {
                    \tiny
                        1000020
                    }
        }
        \new Staff {
            \clef "alto"
            g4
            f4
                _ \markup {
                    \tiny
                        0100110
                    }
        }
        \new Staff {
            \clef "bass"
            c,2
                _ \markup {
                    \tiny
                        1000020
                    }
        }
    >>
    '''

    assert wellformednesstools.is_well_formed_component(score)
    assert score.lilypond_format == '\\new Score <<\n\t\\new Staff {\n\t\tc\'8\n\t\td\'8\n\t\t\t_ \\markup {\n\t\t\t\t\\tiny\n\t\t\t\t\t0010020\n\t\t\t\t}\n\t\te\'8\n\t\tf\'8\n\t\t\t_ \\markup {\n\t\t\t\t\\tiny\n\t\t\t\t\t1000020\n\t\t\t\t}\n\t}\n\t\\new Staff {\n\t\t\\clef "alto"\n\t\tg4\n\t\tf4\n\t\t\t_ \\markup {\n\t\t\t\t\\tiny\n\t\t\t\t\t0100110\n\t\t\t\t}\n\t}\n\t\\new Staff {\n\t\t\\clef "bass"\n\t\tc,2\n\t\t\t_ \\markup {\n\t\t\t\t\\tiny\n\t\t\t\t\t1000020\n\t\t\t\t}\n\t}\n>>'
 

def test_labeltools_label_vertical_moments_in_expr_with_interval_class_vectors_02():
    '''Vertical moments with quartertones format with a two-row
    interval-class vector. Top for 12-ET, bottom for 24-ET.'''

    chord = Chord([-2, -1.5, 9], (1, 4))
    labeltools.label_vertical_moments_in_expr_with_interval_class_vectors(chord)

    r'''
    <bf bqf a'>4
        _ \markup {
            \tiny
                \column
                    {
                        0100000
                        110000
                    }
            }
    '''

    assert chord.lilypond_format == "<bf bqf a'>4\n\t_ \\markup {\n\t\t\\tiny\n\t\t\t\\column\n\t\t\t\t{\n\t\t\t\t\t0100000\n\t\t\t\t\t110000\n\t\t\t\t}\n\t\t}"

 
