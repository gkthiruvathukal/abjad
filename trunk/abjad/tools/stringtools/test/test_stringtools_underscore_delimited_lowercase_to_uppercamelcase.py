from abjad import *


def test_stringtools_underscore_delimited_lowercase_to_uppercamelcase_01( ):

   assert stringtools.underscore_delimited_lowercase_to_uppercamelcase('foo_bar_blah') == 'FooBarBlah'
