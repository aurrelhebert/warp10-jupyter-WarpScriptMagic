try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
import json
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from IPython.core.magic import (Magics, magics_class,
                                line_cell_magic, needs_local_scope)
from IPython.testing.skipdoctest import skip_doctest
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)
from IPython.utils.py3compat import unicode_to_str
from IPython.utils.text import dedent

class WarpScriptMagicError(Exception):
    pass

@magics_class
class WarpScriptMagics(Magics):
    """
A set of magics useful for interactive work with Warp 10.
"""

    def __init__(self, shell):
        super(WarpScriptMagics, self).__init__(shell)

    @skip_doctest
    @magic_arguments()
    @argument(
        '-u', '--url', action='append', nargs = "*",
        help='Warp 10 url to reach'
        )

    @line_cell_magic
    def warpscript(self, line, cell=None, local_ns=None):
         args = parse_argstring(self.warpscript, line)

         if args.url is not  None:
            if len(args.url[0]) > 1:
                    warnings.warn("\nOnly one url accepted", UserWarning)
            url = unicode_to_str(args.url[0][0])
            binary_code = code.encode('UTF-8')
            req = urllib2.Request(url, binary_code)
            rsp = urllib2.urlopen(req)

            content = rsp.read()

            if not silent:
                str_response = content.decode('UTF-8')
                obj = json.loads(str_response)
                stream_content = {'name': 'stdout', 'text': content.decode('UTF-8')}
                self.send_response(self.iopub_socket, 'stream', stream_content)

            return {'status': 'ok',
                    # The base class increments the execution count
                    'execution_count': self.execution_count,
                    'payload': [],
                    'user_expressions': {},
                   }

    def load_ipython_extension(ip):
      """Load the extension in IPython."""
      ip.register_magics(WarpScriptMagics)