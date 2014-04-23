# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MakerModuleWrangler_pytest_01():
    r'''Works on all test files in all maker module directories.
    '''

    input_ = 'k pyt q'
    score_manager._run(pending_user_input=input_)
    transcript_contents = score_manager._transcript.contents

    strings = [
        'Running py.test ...',
        'testable assets found',
        ]

    for string in strings:
        assert string in transcript_contents


def test_MakerModuleWrangler_pytest_02():
    r'''Works on all test files in a single maker module directory.
    '''

    input_ = 'red~example~score k pyt q'
    score_manager._run(pending_user_input=input_)
    transcript_contents = score_manager._transcript.contents

    strings = [
        'Running py.test ...',
        'testable assets found',
        ]

    for string in strings:
        assert string in transcript_contents