from abjad.component.component import _Component
from abjad.helpers.test_components import _test_components
from abjad import *


def test_test_components_none_score_01( ):
   '''All components here in the same score.'''
   
   t = Voice(Sequential(run(2)) * 2)
   diatonicize(t)

   r'''\new Voice {
      {
         c'8
         d'8
      }
      {
         e'8
         f'8
      }
   }'''

   assert _test_components([t], share = 'score')
   assert _test_components(t[:], share = 'score')
   assert _test_components(t.leaves[:2], share = 'score')
   assert _test_components(t.leaves[2:], share = 'score')
   assert _test_components(t.leaves, share = 'score')
   assert _test_components(list(iterate(t, _Component)), share = 'score')


def test_test_components_none_score_02( ):
   '''Components here divide between two different scores.'''

   t1 = Voice(scale(4))
   t2 = Voice(scale(4))

   assert _test_components([t1], share = 'score')
   assert _test_components(t1.leaves, share = 'score')
   assert _test_components([t2], share = 'score')
   assert _test_components(t2.leaves, share = 'score')

   assert _test_components([t1, t2], share = 'score')
   assert not _test_components([t1, t2], share = 'score', 
      allow_orphans = False)

   assert not _test_components(t1.leaves + t2.leaves, share = 'score')


def test_test_components_none_score_03( ):
   '''Unincorporated component returns True.'''

   assert _test_components([Note(0, (1, 8))], share = 'score')


def test_test_components_none_score_04( ):
   '''Empty list returns True.'''

   assert _test_components([ ], share = 'score')
