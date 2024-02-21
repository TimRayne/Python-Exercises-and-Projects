#Day_name  Day_number  Month_name  Year
from datetime import *

given_date = datetime(2020, 2, 25)

formatted_date = given_date.strftime('%A %d %B %Y')

print(formatted_date)


