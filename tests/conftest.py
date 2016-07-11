#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for RackTablesDB.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import RackTablesDB.config
import logging
import sys

rootlogger = logging.getLogger()
rootlogger.setLevel(logging.DEBUG)

consolehandler = logging.StreamHandler(sys.stdout)
consolehandler.setFormatter(logging.Formatter("%(levelname)s:  %(message)s"))
rootlogger.addHandler(consolehandler)

rtdb_cfg = RackTablesDB.config.Config()

print rtdb_cfg.user
print rtdb_cfg.password
print rtdb_cfg.name

