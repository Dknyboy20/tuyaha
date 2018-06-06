import voluptuous as vol
from homeassistant.components.switch import SwitchDevice, PLATFORM_SCHEMA
import custom_components.tuyaha as tuyaha
import homeassistant.helpers.config_validation as cv
import time

REQUIREMENTS = ['tuyaapi==6.0']
DEPENDENCIES = ['tuyaha']
CONF_DEVICE_ID = 'device_id'
CONF_SWITCHES = 'switches'
CONF_ID = 'id'
CONF_FRIENDLY_NAME = 'friendly_name'
DEFAULT_ID = '1'
SWITCH_SCHEMA = vol.Schema({
    vol.Optional(CONF_ID, default=DEFAULT_ID): cv.string,
    vol.Optional(CONF_FRIENDLY_NAME): cv.string,
})
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_DEVICE_ID): cv.string,
    vol.Optional(CONF_SWITCHES, default={}):
        vol.Schema({cv.slug: SWITCH_SCHEMA}),
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    import tuyaapi
    switches = []
    if discovery_info == None:
        devid = config.get(CONF_DEVICE_ID)
        tdev = tuyaapi.TuyaSwitch(tuyaha.tapi, devid)
        devices = config.get(CONF_SWITCHES)
        for id, devconf in devices.items():
            switches.append(
                TuyaSwitch(
                    tdev,
                    devconf.get(CONF_ID),
                    devconf.get(CONF_FRIENDLY_NAME, id)
                )
            )
    else:
        devid = discovery_info['devId']
        tdev = tuyaapi.TuyaSwitch(tuyaha.tapi, devid)
        swcount = tdev.getsws()
        name = discovery_info['name']
        if swcount == 1:
            switches.append(
                TuyaSwitch(
                    tdev,
                    1,
                    name
                )
            )
        else:
            i = 1
            while i <= swcount:
                switches.append(
                    TuyaSwitch(
                        tdev,
                        i,
                        name + ': ' + str(i)
                    )
                )
                i = i + 1
    add_devices(switches)

class TuyaSwitch(SwitchDevice):
    def __init__(self, tdev, swid, name):
        self._tdev = tdev
        self._swid = swid
        self._name = name
        self._state = False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self._tdev.setstate(True, self._swid)
        time.sleep(1)

    def turn_off(self, **kwargs):
        self._tdev.setstate(False, self._swid)
        time.sleep(1)

    def update(self):
        self._state = self._tdev.getstate(self._swid)
