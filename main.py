#!/usr/bin/env python3

import pafy
import platform
import tkinter as tk
from tkinter import filedialog

while 1:
	url = input("Enter video link: ")
	v = pafy.new(url)
	strm = v.getbestaudio()

	root = tk.Tk()
	root.withdraw()
	dest = filedialog.askdirectory()

	strm.download(dest)

	cont = input("Download again?(Y/n): ")
	if(cont != 'Y' and cont != 'y'):
		break