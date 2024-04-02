class Weathermachine:
           
    def get_maximum_temperature(self,data):
        max_temp_values = data['Max TemperatureC']
        max_temp_values = [temp for temp in max_temp_values if temp]
        max_temp = max(max_temp_values)                
        return max_temp

    def get_minimum_temperature(self,data):
        min_temp_values = data['Min TemperatureC']
        min_temp_values = [temp for temp in min_temp_values if temp]
        min_temp = min(min_temp_values)                
        return min_temp
    
    def get_maximum_humidity(self, data):
        max_humidity_values = data['Max Humidity']
        max_humidity_values = [temp for temp in max_humidity_values if temp]
        max_humidity = max(max_humidity_values)                
        return max_humidity

    def get_minimum_humidity(self, data):
        min_humidity_values = data[' Min Humidity']
        min_humidity_values = [temp for temp in min_humidity_values if temp]
        min_humidity = min(min_humidity_values)                
        return min_humidity
    
    def get_highest_average_temperature(self, data):
        max_temp_values = data['Max TemperatureC']
        max_temp_values = [temp for temp in max_temp_values if temp]
        highest_avg_temp_value = sum(max_temp_values)//len(max_temp_values)
        return highest_avg_temp_value
        
    def get_lowest_average_temperature(self, data):
        min_temp_values = data['Min TemperatureC']
        min_temp_values = [temp for temp in min_temp_values if temp]
        lowest_avg_temp_value = sum(min_temp_values)//len(min_temp_values)
        return lowest_avg_temp_value