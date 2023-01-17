import csv

def extracting_data(path):
  with open(path,"r") as archive:
    reader = csv.reader(archive, delimiter=",")
    header = next(reader)
    data = []
    for line in reader:
      iterator = zip(header, line)
      country_dict = {key:value for key, value in iterator}
      data.append(country_dict)
  return data

