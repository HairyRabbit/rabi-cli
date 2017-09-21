# -*- mode: python -*-
# -*- coding: utf-8 -*-

import sys
import argparse
import getopt
import textwrap
from rabi.new.lib.proc import main as proc


def arg_name(cmder):
  """ Library name
  """

  helper = 'direction name'

  cmder.add_argument('name', help=helper)


def arg_path(cmder):
  """ Create path
  """

  helper = """
  which path to be create. [default] the current directory.
  """

  cmder.add_argument('path', nargs='?', help=helper, default='.')


def main(parser):
  
  helper = 'create a new library'
  alias  = 'l'
  
  cmder  = parser.add_parser(
    'lib', aliases=[alias],
    help=helper
  )


  arg_name(cmder)
  arg_path(cmder)

  cmder.set_defaults(func=proc)
