# -*- encoding: utf-8 -*-
#import pytest
#pytest.skip('make me work')
from abjad import *
import scoremanager

# is_test=True is ok when testing the creation of views
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_SegmentPackageWrangler_make_view_01():
    r'''Makes sure view creation menu title is correct.
    '''

    input_ = 'g vnew _test q' 
    score_manager._run(pending_input=input_)
    transcript = score_manager._transcript

    string = 'Score manager - segments - views - _test - edit:'
    assert transcript.last_title == string


def test_SegmentPackageWrangler_make_view_02():
    r'''Makes sure at least one Abjad stylesheet appears in 
    view creation menu.
    '''

    input_ = 'g vnew _test q' 
    score_manager._run(pending_input=input_)
    transcript = score_manager._transcript

    string = 'segment 01 (Red Example Score)'
    assert string in transcript.contents


def test_SegmentPackageWrangler_make_view_03():
    r'''In score package.

    Makes sure segment packages are not annotated with score title.
    '''

    input_ = 'red~example~score g vnew _test q' 
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents

    string = 'segment 01'
    assert string in contents

    string = 'segment 01 (Red Example Score)'
    assert string not in contents


def test_SegmentPackageWrangler_make_view_04():
    r'''Makes view. Removes view.

    Makes sure no extra new lines appear before or after 
    'written to disk' message.
    '''

    input_ = 'g vnew _test rm all'
    input_ += ' add segment~01~(Red~Example~Score) done default q' 
    score_manager._run(pending_input=input_)

    lines =['> done', '']
    assert score_manager._transcript[-5].lines == lines

    lines = ['View inventory written to disk.', '']
    assert score_manager._transcript[-4].lines == lines
        
    input_ = 'g vls vrm _test default q'
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents
    assert 'view found' in contents or 'views found' in contents
    assert '_test' in contents

    input_ = 'y vls q'
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents
    assert 'view found' in contents or 'views found' in contents
    assert '_test' not in contents