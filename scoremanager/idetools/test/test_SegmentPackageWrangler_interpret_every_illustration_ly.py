# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageWrangler_interpret_every_illustration_ly_01():
    r'''Does not display candidate messages.
    '''

    path = ide._configuration.example_score_packages_directory
    path = os.path.join(path, 'red_example_score', 'segments')
    package_names = (
        'segment_01',
        'segment_02',
        'segment_03',
        )
    ly_paths = [
        os.path.join(path, _, 'illustration.ly') 
        for _ in package_names
        ]
    pdf_paths = [_.replace('.ly', '.pdf') for _ in ly_paths]
    paths = ly_paths + pdf_paths

    with systemtools.FilesystemState(keep=paths):
        for path in pdf_paths:
            os.remove(path)
        assert not any(os.path.exists(_) for _ in pdf_paths)
        input_ = 'red~example~score g ii* y q'
        ide._run(input_=input_)
        assert all(os.path.isfile(_) for _ in pdf_paths)
        # TODO: reinterpret illustration.ly files and this should work
        #for pdf_path in pdf_paths:
        #    assert systemtools.TestManager.compare_pdfs(
        #        pdf_path, 
        #        pdf_path + '.backup',
        #        )

    contents = ide._transcript.contents
    for path in paths:
        assert path in contents

    assert 'Will interpret ...' in contents
    assert 'INPUT:' in contents
    assert 'OUTPUT:' in contents
    assert not 'The PDFs ...' in contents
    assert not '... compare the same.' in contents
    assert not 'Preserved' in contents


def test_SegmentPackageWrangler_interpret_every_illustration_ly_02():
    r'''Does display candidate messages.
    '''

    path = ide._configuration.example_score_packages_directory
    path = os.path.join(path, 'red_example_score', 'segments')
    package_names = (
        'segment_01',
        'segment_02',
        'segment_03',
        )
    ly_paths = [
        os.path.join(path, _, 'illustration.ly') for _ in package_names]
    pdf_paths = [_.replace('.ly', '.pdf') for _ in ly_paths]
    paths = ly_paths + pdf_paths

    with systemtools.FilesystemState(keep=paths):
        input_ = 'red~example~score g ii* y q'
        ide._run(input_=input_)

    contents = ide._transcript.contents
    for path in paths:
        assert path in contents

    assert 'Will interpret ...' in contents
    assert 'INPUT:' in contents
    assert 'OUTPUT:' in contents
    assert 'The PDFs ...' in contents
    assert '... compare the same.' in contents
    assert 'Preserved' in contents