from abjad import *


def test_marktools_attach_annotation_to_components_in_expr_01():

    staff = Staff("c'8 d'8 e'8 f'8")
    annotation = marktools.Annotation('foo', 'bar')
    marktools.attach_annotations_to_components_in_expr(staff.select_leaves(), [annotation])

    for leaf in staff.select_leaves():
        new_annotation = leaf.get_marks(marktools.Annotation)[0]
        assert new_annotation == annotation
        assert new_annotation is not annotation
