from abjad.helpers.get_dominant_spanners_between import \
   get_dominant_spanners_between
from abjad.helpers.get_dominant_spanners import get_dominant_spanners


def get_dominant_spanners_slice(container, start, stop):
   '''Return Python list of (spanner, index) pairs.
      Each spanner dominates the components specified by slice 
      with start index 'start' and stop index 'stop'.
      Generalization of dominant spanner-finding functions for slices.
      This exists for slices like t[2:2] that are empty lists.'''

   from abjad.container.container import Container
   if not isinstance(container, Container):
      raise TypeError('Must be Abjad container.')

   if start == stop:
      if start == 0:
         left = None
      else:
         left = container[start - 1]
      if len(container) <= stop:
         right = None
      else:
         right = container[stop]
      spanners_receipt = get_dominant_spanners_between(left, right)
   else:
      spanners_receipt = get_dominant_spanners(
         container[start:stop])

   return spanners_receipt
