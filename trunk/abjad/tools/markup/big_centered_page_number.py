from abjad.markup import Markup
import types


def big_centered_page_number(text = None):
   r'''.. versionadded:: 1.1.1

   Make big centered page number markup::

      abjad> t = markup.centered_page_number( )
      abjad> print t.format
      \markup { 
         \fill-line {
         \bold \fontsize #3
         \on-the-fly #print-page-number-check-first
         \fromproperty #'page:page-number-string } }

   Return markup.
   '''

   assert isinstance(text, (str, types.NoneType))

   contents = r'''
   \fill-line {
   \bold \fontsize #3 \concat {
   \on-the-fly #print-page-number-check-first
   \fromproperty #'page:page-number-string'''

   if text is None:
      contents += ' } }'
   else:
      contents += '\n   " - " %s } }' % text

   markup = Markup(contents)

   return markup
