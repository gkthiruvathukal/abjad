from abjad.core import Rational
from abjad.components.Tuplet._TupletDurationInterface import _TupletDurationInterface


class _FixedMultiplierTupletDurationInterface(_TupletDurationInterface):

#   def __init__(self, _client, multiplier):
#      _TupletDurationInterface.__init__(self, _client)
#      self.multiplier = multiplier
#
#   ## PRIVATE ATTRIBUTES ##
#
#   @property
#   def _duration(self):
#      if 0 < len(self._client):
#         return self.multiplier * self.contents
#      else:
#         return Rational(0)
#
#   ## PUBLIC ATTRIBUTES ##
#
#   @property
#   def multiplied(self):
#      return self.multiplier * self.contents
#
#   @apply
#   def multiplier( ):
#      def fget(self):
#         return self._multiplier
#      def fset(self, expr):
#         if isinstance(expr, (int, long)):
#            rational = Rational(expr)
#         elif isinstance(expr, tuple):
#            rational = Rational(*expr)
#         elif isinstance(expr, Rational):
#            rational = Rational(expr)
#         else:
#            raise ValueError('Can not set tuplet rational from %s.' % 
#               str(expr))
#         if 0 < rational:
#            self._multiplier = rational
#         else:
#            raise ValueError('Tuplet rational %s must be positive.' %
#               rational)
#      return property(**locals( ))

   pass
