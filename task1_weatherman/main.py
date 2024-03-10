from practice import Weathermachine
import argparse
import sys
import os



folder_path = "weatherfiles"
target_year = 2006
target_month = 8

weather_machine = Weathermachine(folder_path)

files_with_year_month = weather_machine.get_files_by_year_month(target_year,target_month)

def year():
    for file_name in files_with_year_month:
        max_temp = weather_machine.maximum_temperature(file_name)
        print(f"Maximum temperature for {file_name} is {max_temp}")

    for file_name in files_with_year_month:
        min_temp = weather_machine.minimum_temperature(file_name)
        print(f"Minimum temperature for {file_name} is {min_temp}")
        
    for file_name in files_with_year_month:
        humidity_percentage = weather_machine.humidity(file_name)
        print(f"humidity for {file_name} is {humidity_percentage: .2f}%")

def data(args):
    
    if args.e:
       return year()

       

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--e', type=int, default=2002, help='Enter year for highest temp, lowest temp and humidity')
    args = parser.parse_args()
    msg = sys.stdout.write(str(data(args)))
