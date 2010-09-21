from abjad.components.Container import Container
from abjad.components.Tuplet._TupletDurationInterface import _TupletDurationInterface
from abjad.components.Tuplet._TupletFormatter import _TupletFormatter


class _Tuplet(Container):
   '''Abjad tuplet formalization.
   '''

   #def __init__(self, music = None):
   def __init__(self, multiplier, music = None):
      Container.__init__(self, music)
      self._duration = _TupletDurationInterface(self, multiplier)
      self._force_fraction = None
      self._formatter = _TupletFormatter(self) 
      self._is_invisible = None

   ## OVERLOADS ##

   def __add__(self, arg):
      '''Add two tuplets of same type and with same multiplier.'''
      from abjad.tools import tuplettools
      assert isinstance(arg, type(self))
      new = tuplettools.fuse_tuplets([self, arg])
      return new
      
   def __repr__(self):
      if 0 < len(self):
         return '_Tuplet(%s)' % self._summary
      else:
         return '_Tuplet( )'

   ## PRIVATE ATTRIBUTES ##

   @property
   def _summary(self):
      if 0 < len(self):
         return ', '.join([str(x) for x in self._music])
      else:
         return ' '

   @property
   def _is_visible(self):
      return not self.is_invisible

   ## PUBLIC ATTRIBUTES ##

   @apply
   def force_fraction( ):
      '''Read / write boolean to force n:m fraction.'''
      def fget(self):
         return self._force_fraction
      def fset(self, arg):
         if isinstance(arg, (bool, type(None))):
            self._force_fraction = arg
         else:
            raise TypeError
      return property(**locals( ))

   @apply
   def is_invisible( ):
      def fget(self):
         '''Read / write boolean to render tuplet invisible.'''
         return self._is_invisible
      def fset(self, arg):
         assert isinstance(arg, (bool, type(None)))
         self._is_invisible = arg
      return property(**locals())

   @property
   def is_trivial(self):
      '''True when tuplet multiplier is one, otherwise False.'''
      return self.duration.multiplier == 1

   @property
   def ratio(self):
      '''Tuplet multiplier formatted with colon as ratio.'''
      multiplier = self.duration.multiplier
      if multiplier is not None:
         return '%s:%s' % (multiplier.denominator, multiplier.numerator)
      else:
         return None
