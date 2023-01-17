def find_country(country_to_find, data):
  result = list(filter(lambda country : country["Country/Territory"] == country_to_find, data))
  return result

def find_labels_values(country):
  