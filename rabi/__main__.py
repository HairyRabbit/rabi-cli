# -*- mode: python -*-
# -*- coding: utf-8 -*-

import sys

# Development mode
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..\\'))


def main():
    from rabi.cli import main
    sys.exit(main())


if __name__ == '__main__':
    main()
    
