import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format. 

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")
        
    
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius and make it a float. 

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    degrees_c = (float(temp_in_farenheit) - 32)/1.8
    return round(degrees_c, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0
    for n in weather_data:
        sum = sum + float(n)
    return sum/len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.
            
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter = ',')
        next(reader)
        result = []
        for row in reader: 
            if len(row) > 0:
                result.append([row[0],int(row[1]), int(row[2])]) 
        return(result)
    

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0:
        return ()
    min = None
    pos = 0
    for i in range(0,len(weather_data)):
        n = float(weather_data[i])
        if i == 0 or n <= min:
            min = n
            pos = i
    return (min, pos)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0:
        return ()
    max = None
    pos = 0
    for i in range(0,len(weather_data)):
        n = float(weather_data[i])
        if i == 0 or n >= max:
            max = n
            pos = i
    return (max, pos)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    def temperatures(index):
        temperatures = []
        for row in weather_data:
            temperatures.append(row[index])
        return temperatures
    
    min_temps = temperatures(1)
    max_temps = temperatures(2)   
    min = find_min(min_temps)
    max = find_max(max_temps) 
    
    days = len(weather_data)
    return f"{days} Day Overview\n" + \
        f"  The lowest temperature will be {convert_f_to_c(min[0])}°C, and will occur on {convert_date(weather_data[min[1]][0])}.\n" + \
        f"  The highest temperature will be {convert_f_to_c(max[0])}°C, and will occur on {convert_date(weather_data[max[1]][0])}.\n" + \
        f"  The average low this week is {convert_f_to_c(calculate_mean(min_temps))}°C.\n" + \
        f"  The average high this week is {convert_f_to_c(calculate_mean(max_temps))}°C.\n"
 

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
