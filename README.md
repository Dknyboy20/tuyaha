tuyaha
======

This is is more complex platform for Home Assistant that allows you to control your Tuya Smart devices from Home Assistant via the Tuya cloud.
It uses the tuyaapi library (https://github.com/sean6541/tuyaapi) to interface with the Tuya cloud. (No need to install as Home Assistant automatically installs it.)
To use, copy the contents of this repository to "/custom_components" and add config below to configuration.yaml
Config Example:
```
tuyaha:
    email: example@example.com
    password: somecrazypassword
    
switch:
  - platform: tuyaha
    device_id: xxxxxxxxxxxxxxxxxxxx
    switches:
        switch1:
            friendly_name: Switch 1
            id: 1
```
