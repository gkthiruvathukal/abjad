from abjad import *
from abjad.tools import sequencetools


def test_seqtools_Matrix___init___01():
    r'''Init from rows.
    '''

    matrix = sequencetools.Matrix(((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23)))

    assert matrix.rows == ((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23))
    assert matrix.columns == ((0, 10, 20), (1, 11, 21), (2, 12, 22), (3, 13, 23))


def test_seqtools_Matrix___init___02():
    r'''Init from columns.
    '''

    matrix = sequencetools.Matrix(columns=((0, 10, 20), (1, 11, 21), (2, 12, 22), (3, 13, 23)))

    assert matrix.rows == ((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23))
    assert matrix.columns == ((0, 10, 20), (1, 11, 21), (2, 12, 22), (3, 13, 23))
