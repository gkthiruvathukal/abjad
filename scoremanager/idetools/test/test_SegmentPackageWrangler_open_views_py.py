# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageWrangler_open_views_py_01():

    input_ = 'G we q'
    ide._run(input_=input_)

    assert ide._session._attempted_to_open_file