tuyaha
======

This is a more complex platform for Home Assistant that allows you to control your Tuya Smart devices from Home Assistant via the Tuya cloud.

`email` and `password` are your Tuya account details. If you don't have an account, your account will be created with the information provided.

**Important Notice: You must set up your device using the Python library tuyaapi or it will not work in Home Assistant!** You can find a script to help you do that here: https://raw.githubusercontent.com/sean6541/file/master/tuyasetup.py

It uses the tuyaapi library (https://github.com/sean6541/tuyaapi) to interface with the Tuya cloud. (No need to install as Home Assistant automatically installs it.)

It will automatically find all devices on your account and add them to Home Assistant.

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

See INSTALL.md for an easy install guide.
