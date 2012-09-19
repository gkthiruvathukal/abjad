def iterate_tie_chains_backward_in_expr(expr):
    r'''Deprecated. Use `tietools.iterate_tie_chains_in_expr` instead.

    Iterate tie chains backward in `expr`::

        >>> staff = Staff(r"c'4 ~ \times 2/3 { c'16 d'8 } e'8 f'4 ~ f'16")

    ::

        >>> f(staff)
        \new Staff {
            c'4 ~
            \times 2/3 {
                c'16
                d'8
            }
            e'8
            f'4 ~
            f'16
        }

    ::

        >>> for x in tietools.iterate_tie_chains_backward_in_expr(staff):
        ...     x
        ...
        TieChain((Note("f'4"), Note("f'16")))
        TieChain((Note("e'8"),))
        TieChain((Note("d'8"),))
        TieChain((Note("c'4"), Note("c'16")))

    Return generator.
    '''
    from abjad.tools import tietools

    return tietools.iterate_tie_chains_in_expr(expr, reverse=True)
