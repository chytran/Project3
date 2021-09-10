#!c:\xampp\htdocs\project3\.venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'prettify==0.1.1','console_scripts','prettify'
__requires__ = 'prettify==0.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('prettify==0.1.1', 'console_scripts', 'prettify')()
    )
