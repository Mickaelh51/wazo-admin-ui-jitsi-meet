#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_admin_ui_jit_meet_mickael',
    version='0.1',

    description='Wazo Admin UI Jit Meet',

    author='Mickael HUBERT',
    author_email='',

    url='https://github.com/Mickaelh51/wazo-admin-ui-jitsi-meet',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'wazo_admin_ui.plugins': [
            'jit_meet = wazo_plugind_admin_ui_jitsi_meet_mickael.plugin:Plugin',
        ]
    }
)
