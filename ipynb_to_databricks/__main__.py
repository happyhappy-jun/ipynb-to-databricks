""" Main for Jupytext

Call with (e.g.)::

    python -m main my_notebook.ipynb --to Rmd
"""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())