#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io



CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
 

"""v = intentMessage.slots.ville.first().value
r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=v&appid=c427cad62f8bfde6ed0e800f59e1a39d&lang=fr&units=metric")
data=r.json()

s = data["weather"][0]
d = s["description"]
tm  = data["main"]["temp_min"]
tM = data["main"]["temp_max"]

m =u"Ce jour à " + ville + " " +  d + u" température entre " + str(tm) + " et " + str(tM) + u" degrés"
"""
    m = "bien appelé cher Monsieur"
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, m)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("louisros:today", subscribe_intent_callback) \
        .start()
