import os
import csv

class Weathermachine:
    
    def __init__(self,folder_path):
        self.folder_path = folder_path
    
    
    
    def get_files_by_year_month(self, target_year, target_month):
        file_name_with_year_month = []
        all_items = os.listdir(self.folder_path)
        for item in all_items:
            if os.path.isfile(os.path.join(self.folder_path,item)):
                if self.has_year_month_in_pkt(os.path.join(self.folder_path,item),target_year,target_month):
                    file_name_with_year_month.append(item)
        return file_name_with_year_month


    def has_year_month_in_pkt(self, file_path,target_year, target_month):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pkt_date_parts = row.get('PKT', '').split('-')
                if len(pkt_date_parts) == 3:
                    year, month, date = pkt_date_parts
                    if year == str(target_year) and month == str(target_month):
                        return True
        
            return False
    

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
        



        
folder_path = "weatherfiles"
target_year = 2006
target_month = 8

weather_machine = Weathermachine(folder_path)

files_with_year_month = weather_machine.get_files_by_year_month(target_year,target_month)


for file_name in files_with_year_month:
    max_temp = weather_machine.maximum_temperature(file_name)
    print(f"Maximum temperature for {file_name} is {max_temp}")

for file_name in files_with_year_month:
    min_temp = weather_machine.minimum_temperature(file_name)
    print(f"Minimum temperature for {file_name} is {min_temp}")
    
for file_name in files_with_year_month:
    humidity_percentage = weather_machine.humidity(file_name)
    print(f"humidity for {file_name} is {humidity_percentage: .2f}%")