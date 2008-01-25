from .. core.initializer import _Initializer
from .. helpers.attributes import transfer_all_attributes

class NoteInitializer(_Initializer):
   
   def __init__(self, client, Leaf, *args): 
      from .. rest.rest import Rest
      from .. chord.chord import Chord
      from .. skip.skip import Skip

      client.notehead = None
      if len(args) == 0:
         Leaf.__init__(client, None, None)
      elif len(args) == 1 and isinstance(args[0], Leaf):
         if args[0].kind('Note'):
            Leaf.__init__(client, None, None)
            note = args[0]
            transfer_all_attributes(note, client)
         if args[0].kind('Rest'):
            Leaf.__init__(client, None, None)
            rest = args[0]
            del rest._pitch
            transfer_all_attributes(rest, client)
         elif args[0].kind('Chord'):
            Leaf.__init__(client, None, None)
            chord = args[0]
            transfer_all_attributes(chord, client)
            if len(chord) > 0:
               copy = chord.copy( )
               client.notehead = copy.noteheads[0]
         elif args[0].kind('Skip'):
            Leaf.__init__(client, None, None)
            skip = args[0]
            transfer_all_attributes(skip, client)
      elif len(args) == 1:
         Leaf.__init__(client, None, None)
         pitch = args[0]
         client.pitch = pitch
      elif len(args) == 2:
         pitch, duration = args
         Leaf.__init__(client, duration, None)
         client.pitch = pitch
      elif len(args) == 3:
         pitch, duration, multiplier = args
         Leaf.__init__(client, duration, multiplier)
         client.pitch = pitch
      else:
         raise ValueError('can not initialize note.')
