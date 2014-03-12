# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_TempoEditor__run_01():

    session = scoremanager.core.Session()
    editor = scoremanager.editors.TempoEditor(session=session)
    editor._run(pending_user_input='q')
    assert editor.target == Tempo()


def test_TempoEditor__run_02():

    session = scoremanager.core.Session()
    editor = scoremanager.editors.TempoEditor(session=session)
    editor._run(pending_user_input='duration (1, 8) units 98 q')
    assert editor.target == indicatortools.Tempo(Duration(1, 8), 98)


def test_TempoEditor__run_03():

    session = scoremanager.core.Session()
    editor = scoremanager.editors.TempoEditor(session=session)
    editor._run(pending_user_input='duration Duration(1, 8) units 98 q')
    assert editor.target == indicatortools.Tempo(Duration(1, 8), 98)
