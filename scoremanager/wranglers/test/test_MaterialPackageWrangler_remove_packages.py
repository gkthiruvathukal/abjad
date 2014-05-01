# -*- encoding: utf-8 -*-
import os
import shutil
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MaterialPackageWrangler_remove_packages_01():

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory_path,
        'red_example_score',
        'materials',
        'instrumentation',
        )
    backup_path = path + '.backup'

    assert os.path.exists(path)
    assert not os.path.exists(backup_path)
    shutil.copytree(path, backup_path)
    assert os.path.exists(backup_path)

    input_ = 'red~example~score m rm instrumentation remove q'
    score_manager._run(pending_user_input=input_)
    assert not os.path.exists(path)
    assert os.path.exists(backup_path)
    shutil.move(backup_path, path)
    manager = scoremanager.managers.DirectoryManager(
        path=path,
        session=score_manager._session,
        )
    manager.add_to_repository(prompt=False)

    assert os.path.exists(path)
    assert not os.path.exists(backup_path)