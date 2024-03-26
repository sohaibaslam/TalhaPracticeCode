import os
import csv
import argparse
import sys



class FileReading:
    
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