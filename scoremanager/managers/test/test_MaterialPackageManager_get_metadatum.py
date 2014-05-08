# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MaterialPackageManager_get_metadatum_01():

    # make sure no flavor metadatum found
    input_ = 'red~example~score m magic~numbers mdg flavor default q'
    score_manager._run(pending_input=input_)
    assert score_manager._transcript.entries[-4].title == 'None'

    # add flavor metadatum
    input_ = 'red~example~score m magic~numbers mda flavor cherry q'
    score_manager._run(pending_input=input_)

    # maker sure flavor metadatum now equal to 'cherry'
    input_ = 'red~example~score m magic~numbers mdg flavor default q'
    score_manager._run(pending_input=input_)
    assert score_manager._transcript.entries[-4].title == "'cherry'"

    # remove flavor metadatum
    input_ = 'red~example~score m magic~numbers mdrm flavor default q'
    score_manager._run(pending_input=input_)

    # make sure no flavor metadatum found
    input_ = 'red~example~score m magic~numbers mdg flavor default q'
    score_manager._run(pending_input=input_)
    assert score_manager._transcript.entries[-4].title == 'None'