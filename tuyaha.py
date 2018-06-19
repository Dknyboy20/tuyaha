import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.discovery import load_platform

REQUIREMENTS = ['tuyaapi==7.1']
DOMAIN = 'tuyaha'
CONF_USER_EMAIL = 'email'
CONF_USER_PASSW = 'password'
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_USER_EMAIL): cv.string,
        vol.Required(CONF_USER_PASSW): cv.string,
    }),
}, extra=vol.ALLOW_EXTRA)
tapi = None

def setup(hass, config):
    import tuyaapi
    global tapi
    email = config.get(DOMAIN, {}).get(CONF_USER_EMAIL)
    passwd = config.get(DOMAIN, {}).get(CONF_USER_PASSW)
    tapi = tuyaapi.TuyaAPI(email, passwd)
    devs = tapi.ldevbyuser()
    for dev in devs:
        load_platform(hass, 'switch', DOMAIN, dev)
    return True
