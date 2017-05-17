#-*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import json, jwt, random, string

configfile = '/etc/jitsi_meet/config.json'

class JitsiMeetService(object):
    def get(self, arg):
        configjson =  self._read_config()
        print self._generate_token(configjson)
        return self._generate_token(configjson)

    def update(self, resource):
        config = self._read_config()
        config['jitsi_url'] = resource.get('jitsi_url')
        config['secret_id'] = resource.get('secret_id')
        config['app_id'] = resource.get('app_id')
        config['auth_method'] = resource.get('auth_method')
        config['firefox_plugin'] = resource.get('firefox_plugin')
        config['chrome_plugin'] = resource.get('chrome_plugin')

        with open(configfile, 'w') as outfile:
            json.dump(config, outfile, indent = 4)

        return True

    def _read_config(self):
        with open(configfile) as json_data:
            data2 = json.load(json_data)
            print "config file " + str(data2)
            #return json.load(json_data)
            return data2

    def _generate_token(self, configjson):
        print configjson['jitsi_url']
        if configjson['jitsi_url'] and configjson['secret_id'] and configjson['auth_method'] != "anonymous" and configjson['app_id']:
            room = self._generate_room()
            if configjson['auth_method'] == "new_token":
                data = { "iss": configjson['app_id'], "room": room, "aud": "visio.hexavoip.fr" }
                jwttoken = jwt.encode(data, configjson['secret_id'], algorithm='HS256')
                tokenurl = "/" + str(room) + "?jwt=" + str(jwttoken)
            elif configjson['auth_method'] == "old_token":
                data = { "iss": configjson['app_id'], "room": room, "aud": "visio.hexavoip.fr" }
                jwttoken = jwt.encode(data, configjson['secret_id'], algorithm='HS256')
                tokenurl = "/" + str(room) + "#config.token=\"" + str(jwttoken) + "\""

            configjson['url_token'] = configjson['jitsi_url'] + tokenurl
            return configjson

        else:
            print "No information to generate token or it's anonymous method"
            configjson['url_token'] = configjson['jitsi_url']
            print configjson
            return configjson

    def _generate_room(self):
        return ''.join(random.choice(string.lowercase) for i in range(30))
