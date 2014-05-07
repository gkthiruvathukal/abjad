# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_MenuSection__make_menu_lines_01():
    r'''Include one-line summary of tempo.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    input_ = 'red~example~score m tempo~inventory q'
    score_manager._run(pending_input=input_)

    string = '  * 8=72'
    assert string in score_manager._transcript.contents