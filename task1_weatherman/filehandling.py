import os
import csv
from datetime import datetime

class FileReader:
    
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


    def has_year_month_in_pkt(self, file_path, target_year, target_month):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pkt_date = row.get('PKT', '')
                if pkt_date:
                    pkt_date = datetime.strptime(pkt_date, '%Y-%m-%d')
                    if pkt_date.year == target_year and pkt_date.month == target_month:
                        return True
        return False

    def get_file_data (self,file_name):
        file_path = os.path.join(self.folder_path,file_name)
        data = {}
        
        with open (file_path,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key,values in row.items():
                    if key not in data:
                        data[key] = []
                    data[key].append(values)
                    
        return data