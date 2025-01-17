import voluptuous as vol
from datetime import timedelta

from homeassistant.helpers import config_validation as cv
from homeassistant.const import (TEMP_CELSIUS, PERCENTAGE)
DOMAIN = 'philips_somneo'
PREFIX = 'Somneo '
DATA_SOMNEO = 'data_somneo'
DATA_PSC = 'PSC'
VERSION = "0.2"
UNIQUE_ID_PREFIX = "somneo"

DEFAULT_NAME = "somneo"
DEFAULT_HOST = "192.168.2.131"
DEFAULT_CTYPE = "3"
DEFAULT_INTERVAL = 60

CONF_NAME = 'name'
CONF_HOST = 'host'
CONF_SENS = 'sensors'
CONF_INTERVAL = 'scan_interval'

CONF_CTYPE = "ctype"
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=60)
#SCAN_INTERVAL = timedelta(seconds=60)


SENSOR_TYPES = {
    "temperature": ["Temperature", TEMP_CELSIUS, "mdi:thermometer"],
    "humidity": ["Humidity", PERCENTAGE, "mdi:water-percent"],
    "illuminance": ["Illuminance", "lux", "mdi:brightness-6"],
    "noise": ["Noise", "dB", "mdi:waveform"]
}

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_INTERVAL, default=DEFAULT_INTERVAL):  cv.time_period,
        vol.Optional(CONF_SENS, default=list(SENSOR_TYPES)): [vol.In(SENSOR_TYPES)],
    })
}, extra=vol.ALLOW_EXTRA)


NOTIFICATION_ID = "somneosensor_notification"
NOTIFICATION_TITLE = "SomneoSensor Setup"

ATTR_C_NAME = "name"
ATTR_C_HOST = "host"
ATTR_C_SENS = "sensors"
ATTR_C_SURL = "sensor_url"
ATTR_C_LURL = "light_url"
ATTR_C_INT = "scan_interval"

ATTR_S_TEMP = "temperature"
ATTR_S_HUM = "humidity"
ATTR_S_LIGHT = "illuminance"
ATTR_S_NOISE = "noise"

ATTR_L_ONOFF = "state"
ATTR_L_LTLVL = "intensity"
ATTR_L_CTYPE = "light_type"
ATTR_L_NGTLT = "night_light"


#ENTITY_ID_FORMAT = DOMAIN + ".{}"
#SOMNEO_COMPONENTS = ["sensor", "light"]




