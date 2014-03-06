# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager


def test_TempoInventoryMaterialManager_01():

    score_manager = scoremanager.core.ScoreManager()
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.abjad_material_packages_directory_path,
        'testtempoinventory',
        )
    assert not os.path.exists(path)
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'output_material.py', 
        ]
    inventory = indicatortools.TempoInventory([
        ((1, 4), 60), 
        ((1, 4), 90),
        ])
    input_ = 'lmm nmm tempo testtempoinventory default testtempoinventory omi'
    input_ += ' add ((1, 4), 60) add ((1, 4), 90) b default q'

    try:
        score_manager._run(pending_user_input=input_, is_test=True)
        manager = scoremanager.managers.TempoInventoryMaterialManager(
            path=path)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_material_module()
        assert output_material == inventory
    finally:
        input_ = 'lmm testtempoinventory rm remove q'
        score_manager._run(pending_user_input=input_, is_test=True)
        assert not os.path.exists(path)