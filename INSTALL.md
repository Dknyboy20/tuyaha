Quick Setup Guide
=================

Before starting, you must have Python 3.4 or newer installed on your computer.

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

On your computer if running Windows...
-------------------

1. Download https://raw.githubusercontent.com/sean6541/file/master/tuyasetup.py
2. Open a cmd window and cd to the directory containing the file you just downloaded
3. Run `python -m pip install tuyaapi`
4. Run `python tuyasetup.py` and follow the prompts. **You will have to do this for every device you want to add to Home Assistant and once you do this, you can no longer use any app to control your device unless you reset it and then it will no longer work with Home Assistant.**
5. Restart your Home Assistant device

On your computer if running linux...
-------------------

1. Run `wget https://raw.githubusercontent.com/sean6541/file/master/tuyasetup.py`
2. Run `python -m pip install tuyaapi`
3. Run `python tuyasetup.py` and follow the prompts. **You will have to do this for every device you want to add to Home Assistant and once you do this, you can no longer use any app to control your device unless you reset it and then it will no longer work with Home Assistant.**
4. Restart your Home Assistant device
