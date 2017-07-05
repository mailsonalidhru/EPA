# Environmental Protection Agency(EPA) - Measures Air Quality from monitors located across the country. 
This Data contains the value measured for the different pollutants at various sites

DataSet: epa_air_quality_annual_summary.csv
1) Python Program
2) Reads Data File "epa_air_quality_annual_summary.csv"
3) Derives:
    - Air Quality Sites near SFO, California
        Data Structure: Dictionary [SiteName]:[Address]
    - Pollutant PM2.5 value, Year, City / State
        Data Structure: Dictionary [Year]:[[Avg, Pollutant, County, State],[Avg, Pollutant, County, State]]
    - Pollutants measured every Year
        Data Structure: Dictionary [Year]:[<Pollutant 1>, <Pollutant 2>, <Pollutant 3>....N]
