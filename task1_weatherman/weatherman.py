
class Weathermachine:
    
           
    def get_maximum_temperature(self,data):
        max_temp_values = data['Max TemperatureC']
        max_temp_values = [int(temp) for temp in max_temp_values if temp]
        max_temp = max(max_temp_values)                
        return max_temp

    def get_minimum_temperature(self,data):
        min_temp_values = data['Min TemperatureC']
        min_temp_values = [int(temp) for temp in min_temp_values if temp]
        min_temp = min(min_temp_values)                
        return min_temp
    
    def get_humidity(self, data):
        max_humidity_values = data['Max Humidity']
        max_humidity_values = [int(temp) for temp in max_humidity_values if temp]
        max_humidity = max(max_humidity_values)                
        return max_humidity
    

    

    
        




        

    
