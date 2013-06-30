from abjad.tools.documentationtools.ReSTDirective import ReSTDirective


class ReSTOnlyDirective(ReSTDirective):
    '''An ReST `only` directive:

    ::

        >>> only = documentationtools.ReSTOnlyDirective(argument='latex')

    ::

        >>> heading = documentationtools.ReSTHeading(
        ...     level=3, text='A LaTeX-Only Heading')
        >>> only.append(heading)
        >>> only
        ReSTOnlyDirective(
            argument='latex',
            children=(
                ReSTHeading(
                    level=3,
                    text='A LaTeX-Only Heading'
                    ),
                )
            )

    ::

        >>> print only.rest_format
        .. only:: latex
        <BLANKLINE>
           A LaTeX-Only Heading
           --------------------

    Return `ReSTOnlyDirective` instance.
    '''

    ### INITIALIZER ###

    def __init__(self, argument=None, children=None, name=None):
        ReSTDirective.__init__(
            self, 
            argument=argument, 
            children=children, 
            name=name,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def directive(self):
        return 'only'
