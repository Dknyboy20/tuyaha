Quick Setup Guide
=================

Before starting, you must have Python 3.4 or newer installed.

On the device running Home Assistant...
---------------------------------------

1. Copy the contents of this repository to "/custom_components"
2. Enable the platform by adding the configuration below to configuration.yaml
```
tuyaha:
    email: example@example.com
    password: somecrazypassword
```
3. Home Assistant will automatically find all your Tuya devices, but if you want to, add the configuration below to configuration.yaml
```
switch:
  - platform: tuyaha
    device_id: xxxxxxxxxxxxxxxxxxxx
    switches:
        switch1:
            friendly_name: Switch 1
            id: 1
```
