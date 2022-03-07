
import pandas as pd
import os
import glob


source='C:/Users/Paul/Desktop/Upload'
dest='C:/Users/Paul/Desktop/unzip/converted folder/'

os.chdir(source)

all_data = pd.DataFrame()
for file in glob.glob("*.xls*"):
       df = pd.read_excel(file)
       all_data = all_data.append(df,ignore_index=True)
all_data.to_csv("new_combined_file.csv")  