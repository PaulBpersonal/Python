

import pandas as pd
import os
import glob


source="C:\\Users\\Paul\\Desktop\\unzip\\unzip folder"
dest="C:\\Users\\Paul\\Desktop\\unzip\\converted folder\\"
os.chdir(source)

for file in glob.glob("*.xls"):
       df = pd.read_excel(file)
       df.to_csv(dest+file+'.csv', index=False)
       os.remove(file)
for file in glob.glob("*.xlsx"):
       df = pd.read_excel(file)
       df.to_csv(dest+file+'.csv', index=False)
       os.remove(file)