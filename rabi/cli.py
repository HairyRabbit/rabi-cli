# -*- mode: python -*-
# -*- coding: utf-8 -*-

import sys
import argparse
import getopt
import textwrap
from rabi import __version__ as version
from rabi.library.cli import main as libcmder


def arg_version(parser):
    parser.add_argument(
        '-v', '--version', action='version',
        version='version {0}'.format(version),
        help='print rabi version.')

    
def main():
    prog  = 'rabi'
    cmder = argparse.ArgumentParser(
        prog=prog, epilog="Happy Hack",
        usage="%(prog)s [command] [options]")

    # Sub Parsers
    subcmder = cmder.add_subparsers(
        title='commands', dest='subs',
        prog=prog)

    # Print version
    arg_version(cmder)

    # Command::lib
    libprog, libalias, libparser = libcmder(subcmder, prog)

    # Command::app
    
    
    args = cmder.parse_args()
    subs = vars(args)['subs']

    if subs == libprog or subs == libalias:
        libparser.print_help()
    else:
        cmder.print_help()
