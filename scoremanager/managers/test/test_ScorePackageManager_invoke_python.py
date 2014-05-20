# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_ScorePackageManager_invoke_python_01():
    
    input_ = 'red~example~score pyi 2**38 q'
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents

    assert '274877906944' in contents