# -*- encoding: utf-8 -*-
from abjad.tools import componenttools


def withdraw_components_from_spanners_covered_by_components(components):
    r'''Find every spanner covered by 'components'.
    Withdraw all components in 'components' from covered spanners.
    Return 'components'.
    The operation always leaves all score trees in tact.

    Return components.
    '''
    from abjad.tools import spannertools

    # check components
    assert componenttools.all_are_contiguous_components_in_same_logical_voice(components)

    # withdraw from covered spanners
    for spanner in spannertools.get_spanners_covered_by_components(components):
        spanner.detach()

    # return components
    return components
