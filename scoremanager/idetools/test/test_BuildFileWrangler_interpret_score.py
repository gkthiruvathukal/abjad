# -*- encoding: utf-8 -*-
import filecmp
import os
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_BuildFileWrangler_interpret_score_01():
    r'''Works when score already exists.
    '''

    source_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'build',
        'score.tex',
        )
    path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'build',
        'score.pdf',
        )

    with systemtools.FilesystemState(keep=[source_path, path]):
        assert filecmp.cmp(path, path + '.backup')
        os.remove(path)
        assert not os.path.exists(path)
        input_ = 'red~example~score u si q'
        ide._run(input_=input_)
        assert os.path.isfile(path)
        # TODO: make this work
        #assert systemtools.TestManager.compare_pdfs(path, path + '.backup')