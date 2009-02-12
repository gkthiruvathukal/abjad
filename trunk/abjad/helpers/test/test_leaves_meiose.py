from abjad import *


def test_leaves_meiose_01( ):
   '''Meiose each leaf in two.'''

   t = Voice(scale(3))
   Beam(t[:])
   leaves_meiose(t)

   r'''
   \new Voice {
      c'16 [
      c'16
      d'16
      d'16
      e'16
      e'16 ]
   }
   '''

   assert check(t)
   assert t.format == "\\new Voice {\n\tc'16 [\n\tc'16\n\td'16\n\td'16\n\te'16\n\te'16 ]\n}"


def test_leaves_meiose_02( ):
   '''Meiose one leaf in four.'''

   t = Voice(scale(3))
   Beam(t[:])
   leaves_meiose(t[0], 4)

   r'''
   \new Voice {
      c'32 [
      c'32
      c'32
      c'32
      d'8
      e'8 ]
   }
   '''

   assert check(t)
   assert t.format == "\\new Voice {\n\tc'32 [\n\tc'32\n\tc'32\n\tc'32\n\td'8\n\te'8 ]\n}"
