# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, IndexAjaxViewMixin

from .form import JitsiMeetForm


class JitsiMeetView(IndexAjaxViewMixin, BaseView):

    form = JitsiMeetForm
    resource = 'jitsi_meet'

    @classy_menu_item('.jistmeet', 'Jitsi Meet', order=4, icon="compress")
    def index(self):
        return super(JitsiMeetView, self).get(None)


    def _map_resources_to_form(self, resource):
        form = self.form(data=resource)
        return form
