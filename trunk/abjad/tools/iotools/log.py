import os


def log():
    r'''Open the LilyPond log file in operating system-specific text editor:

    ::

        >>> iotools.log() # doctest: +SKIP

    ::

        GNU LilyPond 2.12.2
        Processing `0440.ly'
        Parsing...
        Interpreting music...
        Preprocessing graphical objects...
        Finding the ideal number of pages...
        Fitting music on 1 page...
        Drawing systems...
        Layout output to `0440.ps'...
        Converting to `./0440.pdf'...

    Exit text editor in the usual way.

    Return none.
    '''
    from abjad import abjad_configuration
    from abjad.tools import iotools

    ABJADOUTPUT = abjad_configuration['abjad_output']
    text_editor = abjad_configuration.get_text_editor()
    command = '{} {}'.format(text_editor, os.path.join(ABJADOUTPUT, 'lily.log'))
    # TODO: how do we get rid of this call to os.system()?
    #spawn_subprocess(command)
    os.system(command)
