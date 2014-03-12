# -*- encoding: utf-8 -*-
import pytest
from abjad import *
import scoremanager


def test_TargetManifest_change_initializer_argument_name_to_retrievable_attribute_name_01():

    session = scoremanager.core.Session()
    editor = scoremanager.editors.MarkupEditor(session=session)

    assert editor.target_manifest.change_initializer_argument_name_to_retrievable_attribute_name('arg') == \
        'contents_string'

    assert editor.target_manifest.change_initializer_argument_name_to_retrievable_attribute_name('direction') == \
        'direction'


def test_TargetManifest_change_initializer_argument_name_to_retrievable_attribute_name_02():

    session = scoremanager.core.Session()
    editor = scoremanager.editors.MarkupEditor(session=session)

    statement = "editor.target_manifest.change_initializer_argument_name"
    statement += "_to_retrievable_attribute_name('asdfasdf')"
    assert pytest.raises(Exception, statement)
