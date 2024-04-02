
from weathermachine_handler import WeatherMachineHandler
import argparse
import sys



folder_path = "weatherfiles"
target_year = 2006
target_month = 8


weather = WeatherMachineHandler(folder_path,target_year,target_month)

def processed_time_interval_data(args):
    if args.e:
        return weather.data_for_a_year()
    elif args.a:
        return weather.data_for_a_month()
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--e', type=int, default=2002, help='Enter year for highest temp, lowest temp and humidity')
    parser.add_argument('--a', type=int, default=2005/6, help='Enter year and then add a "/" and then enter month for highest average temp, lowest average temp and humidity')
    args = parser.parse_args()
    msg = sys.stdout.write(str(processed_time_interval_data(args)))
