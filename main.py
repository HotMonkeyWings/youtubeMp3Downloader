import pafy
import platform
url = input("Enter video link: ")
v = pafy.new(url)
strm = v.getbestaudio()
dest = input("Enter destination folder: ")
if dest == '':
	strm.download()
else:
	try:
		strm.download(dest)
	except:
		print("Invalid destination")