from abjad import *
from abjad.tools import verticalitytools


def test_labeltools_label_vertical_moments_in_expr_with_numbered_chromatic_pitch_classes_01():

    score = Score(Staff([]) * 3)
    notes = [Note("c'8"), Note("d'8"), Note("e'8"), Note("f'8")]
    score[0].extend(notes)
    contexttools.ClefMark('alto')(score[1])
    score[1].extend([Note(-5, (1, 4)), Note(-7, (1, 4))])
    contexttools.ClefMark('bass')(score[2])
    score[2].append(Note(-24, (1, 2)))
    labeltools.label_vertical_moments_in_expr_with_numbered_chromatic_pitch_classes(score)

    r'''
    \new Score <<
        \new Staff {
            c'8
            d'8
                _ \markup {
                    \small
                        \column
                            {
                                7
                                2
                                0
                            }
                    }
            e'8
            f'8
                _ \markup {
                    \small
                        \column
                            {
                                5
                                0
                            }
                    }
        }
        \new Staff {
            \clef "alto"
            g4
            f4
                _ \markup {
                    \small
                        \column
                            {
                                5
                                4
                                0
                            }
                    }
        }
        \new Staff {
            \clef "bass"
            c,2
                _ \markup {
                    \small
                        \column
                            {
                                7
                                0
                            }
                    }
        }
    >>
    '''

    assert wellformednesstools.is_well_formed_component(score)
    assert score.lilypond_format == '\\new Score <<\n\t\\new Staff {\n\t\tc\'8\n\t\td\'8\n\t\t\t_ \\markup {\n\t\t\t\t\\small\n\t\t\t\t\t\\column\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t7\n\t\t\t\t\t\t\t2\n\t\t\t\t\t\t\t0\n\t\t\t\t\t\t}\n\t\t\t\t}\n\t\te\'8\n\t\tf\'8\n\t\t\t_ \\markup {\n\t\t\t\t\\small\n\t\t\t\t\t\\column\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t5\n\t\t\t\t\t\t\t0\n\t\t\t\t\t\t}\n\t\t\t\t}\n\t}\n\t\\new Staff {\n\t\t\\clef "alto"\n\t\tg4\n\t\tf4\n\t\t\t_ \\markup {\n\t\t\t\t\\small\n\t\t\t\t\t\\column\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t5\n\t\t\t\t\t\t\t4\n\t\t\t\t\t\t\t0\n\t\t\t\t\t\t}\n\t\t\t\t}\n\t}\n\t\\new Staff {\n\t\t\\clef "bass"\n\t\tc,2\n\t\t\t_ \\markup {\n\t\t\t\t\\small\n\t\t\t\t\t\\column\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t7\n\t\t\t\t\t\t\t0\n\t\t\t\t\t\t}\n\t\t\t\t}\n\t}\n>>'


