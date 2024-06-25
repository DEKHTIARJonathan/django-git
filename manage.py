#!/usr/bin/env python
import sys
from os import environ

if __name__ == "__main__":
	environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)
