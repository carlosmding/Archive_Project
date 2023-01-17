def find_country(country_to_find, data):
  result = list(filter(lambda country : country["Country/Territory"] == country_to_find, data))
  return result

def find_labels_values(country):
  print(country)
  result = {
    '2022' : int(country['2022 Population']),
    '2020' : int(country['2020 Population']),
    '2015' : int(country['2015 Population']),
    '2010' : int(country['2010 Population']),
    '2000' : int(country['2000 Population']),
    '1990' : int(country['1990 Population']),
    '1980' : int(country['1980 Population']),
    '1970' : int(country['1970 Population']),
  }
  return result.keys(), result.values()

def create_data_percentage(data):
  countries=[]
  percentage =[]
  for country in data:
    countries.append(country["Country/Territory"])
    percentage.append(country["World Population Percentage"])
  return countries, percentage
