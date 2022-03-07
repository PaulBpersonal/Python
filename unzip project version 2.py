import os, zipfile

# unzip folder selected
source='C:/Users/Paul/Desktop/unzip/unzip folder'
dest='C:/Users/Paul/Desktop/unzip/converted folder/'

os.chdir(source)

dir_name = source
extension = ".zip"
extension2 = ".csv"

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name, pwd=bytes('Brc_56@HAS', 'utf-8')) # extract file to dir
        zip_ref.close() # close file
        formal_name = item.stem #file name

        print(directory)
        print(extension)
        print(old_name)
        # can use this to split files into variables: region, report_type, old_date = old_name.split('-')

        
        dates = file_name[-10:-4]
        os.remove(file_name) # delete zipped file
        for item in os.listdir(dir_name):
            if item.endswith(extension2):
                files = os.path.abspath(item)
                os.rename(files,files[:-4]+dates+".csv")
     