#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    PATHS = [os.path.realpath(os.path.join(BASE_DIR, 'apps'))]
    for path in PATHS:
        sys.path.insert(0, path)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
