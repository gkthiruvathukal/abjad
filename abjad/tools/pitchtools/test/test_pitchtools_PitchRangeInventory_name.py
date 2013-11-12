# -*- encoding: utf-8 -*-
import pytest
from abjad import *


def test_pitchtools_PitchRangeinventory_custom_identifier_01():

    inventory = pitchtools.PitchRangeInventory(['[A0, C8]'])
    assert inventory.custom_identifier is None

    inventory.custom_identifier = 'blue inventory'
    assert inventory.custom_identifier == 'blue inventory'


def test_pitchtools_PitchRangeinventory_custom_identifier_02():

    inventory = pitchtools.PitchRangeInventory(['[A0, C8]'])
    assert pytest.raises(Exception, 'inventory.custom_identifier = 99')
