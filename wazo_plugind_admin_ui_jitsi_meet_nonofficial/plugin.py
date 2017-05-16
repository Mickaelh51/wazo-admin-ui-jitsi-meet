# -*- coding: utf-8 -*-
# Copyright 2017 HUBERT Mickael  (see the AUTHORS file)
# SPDX-License-Identifier: MIT

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint


from .service import JitsiMeetService
from .view import JitsiMeetView

jitsi_meet = create_blueprint('jitsi_meet', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        JitsiMeetView.service = JitsiMeetService()
        JitsiMeetView.register(jitsi_meet, route_base='/jitsimeet')
        register_flaskview(jitsi_meet, JitsiMeetView)

        core.register_blueprint(jitsi_meet)
