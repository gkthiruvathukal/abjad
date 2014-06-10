# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_UserInputGetter_go_home_01():

    score_manager = scoremanager.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score m tempo~inventory oae 1 d h q'
    score_manager._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Red Example Score (2013) - materials - tempo inventory (OAE)',
        'Red Example Score (2013) - materials - tempo inventory (EDIT)',
        'Red Example Score (2013) - materials - tempo inventory (EDIT)',
        'Abjad IDE - scores',
        ]
    assert score_manager._transcript.titles == titles