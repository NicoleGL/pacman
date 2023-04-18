# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Pak-Nam",
    version="1.0",
    description="Copia de PacMan",
    author="Alex, Bruno, Nicole y Pablo",
    scripts=["main.py", "board.py", "button.py", "ghost.py", "pacman.py"],
    console=["main.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)