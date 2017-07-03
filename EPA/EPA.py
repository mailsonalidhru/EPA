import pprint

def filterRows(rawData):
    #Get Rows/Data in a list
    rows = rawData.split('\n')

    filteredData = []
    for row in rows:
        # If Row is NOT empty
        if row:
            #Split each Row into columns and create a new list
            ln = row.split(",")
            filteredData.append(ln)
    
    # Remove the Header
    filteredData = filteredData[1:len(filteredData)]
    return filteredData

############### File Open ####################
#fopen = open("C:\Personal\EPA\EPA1.csv", "r") Th
fopen = open("C:\\Personal\\air-quality\\epa_air_quality_annual_summary.csv", "r")
data = fopen.read()

# Get rid of Header & Empty rows
arrFileContents = filterRows(data)

# Get list of Distinct Sites
dictOfSites = {}
dictOfParameter = {}
for rec in arrFileContents:
    #Ignore Empty Rows like ['']
    if(len(rec) != 1):
        ##################################### Air Quality Sites near SFO, California #############################################
        # 37.765946	-122.399044 -> SFO
        try:
            latitude = float(rec[5])#rec[2])
            longitude = float(rec[6])#3])
            # replace with 49
            if(latitude >= 37 and latitude <= 38) and (longitude <= -121 and longitude >= -123):
                if rec[48] not in dictOfSites: #(45 + 3)
                    dictOfSites[rec[48]] = rec[49]
        except ValueError:
            pass
        ##################################### City / State with Pollutant PM2.5 year wise #########################################
        if rec[13] + "," + rec[8] + "," + rec[52] not in dictOfParameter:
            #print(rec[8])
            if (rec[8].find("PM2.5") != -1):
                dictOfParameter[rec[13] + "," + rec[8] + "," + rec[52]] = rec[51]  + ", " +  rec[27]
        
        if (rec[8].find("PM2.5") != -1):
            dictOfParameter[rec[13] + "," + rec[8] + "," + rec[52]] = rec[51]  + ", " +  rec[27]


print ("\n ################ Air Quality Sites near SFO, California ##############################")
pprint.pprint(dictOfSites)
        
print ("\n ################ City / State with Pollutant PM2.5 year wise ##############################")
pprint.pprint(dictOfParameter)





