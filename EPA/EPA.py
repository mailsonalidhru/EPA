##### Import Libraries Section #####
import pprint 
from collections import defaultdict

##### Functions Declaration Section #####

#Function takes in raw data, eliminates empty row(s) and header 
def filterRows(rawData):
    #Get Rows/Data in a list
    rows = rawData.split('\n')
    filteredData = []
    for row in rows:
        #join - takes care of empty rows like ',,,,,,,'
        if (''.join(row.split(',')).strip() != '') and row:
            # If Row is NOT empty
            #Split each Row into columns and create a new list
            ln = row.split(",")
            filteredData.append(ln)
    
    # Remove the Header
    filteredData = filteredData[1:len(filteredData)]
    return filteredData

##### Variables Initialization #####
dictOfSites = {}
dictOfParameter = defaultdict(list)
dictOfAQSCodes = defaultdict(list)

##### Processing Section #####

# Read Data 
fopen = open("C:\\Personal\\air-quality\\epa_air_quality_annual_summary.csv", "r")
data = fopen.read()

# Filter Data
arrFileContents = filterRows(data)

# For every row
for rec in arrFileContents:
    #### Average of Pollutant PM2.5 Yearly for every State and County 
    # 13 Year, 8 Parameter Name, 27 Mean Value, 51 State Name, 52 County Name
    # Data Structure: Dictionary [Year]:[[Avg, Pollutant, County, State],[Avg, Pollutant, County, State]]
    if (rec[8].find("PM2.5") != -1):
        # For Key [Year], List of Values of [Average, Pollutant, County, State]
        dictOfParameter[rec[13]].append([rec[8], rec[27], rec[52] + " " + rec[51]])
        # Append only Unique List of [Average, Pollutant, County, State]
       # unique_data = [list(x) for x in set(tuple(x) for x in dictOfParameter[rec[13]])]
       # dictOfParameter[rec[13]] = unique_data

    #### Calculate Air Quality Sites near SFO, California 
    # 5 Latitude, 6 Longitude, 48 Site Name, 49 Address
    # Data Structure: Dictionary [SiteName]:[Address]
    try:
        latitude = float(rec[5]) # SFO Latitude = 37.765946
        longitude = float(rec[6]) # SFO Longitude = -122.399044
        if(latitude >= 37 and latitude <= 38) and (longitude <= -121 and longitude >= -123):
            if rec[48] not in dictOfSites:
                dictOfSites[rec[48]] = rec[49]
    except ValueError:
        pass
    
    #### Pollutants Measured every Year 
    # Data Structure: Dictionary [Year]:[<Pollutant 1>, <Pollutant 2>, <Pollutant 3>....N]
    if rec[13] not in dictOfAQSCodes:
        dictOfAQSCodes[rec[13]].append(rec[8])
    else:
        if(dictOfAQSCodes[rec[13]].count(rec[8])) == 0:
            #If the Pollutant is not in list append
            dictOfAQSCodes[rec[13]].append(rec[8])

print ("\n ##### Air Quality Sites near SFO, California ##### ")
pprint.pprint(dictOfSites)

print ("\n ##### City / State with Pollutant PM2.5 year wise ##### ")
pprint.pprint(dictOfParameter)

print ("\n ##### Pollutants Measured every Year ##### ")
pprint.pprint(dictOfAQSCodes)
