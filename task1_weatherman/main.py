
from weatherman import Weathermachine
from filehandling import FileReader
import argparse
import sys



folder_path = "weatherfiles"
target_year = 2006
target_month = 8

weather_machine = Weathermachine() 
file_reading = FileReader(folder_path)

files_with_year_month = file_reading.get_files_by_year_month(target_year, target_month)

def data_for_a_year():
    for file in files_with_year_month:
        data = file_reading.get_file_data(file)
        max_temp = weather_machine.get_maximum_temperature(data)
        print(f"Maximum temperature for {file} is {max_temp}")    

    for file in files_with_year_month:
        data = file_reading.get_file_data(file)
        min_temp = weather_machine.get_minimum_temperature(data)
        print(f"Minimum temperature for {file} is {min_temp}")

    for file in files_with_year_month:
        data = file_reading.get_file_data(file)
        max_humidity = weather_machine.get_humidity(data)
        print(f"Maximum Humidity for {file} is {max_humidity}")

def processed_time_interval_data(args):
    if args.e:
        return data_for_a_year()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--e', type=int, default=2002, help='Enter year for highest temp, lowest temp and humidity')
    args = parser.parse_args()
    msg = sys.stdout.write(str(processed_time_interval_data(args)))
