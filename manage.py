#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s %(message)s', level=logging.WARN)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s %(message)s', level=logging.ERROR)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s %(message)s', level=logging.WARNING)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soutenance.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
