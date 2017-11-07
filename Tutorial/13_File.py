file_name = "anhtuan.txt"

def Create_file():
	# Open(Create) file .txt
	f = open(file_name, "w+")	# tao moi
	#f = open("guru99.txt","a+")	# a -> noi them	||	a+ -> chua co .txt thi tao
	for i in range(5):
		f.write("Anhtuanst%d\r\n" % (i+1))	# Write .txt
	f.close()	# Close .txt

def Read_file():
	# Open the file back and read the contents
	f = open(file_name, "r")
	if f.mode == 'r':
		contents = f.read()
		print "contents:\n", contents, "\n\n"

def Readline_file():
	f = open(file_name, "r")
	f = f.readlines()
	for x in f:
		print x

def main():
	Create_file()
	Read_file()
	Readline_file()


if __name__== "__main__":
  main()