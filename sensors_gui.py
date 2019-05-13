import bluepy.btle as btle
import struct
from MainWindow import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class SpeedDelegate(btle.DefaultDelegate):
	def __init__(self):
		btle.DefaultDelegate.__init__(self)
		self.prevCRev = None
		self.prevETime = None

	def handleNotification(self, cHandle, data):
		cRev, eTime = struct.unpack("IH", data[1:1+4+2])
		eTime /= 1024.
		if self.prevCRev and cRev > self.prevCRev and eTime > self.prevETime:
			speed = ((cRev - self.prevCRev) * 72 * 0.09144) / float(eTime - self.prevETime)
			print("Speed: " + str(speed) + " km/h") 
			ui.speed.display(speed)
		self.prevCRev = cRev
		self.prevETime = eTime

class CadenceDelegate(btle.DefaultDelegate):
	def __init__(self):
		btle.DefaultDelegate.__init__(self)
		self.prevCRev = None
		self.prevETime = None

	def handleNotification(self, cHandle, data):
		cRev, eTime = struct.unpack("HH", data[1:1+2*2])
		eTime /= 1024.
		if self.prevCRev and cRev > self.prevCRev and eTime > self.prevETime:
			#print("cRev: " + str(self.prevCRev) + " -> " + str(cRev) + "\t" + "eTime: " + str(self.prevETime) + " -> " + str(eTime))
			cadence = ((cRev - self.prevCRev) * 60.) / float(eTime - self.prevETime)
			print("Cadence: " + str(cadence) + " rpm")
			ui.cadence.display(cadence)
		self.prevCRev = cRev
		self.prevETime = eTime

print("Connecting to speed sensor...")
spdPeri = btle.Peripheral("<address>", btle.ADDR_TYPE_RANDOM)
spdPeri.setDelegate(SpeedDelegate())
spdPeri.writeCharacteristic(0x0024, b"\1\0", True)
print("Speed sensor connected")

print("Connecting to cadence sensor...")
cadPeri = btle.Peripheral("<address>", btle.ADDR_TYPE_RANDOM)
cadPeri.setDelegate(CadenceDelegate())
cadPeri.writeCharacteristic(0x0024, b"\1\0", True)
print("Cadence sensor connected")


def checkForUpdates():
	spdPeri.waitForNotifications(0.1)
	cadPeri.waitForNotifications(0.1)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.showMaximized()

timer = QtCore.QTimer()
timer.timeout.connect(checkForUpdates)
timer.start(0)

sys.exit(app.exec_())
