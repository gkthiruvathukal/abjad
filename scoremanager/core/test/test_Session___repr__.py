# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_Session___repr___01():

    session = scoremanager.core.Session(pending_input='foo')
    string = "Session(initial_pending_input='foo',"
    string += " pending_input='foo')"
    assert repr(session) == string