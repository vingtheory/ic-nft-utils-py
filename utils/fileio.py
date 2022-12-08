import csv
import json
import pickle

class FileIO:
    def writeToCSV(fileName, list):
        with open(fileName, 'w') as f:
            # using csv.writer method from CSV package
            csv_writer = csv.writer(f)
            count = 0
            for item in list:
                if count == 0:
                    # Writing headers of CSV file
                    header = item.keys()
                    csv_writer.writerow(header)
                    count += 1
                
                # Writing data of CSV file
                csv_writer.writerow(item.values())
    
    def writeToJSON(fileName, data):
        with open(fileName + '.json', 'w') as file:
            # Writing data of CSV file
            json.dump(data, file)

    def readFromJSON(fileName):
        with open(fileName + '.json', 'rb') as file:
            # Writing data of CSV file
            return json.load(file)

    def writeToPickle(fileName, data):
        with open(fileName + '.pkl', 'wb') as file:
            # Writing data of CSV file
            pickle.dump(data, file)  

    def readFromPickle(fileName):
        with open(fileName + '.pkl', 'rb') as file:
            # Writing data of CSV file
            return pickle.load(file)
  
                     
    