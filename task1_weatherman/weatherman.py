import os
import csv
import argparse
import sys




class Weathermachine:
    
    def __init__(self,folder_path):
        self.folder_path = folder_path
        
    def maximum_temperature(self,file_name):
        file_path = os.path.join(self.folder_path,file_name)
        max_temp = float('-inf')
        with open (file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                max = row.get('Max TemperatureC', '')
                if max and max.isdigit():
                    current_temp = int(max)
                    if current_temp > max_temp:
                        max_temp = current_temp
                        
        return max_temp

    def minimum_temperature(self,file_name):
        file_path = os.path.join(self.folder_path,file_name)
        min_temp = float('inf')
        with open (file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                min = row.get('Min TemperatureC', '')
                if min and min.isdigit():
                    current_temp = int(min)
                    if current_temp < min_temp:
                        min_temp = current_temp
                        
        return min_temp
    def humidity(self, file_name):
        file_path = os.path.join(self.folder_path, file_name)
        total_humidity = float('-inf')
        count = 0
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                min_humidity = row.get('Min Humidity', '')
                max_humidity = row.get('Max Humidity', '')
                mean_humidity = row.get('Mean Humidity', '')

                if min_humidity and max_humidity and mean_humidity:
                    total_humidity = ((int(mean_humidity) - int(min_humidity)) / (int(max_humidity) - int(min_humidity))) * 100
                    count += 1

        if count == 0:
            return 0

        avg_humidity = total_humidity / count
        return avg_humidity
    

    

    
        




        

    
