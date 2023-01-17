from archive import file
from utils import functions

data= file.extracting_data("./archive/data.csv")
country = input("Ingres el pais a buscar=> ")
result = functions.find_country(country,data)


    
    