# -*- mode: python -*-
# -*- coding: utf-8 -*-

import sys
import argparse
import getopt
import textwrap
from rabi.library.new.cli import main as cmd_new


def main(parser, parent_prog):
    prog  = 'lib'
    alias = 'l'
    desc  = open('rabi/library/helper.txt').read()
    cmder = parser.add_parser(
        prog, aliases=[alias],
        help='library tools',        
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(desc)
    )

    subcmder = cmder.add_subparsers(
        title='SubCommands', prog='{0} {1}'.format(parent_prog, prog)
    )
    
  
    cmd_new(subcmder)              # Register command create.

    return prog, alias, cmder
