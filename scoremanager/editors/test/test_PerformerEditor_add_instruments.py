# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_PerformerEditor_add_instruments_01():
    r'''Quit, back, home, score & junk all work.
    '''

    score_manager = scoremanager.core.ScoreManager()
    string = 'red~example~score setup instrumentation hornist add q'
    score_manager._run(pending_user_input=string, is_test=True)
    assert score_manager._transcript.signature == (12,)

    string = 'red~example~score setup instrumentation hornist add b q'
    score_manager._run(pending_user_input=string, is_test=True)
    assert score_manager._transcript.signature == (14, (8, 12))

    string = 'red~example~score setup instrumentation hornist add h q'
    score_manager._run(pending_user_input=string, is_test=True)
    assert score_manager._transcript.signature == (14, (0, 12))

    string = 'red~example~score setup instrumentation'
    string += ' hornist add s q'
    score_manager._run(pending_user_input=string, is_test=True)
    assert score_manager._transcript.signature == (14, (2, 12))

    string = 'red~example~score setup instrumentation hornist add foo q'
    score_manager._run(pending_user_input=string, is_test=True)
    assert score_manager._transcript.signature == (14, (10, 12))


def test_PerformerEditor_add_instruments_02():
    r'''Add two instruments.
    '''

    session = scoremanager.core.Session()
    editor = scoremanager.editors.PerformerEditor(session=session)
    editor._run(pending_user_input='add 1 add 2 q')
    assert editor.target == instrumenttools.Performer(
        instruments=[
            instrumenttools.Accordion(), 
            instrumenttools.AltoVoice(),
            ])


def test_PerformerEditor_add_instruments_03():
    r'''Range handling.
    '''

    session = scoremanager.core.Session()
    editor = scoremanager.editors.PerformerEditor(session=session)
    editor._run(pending_user_input='add 1-2 q')
    assert editor.target == instrumenttools.Performer(
        instruments=[
            instrumenttools.Accordion(), 
            instrumenttools.AltoVoice(),
            ])
