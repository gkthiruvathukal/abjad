from abjad.tools import componenttools


def get_spanners_attached_to_any_improper_child_of_component(
    component, spanner_classes=None):
    r'''.. versionadded:: 2.0

    Get all spanners attached to any improper children of `component`:

    ::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> beam = beamtools.BeamSpanner(staff.leaves)
        >>> first_slur = spannertools.SlurSpanner(staff.leaves[:2])
        >>> second_slur = spannertools.SlurSpanner(staff.leaves[2:])
        >>> trill = spannertools.TrillSpanner(staff)

    ::

        >>> f(staff)
        \new Staff {
            c'8 [ ( \startTrillSpan
            d'8 )
            e'8 (
            f'8 ] ) \stopTrillSpan
        }

    ::

        >>> len(
        ...     spannertools.get_spanners_attached_to_any_improper_child_of_component(
        ...     staff))
        4

    Get all spanners of `klass` attached to any proper children 
    of `component`:

    ::

        >>> spanner_classes = (spannertools.SlurSpanner, )
        >>> result = \
        ...     spannertools.get_spanners_attached_to_any_proper_child_of_component(
        ...     staff, spanner_classes=spanner_classes)

    ::

        >>> list(sorted(result))
        [SlurSpanner(c'8, d'8), SlurSpanner(e'8, f'8)]

    Get all spanners of any `klass` attached to any proper children 
    of `component`:

    ::

        >>> spanner_classes = (spannertools.SlurSpanner, beamtools.BeamSpanner)
        >>> result = \
        ...     spannertools.get_spanners_attached_to_any_proper_child_of_component(
        ...     staff, spanner_classes=spanner_classes)

    ::

        >>> for spanner in list(sorted(result)):
        ...     spanner
        BeamSpanner(c'8, d'8, e'8, f'8)
        SlurSpanner(c'8, d'8)
        SlurSpanner(e'8, f'8)

    Return unordered set of zero or more spanners.
    '''
    from abjad.tools import iterationtools
    from abjad.tools import spannertools

    # check input
    spanner_classes = spanner_classes or (spannertools.Spanner, )
    if not isinstance(spanner_classes, tuple):
        spanner_classes = (spanner_classes, )
    assert isinstance(spanner_classes, tuple)

    # initialize result set
    result = set([])

    # iterate children
    for child in iterationtools.iterate_components_in_expr([component]):
        result.update(spannertools.get_spanners_attached_to_component(
            child, spanner_classes=spanner_classes))

    # return result
    return result
