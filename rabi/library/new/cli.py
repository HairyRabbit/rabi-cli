# -*- mode: python -*-
# -*- coding: utf-8 -*-

import sys
import argparse
import getopt
import textwrap
from rabi.library.new.proc import main as proc


def arg_name(cmder):
    """Argument name

    Library name.
    """

    helper = 'direction name'

    cmder.add_argument('name', help=helper)


def arg_path(cmder):
    """Argument path
    
    Mount path, default to current directory.
    """

    helper = """
    which path to be create. [default] the current directory.
    """

    cmder.add_argument('path', nargs='?', help=helper, default='.')


def main(parser):
    """Main

    Main entry for create library.
    """

    desc  = open('rabi/library/new/helper.txt').read()
    help  = 'create a new library'
    alias = 'n'
    cmder = parser.add_parser(
        'new', aliases=[alias], help=help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(desc))
    
    cmder.set_defaults(func=proc)
  
    arg_name(cmder)               # Required argument name
    arg_path(cmder)               # Optional argument path
    
