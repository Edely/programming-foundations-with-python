import os

def rename_files():
	file_list = os.listdir("/home/edely/Documentos/Projetos/Full Stack/01/code/prank")
	print file_list

	saved_path = os.getcwd()
	os.chdir("/home/edely/Documentos/Projetos/Full Stack/01/code/prank")
	

	print("Current Working Directory is "+ saved_path)

	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789") )
	os.chdir(saved_path)

rename_files()