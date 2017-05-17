# -*- coding: utf-8 -*-
# Copyright 2017 HUBERT Mickael  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import (SubmitField,
                            StringField,
                            SelectField,
                            FieldList,
                            FormField)
from wtforms.fields.html5 import IntegerField, URLField
from wtforms.validators import InputRequired, NumberRange, Length, Regexp, URL

from wazo_admin_ui.helpers.form import BaseForm


class JitsiMeetForm(BaseForm):
    jitsi_url = URLField('Url for Jitsi Meet instance', [InputRequired()], default='https://meet.jit.si')
    secret_id = StringField('Secret ID', [Length(max=80)], render_kw={'type': 'password', 'data_toggle': 'password'})
    app_id = StringField('App ID', [Length(max=80)])
    auth_method = SelectField('Authentification method',
                           validators=[InputRequired()],
                           choices=[
                               ('anonymous', 'Anonymous (without token)'),
                               ('old_token', 'Old token method (#conf.token)'),
                               ('new_token', 'New token method (?jwt=)')
                           ])
    firefox_plugin = URLField('Url for firefox plugin', [])
    chrome_plugin = URLField('Url for Chrome plugin', [])
    submit = SubmitField('Submit')
