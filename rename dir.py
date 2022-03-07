from pathlib import Path
from datetime import datetime
import os


source='C:/Users/Paul/Desktop/Open'
dest='C:/Users/Paul/Desktop/unzip/converted folder/'

os.chdir(source)

our_files = Path(source)

for file in our_files.iterdir():
    if file.is_file() and file.stem != ".DS_Store":
        directory = file.parent #directory folder
        extension = file.suffix #file type
        old_name = file.stem #file name
        dir= os.path.abspath(file)
        os.rename(dir,dir[:-4]+".txt")
        #print(directory)
        #print(extension)
        #print(old_name)
        #print(dir)
        # can use this to split files into variables: region, report_type, old_date = old_name.split('-')


        # 3) Change date format and label the new file
        #old_date = datetime.strptime(old_date, "%Y%b%d")
        #date = datetime.strftime(old_date, '%Y-%m-%d')
        #new_file = f'{date} - {region} - {report_type}{extension}'

        # 4) Calculate the month and create a new path with it
        #month = datetime.strftime(old_date, "%B")
        #new_path = our_files.joinpath(month)

        # 5) Check if the folder exists. If not, create it
        #if not new_path.exists():
        #    new_path.mkdir()

        # 6) Create a new path in the new directory
        #new_file_path = new_path.joinpath(new_file)

        # 7) Move the files
       # file.replace(new_file_path)