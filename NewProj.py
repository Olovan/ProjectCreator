#!python3
import sys
import os

NAME = "Micah Smith"

def main(argv):
	if len(argv) == 3:
		os.mkdir(argv[1])
		os.chdir(argv[1])
		if argv[2] == "C":
			os.mkdir("src")
			os.mkdir("bin")
			#compFile = open("compile.sh", 'w')
		elif argv[2] == "Java":
			os.mkdir("src")
			os.mkdir("bin")
			appFileName = argv[1] + "Application"
			compFile = open("compile.sh", 'w')
			compFile.write("#!/bin/sh\njavac -d \"bin/\" -cp \"src/\" src/" + appFileName + ".java")
			compFile.close()
			runFile = open("run.sh", 'w')
			runFile.write("#!/bin/sh\njava -cp \"bin/\" " + appFileName)
			runFile.close()
			appFile = open("src/" + appFileName + ".java", 'w')
			appFile.write( "/* NAME: " + NAME + "\n*/ \npublic class " + appFileName + "\n{\n\tpublic static void main(String[] args)\n\t{\n\t\tSystem.out.println(\"Hello World\");\n\t}\n}\n") 

			

			
	else:
		print("Must give a project name");

if __name__ == "__main__":
	main(sys.argv)

