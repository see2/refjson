# python version 3.6
# Refwork file to json(dict) -> json/dataframe

# dependent package: 

# * Refdict with one file
# * RefBatch Deal with one zip file with multiple files
import json
import re
import os

import psutil # see the used memory

# see the memory used by python
#def used_memory(self):
#    process = psutil.Process(os.getpid())
#    print( "Your python cost {} MB memory".format(process.memory_info().rss/1000000) )  # in MB
class RefJson:
    def __init__(self, text):

        self.dict = self.to_dict(text)

    
    def to_dict(self,text):
        # print(text)
        paperlist= re.split('\r\n\r\n\r\n', text)    
        # package the text file into json

        # constant parameter for paper loop 
        papercount=1   # every paper one count
        paperdict={}     # every paper one js file 
        for paper in paperlist:

            paperinfo= re.split(r'\r\n', paper)    



            # constant parameter for var loop
            varcount=1     # every variance for paper for one count
            variance=""
            value=""    
            content = {}     # content of the json
            for var in paperinfo:

                var_search = re.search( r'(^[A-Z]\w) (.*)' ,var) 

                if var_search: # if have a key, then add the value

                    variance = var_search.group(1)
                    value = var_search.group(2)        

                    content[variance] = value

                else: # if don't have a key, then don't 

                    value = value + var
                    content[variance] = value 
            
            paperdict[papercount] = content 
            papercount+=1
        return paperdict