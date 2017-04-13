import sys
import time
import Tkinter as tk
import tkMessageBox

root = tk.Tk()
root.withdraw()
wakehr = 0
wakemin = 0
while (True):
	if wakehr == 0 and wakemin == 0:
		wakehr = raw_input("\nEnter wake hour:\n ")
		wakemin = raw_input("\nEnter wake min:\n ")
		print "Waketime set for:", wakehr, ":", wakemin, 
	if ((time.strftime("%H")) == wakehr and (time.strftime("%M")) == wakemin ):
		print "WAKE UP SURBHI"
		tkMessageBox.showwarning('alert title', 'WAKE UP SURBHI')

