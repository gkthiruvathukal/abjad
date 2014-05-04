# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_MaterialPackageManager_open_illustration_ly_01():

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    input_ = 'm example~notes lyo q'
    score_manager._run(pending_user_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - materials',
        'Score manager - materials - example notes (Abjad)',
        'Score manager - materials - example notes (Abjad)',
        ]

    assert score_manager._transcript.titles == titles
    assert score_manager._session._attempted_to_open_file