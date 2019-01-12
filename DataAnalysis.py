'''Load the Sample DataSet of the CSV File via PANDAS
'''

#Importing Pandas Library for Importing the Data Set
import pandas as pd
import os


class DataLoad:
    """Class to load the data
    """

    def __init__(self, url="dataset\\data.csv"):
        """This is the default constructor of the class Dataload,
        which helps in pulling up the dataset on the basis of
        provided URL
        
        Arguments:
            url {string} -- This expects a url string which will load the data set (default: {""})
        """       
        
        self.url = url


    def get_data_set(self):
        """This is the implementation logic of pandas for retreiving the dataset
        """
        if not self.url:
            path=os.path.join(os.path.dirname(__file__),self.url)
        else:
            path=self.url
            
        data_frame_result = pd.read_csv(r""+path)
        return data_frame_result


data_load=DataLoad()
print(data_load.get_data_set())

