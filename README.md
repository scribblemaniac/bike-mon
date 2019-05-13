# bike-mon

bike-mon is a graphical application to display speed and cadence measurements from a bicycle Bluetooth sensor.

## Requirements

As far as hardware requirements go, bike-mon was designed to be used on a Raspberry Pi with a touchscreen connected to it, but it should work any system that has Bluetooth and can run Python. If you want to use this with a non-stationary bike, you will obviously also need a portable power source. There are no other specific requirements.

For software requirements, you need to have Python 3 installed. Additionally you will need the following libraries which can be installed with pip:
- `pyqt5`
- `bluepy`

## Using the Program

To start bike-mon, you will need to first define the Bluetooth addresses of your speed and cadence sensors in the code. Open up sensors_gui.py in your favorite text editor and locate the following two lines of code:

```python
spdPeri = btle.Peripheral("<address>", btle.ADDR_TYPE_RANDOM)
cadPeri = btle.Peripheral("<address>", btle.ADDR_TYPE_RANDOM)
```
The first line is for the speed sensor and the second line is for the cadence sensor. Replace "<address>" in each with the Bluetooth MAC address corresponding to that peripheral and then save the file. To find your address look the device in the table below or find it using [this guide](https://www.pcsuggest.com/linux-bluetooth-setup-hcitool-bluez/). If you have an unlisted device, please consider submitting a pull request to add it to the table.

| Device Name    | Speed Address     | Cadence Address   |
| -------------- | ----------------- | ----------------- |
| Polar 91047327 | C4:D3:54:E8:33:B9 | E0:25:5E:B0:4D:EC |

Now you can startup the application by running sensors_gui.py. That's all you need to do. The program should automatically connect to the addresses you specified and start outputting your current speed and cadence.

If you want easy access to the application and are on a GNOME system, you can create an application entry by copying the desktop file to the correct location on your system (usually `/usr/share/applications` or `~/.local/share/applications`).
