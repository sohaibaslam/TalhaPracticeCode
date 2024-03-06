import os
import csv



def get_files_by_year_month(folder_path, target_year, target_month):
    file_name_with_year_month = []
    all_items = os.listdir(folder_path)
    for item in all_items:
        if os.path.isfile(os.path.join(folder_path,item)):
            if has_year_month_in_pkt(os.path.join(folder_path,item),target_year,target_month):
                file_name_with_year_month.append(item)
    return file_name_with_year_month


def has_year_month_in_pkt(folder_path, target_year, target_month):
    with open(folder_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pkt_date_parts = row.get('PKT','').split('-')
            if len(pkt_date_parts) == 3:
                year, month, date = pkt_date_parts
                if year == str(target_year) and month == str(target_month):
                    return True
    return False  

def maximum_temperature(file_name):
    file_path = os.path.join(os.getcwd(),file_name)
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

def minimum_temperature(file_name):
    file_path = os.path.join(os.getcwd(),file_name)
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

        
folder_path = "weatherfiles"
target_year = 2004   
target_month = 8

files_with_year_month = get_files_by_year_month(folder_path,target_year,target_month)


for file_name in files_with_year_month:
    max_temp = maximum_temperature(file_name)
    print(f"Maximum temperature is {file_name} : {max_temp}")

for file_name in files_with_year_month:
    min_temp = minimum_temperature(file_name)
    print(f"Minimum temperature is {file_name} : {min_temp}")