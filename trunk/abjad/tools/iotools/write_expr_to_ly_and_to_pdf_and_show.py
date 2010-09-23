from abjad.cfg._open_file import _open_file
from abjad.cfg._read_config_file import _read_config_file
from abjad.tools.iotools.write_expr_to_ly import write_expr_to_ly
from abjad.tools.iotools.write_expr_to_pdf import write_expr_to_pdf
from abjad.tools.iotools.show import show


def write_expr_to_ly_and_to_pdf_and_show(expr, name, template = None, write = True):
   '''When ``write = True`` (default) call ``write_ly(expr)`` and 
   ``write_pdf(expr)`` and then open the resulting PDF.

   When ``write = False`` call ``show(expr)`` only.

   The purpose of this function is to conditionally save named PDF
   and named ``.ly`` output corresponding to `expr`.

   .. versionchanged:: 1.1.2
      renamed ``io.write_and_show( )`` to
      ``io.write_expr_to_ly_and_to_pdf_and_show( )``.
   '''

   lily_time = 10

   if write:
      write_expr_to_ly(expr, name + '.ly', template = template)
      write_expr_to_pdf(expr, name + '.pdf', template = template)
      pdf_viewer = _read_config_file( )['pdf_viewer']
      _open_file(name + '.pdf', pdf_viewer)
   else:
      show(expr, template = template)
