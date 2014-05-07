# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_Session_is_navigating_to_stylesheet_library_01():
    r'''From build directory to stylesheet library directory.
    '''

    input_ = 'u y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - build files',
        'Score manager - stylesheets',
        ]
    assert score_manager._transcript.titles == titles


def test_Session_is_navigating_to_stylesheet_library_02():
    r'''From distribution directory to stylesheet library directory.
    '''

    input_ = 'd y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - distribution files',
        'Score manager - stylesheets',
        ]
    assert score_manager._transcript.titles == titles


def test_Session_is_navigating_to_stylesheet_library_03():
    r'''From makers directory to stylesheet library directory.
    '''

    input_ = 'k y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - maker modules',
        'Score manager - stylesheets',
        ]
    assert score_manager._transcript.titles == titles


def test_Session_is_navigating_to_stylesheet_library_04():
    r'''From materials directory to stylesheet library directory.
    '''

    input_ = 'm y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - materials',
        'Score manager - stylesheets',
        ]
    assert score_manager._transcript.titles == titles


def test_Session_is_navigating_to_stylesheet_library_05():
    r'''From segments directory to stylesheet library directory.
    '''

    input_ = 'g y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - segments',
        'Score manager - stylesheets',
        ]
    assert score_manager._transcript.titles == titles


def test_Session_is_navigating_to_stylesheet_library_06():
    r'''From stylesheet library directory to stylesheet library directory.
    '''

    input_ = 'y y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - stylesheets',
        'Score manager - stylesheets',
        ]
    assert score_manager._transcript.titles == titles