import zipfile
import argparse
import sys

def extract_data(filename):
    with zipfile.ZipFile(filename, 'r') as z:
        z.extractall('weatherman')
     
def read_data(filename):
    data = []
    
    with open(filename,'r') as f:
        header = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            entry = dict(zip(header, values))
            data.append(entry)
            
    return data


def max_temp(file_data):
    max_temp = float('-inf') 
    for entry in file_data:
        max_temp_entry = entry.get('Max TemperatureC', '')
        
        if max_temp_entry and max_temp_entry.isdigit():
            current_temp = int(max_temp_entry)
            if current_temp > max_temp:
                max_temp = current_temp

    return max_temp

def min_temp(file_data):
    min_temp = float('inf') 
    for entry in file_data:
        min_temp_entry = entry.get('Min TemperatureC', '')
        
        if min_temp_entry and min_temp_entry.isdigit():
            current_temp = int(min_temp_entry)
            if current_temp < min_temp:
                min_temp = current_temp
                
    return min_temp
    
filename = 'Murree_weather_2004_Aug.txt'
file_data = read_data(filename)
  
def data(args):
    
    if args.e:
       print(f"max temp is {max_temp(file_data)} \nmin temp is {min_temp(file_data)}") 
               
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--e', type=int, default=2002, help='Enter year for highest temp, lowest temp and humidity')
    args = parser.parse_args()
    sys.stdout.write(str(data(args)))
    
    
    
    
