import os
import datetime
import shutil
from os import path
from datetime import date, time, timedelta		#	Note
import time										#<---|
from zipfile import ZipFile
from shutil import make_archive

file_name = "anhtuan.txt"

def O_S():
	# Print the name of the OS
	print os.name, "\n"

	# Check for item existence and type
	print "Item exists: " + str(path.exists(file_name))  # ton tai
	print "Item is a file: " + str(path.isfile(file_name))
	print "Item is a directory: " + str(path.isdir(file_name))

	# Work with file paths
	print "\nItem's path: " + str(path.realpath(file_name))
	print "Item's path and name: " + str(path.split(path.realpath(file_name))), "\n"

	# Get the modification time
	t = time.ctime(path.getmtime(file_name))
	print t, "\t", path.getmtime(file_name)
	print datetime.datetime.fromtimestamp(path.getmtime(file_name))


def File_System_Shell_Methods():
	# make a duplicate of an existing file
	print "Item exists: " + str(path.exists(file_name)), "\n"
	if path.exists(file_name):			# Co file_name trong thu muc
		src = path.realpath(file_name)	# Duong dan
		print src

		''' Tach duong dan va ten file '''
		head, tail = path.split(src)
		print "path:", head
		print "file:", tail, "\n"

		''' Tao 1 file '.bak' & coppy du lieu tu file_name '''
		dst = src + ".bak"
		shutil.copy(src, dst)
		#shutil.copystat(src,dst)

		''' Save into file zip (tat ca file trong folder) '''
		root_dir, tail = path.split(src)
		shutil.make_archive("anhtuan archive", "zip", root_dir)
		print path.split(src)

		''' Save into file zip (chi luu cac file duoc chi dinh) '''
		#with ZipFile("anhtuan.zip", "w") as newzip:
			#newzip.write(file_name)
			#newzip.write(file_name + ".bak")

def Rename_file(old_name, new_name):
	''' Rename file_name '''
	os.rename(old_name, new_name)
	print  path.exists(old_name), "\t", old_name
	print  path.exists(new_name), "\t", new_name


def main():
	O_S()
	File_System_Shell_Methods()
	#Rename_file("st1.txt","anhtuan.txt")

if __name__== "__main__":
	  main()