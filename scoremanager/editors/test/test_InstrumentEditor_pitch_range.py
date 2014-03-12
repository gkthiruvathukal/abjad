# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_InstrumentEditor_pitch_range_01():

    session = scoremanager.core.Session()
    editor = scoremanager.editors.InstrumentEditor(session=session)
    editor._run(pending_user_input='marimba q')
    assert editor.target.pitch_range == pitchtools.PitchRange(-19, 36)

    session = scoremanager.core.Session()
    editor = scoremanager.editors.InstrumentEditor(session=session)
    editor._run(pending_user_input='marimba rg [C2, C7] q')
    assert editor.target.pitch_range == pitchtools.PitchRange(-24, 36)
