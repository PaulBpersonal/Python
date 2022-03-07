

import os
import pandas as pd
import glob


path='C:/Users/Paul/Desktop/Open Multiple'
dest='C:/Users/Paul/Desktop/unzip/converted folder/'

os.chdir(path)


for file in os.listdir():
	if file.endswith(".txt"):
		file_path = f"{path}\{file}"
		read_text_file(file_path)

def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())
