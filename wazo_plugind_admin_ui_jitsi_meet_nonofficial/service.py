#-*- coding: utf-8 -*-
# Copyright 2017 The HUBERT Mickael  (see the AUTHORS file)
# SPDX-License-Identifier: MIT

from wazo_admin_ui.helpers.service import BaseConfdExtensionService


class JitsiMeetService(BaseConfdExtensionService):

    resource_confd = 'parking_lots'
