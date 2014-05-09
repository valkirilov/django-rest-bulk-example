#!/usr/bin/env python
import os
import sys

libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'libs'))
if libpath not in sys.path:
	sys.path.insert(0, libpath)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "giftycards.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
