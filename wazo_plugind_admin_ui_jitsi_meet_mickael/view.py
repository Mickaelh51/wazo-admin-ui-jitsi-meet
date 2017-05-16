# -*- coding: utf-8 -*-
# Copyright 2017 The HUBERT Mickael  (see the AUTHORS file)
# SPDX-License-Identifier: MIT

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, IndexAjaxViewMixin

from .form import JitsiMeetForm


class JitsiMeetView(IndexAjaxViewMixin, BaseView):

    form = JitsiMeetForm
    resource = 'jitsi-meet'

    @classy_menu_item('.jistmeet', 'Jitsi Meet', order=4, icon="compress")
    def index(self):
        return super(JitsiMeetView, self).index()
