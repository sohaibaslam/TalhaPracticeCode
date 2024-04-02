from weatherman import Weathermachine
from filehandling import FileReader
from output_printer import Printer

class WeatherMachineHandler:
    def __init__(self,folder_path,target_year,target_month) :
        self.folder_path = folder_path
        self.target_month = target_month
        self.target_year = target_year


    def data_for_a_year(self):

        weather_machine = Weathermachine() 
        file_reading = FileReader(self.folder_path)
        printer = Printer()

        files_with_year_month = file_reading.get_files_by_year_month(self.target_year, self.target_month)

        for file in files_with_year_month:
            data = file_reading.get_file_data(file)
            max_temp = weather_machine.get_maximum_temperature(data)
            min_temp = weather_machine.get_minimum_temperature(data)
            max_humidity = weather_machine.get_maximum_humidity(data)
            min_humidity = weather_machine.get_minimum_humidity(data)
            
            
            printer.print_max_temp(file, max_temp)
            printer.print_min_temp(file, min_temp)
            printer.print_max_humidity(file, max_humidity)
            printer.print_min_humidity(file,min_humidity)
            
    def data_for_a_month(self):
        

        weather_machine = Weathermachine() 
        file_reading = FileReader(self.folder_path)
        printer = Printer()

        files_with_year_month = file_reading.get_files_by_year_month(self.target_year, self.target_month)
        for file in files_with_year_month:
            data = file_reading.get_file_data(file)
            highest_avg_temp = weather_machine.get_highest_average_temperature(data)
            lowest_avg_temp = weather_machine.get_lowest_average_temperature(data)
            
            printer.print_highest_ave_temp(file,highest_avg_temp)
            printer.print_lowest_ave_temp(file,lowest_avg_temp)
