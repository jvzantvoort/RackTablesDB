#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""RackTablesDB.config - read the configuration for the RackTablesDB"""

import os
import logging
import ConfigParser
import traceback

class Config(object):

    def __init__(self):
        self.variables = dict()
        self.database = dict()
        self.has_been_read = False
        self.configfiles = list()
        self.configfiles.append(os.path.expanduser('~/.RackTablesDB.cfg'))
        # NOTE: add smart extras

    def read(self):

        parser = ConfigParser.ConfigParser()

        for configfile in self.configfiles:
            if not os.path.exists(configfile):
                logging.info('file {0} does not exist'.format(configfile))
                continue

            try:
                parser.read(configfile)
            except:
                # NOTE: bad
                logging.error(traceback.format_exc())
                pass

            if parser.has_section('database'):
                for option in parser.options('database'):
                    self.database[option] = parser.get('database', option)
            self.has_been_read = True

    @property
    def user(self):
        """return database user"""
        if 'user' in self.database:
            return self.database['user']

        if self.has_been_read:
            raise KeyError('cannot access value: user')

        self.read()

        return self.user

    @property
    def password(self):
        """return database password"""
        if 'password' in self.database:
            return self.database['password']

        if self.has_been_read:
            raise KeyError('cannot access value: password')

        self.read()

        return self.password

    @property
    def name(self):
        """return database name"""
        if 'name' in self.database:
            return self.database['name']

        if self.has_been_read:
            raise KeyError('cannot access value: name')

        self.read()

        return self.name

    @property
    def host(self):
        """return database host"""
        if 'host' in self.database:
            return self.database['host']

        if self.has_been_read:
            # default to localhost
            self.database['host'] = 'localhost'

        self.read()

        return self.host

