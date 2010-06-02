from abjad import *


def test_measuretools_apply_complex_beam_spanner_to_measure_01( ):

   measure = RigidMeasure((2, 8), construct.run(2))

   r'''
   {
        \time 2/8
        c'8
        c'8
   }
   '''

   measuretools.apply_complex_beam_spanner_to_measure(measure)


   r'''
   {
        \time 2/8
        \set stemLeftBeamCount = #0
        \set stemRightBeamCount = #1
        c'8 [
        \set stemLeftBeamCount = #1
        \set stemRightBeamCount = #0
        c'8 ]
   }
   '''

   assert check.wf(measure)
   assert measure.format == "{\n\t\\time 2/8\n\t\\set stemLeftBeamCount = #0\n\t\\set stemRightBeamCount = #1\n\tc'8 [\n\t\\set stemLeftBeamCount = #1\n\t\\set stemRightBeamCount = #0\n\tc'8 ]\n}"
