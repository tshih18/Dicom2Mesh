import os
import re
import scipy.misc as misc

def tryint(c):
	try:
		return int(c)
	except:
		return c

# turn a string into a list of string and number chunks
def alphanum_key(s):
	return [tryint(c) for c in re.split('([0-9]+)', s)]

# sort the given list
def natural_sort(list):
	list.sort(key=alphanum_key)

path1 = "/home/aether/Desktop/Ankle_png (bad)/"

num = 99

for dirName, subdirList, fileList in os.walk(path1):
		natural_sort(fileList)
		print "hi"
		for filename in fileList:
			print(filename)
			img = misc.imread(os.path.join(dirName,filename))
			misc.imsave("female_ankle/ankle-slice" + str(num) + ".png", img)
			num += 1