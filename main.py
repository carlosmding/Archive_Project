from archive import file
from utils import functions, charts

data= file.extracting_data("./archive/data.csv")

"""country = input("Type the country => ").title()
result = functions.find_country(country,data)
try: 
  labels, values = functions.find_labels_values(result[0])
except IndexError:
  print("We can´t find the country, please try again")
charts.generate_bar_chart(labels, values)
"""
labels_pie, values_pie = functions.create_data_percentage(data)
charts.generate_pie_chart(labels_pie, values_pie)



    
    