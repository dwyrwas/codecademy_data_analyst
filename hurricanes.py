# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def string_to_dollars(damages):
  damage_dollars = []
  for value in damages:
    if "M" in value:
      dollars = float(value[:-1])*conversion["M"]
      damage_dollars.append(dollars)
    elif "B" in value:
      dollars = float(value[:-1])*conversion["B"]
      damage_dollars.append(dollars)
    else:
      damage_dollars.append("Damages not recorded")
  return damage_dollars


# test function by updating damages
#damages = string_to_dollars(damages)
#print(damages)

# 2 
# Create a Table
def create_table_by_name(names=names, months=months, years=years, max_sustained_winds=max_sustained_winds, areas_affected=areas_affected, damages=damages, deaths=deaths):
  hurricanes = {}
  for i in range(0,len(names)):
    hurricanes[names[i]] = {'Name': names[i], 'Month':months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected':areas_affected[i], 'Damage': damages[i], 'Deaths':deaths[i]}
  return hurricanes
  

# Create and view the hurricanes dictionary
hurricane_table = create_table_by_name(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricane_table)
# 3
# Organizing by Year
def sort_table_by_year(table=hurricane_table):
  new_table = {} 
  storms = [x for x in hurricane_table.keys()]
  years = []
  for x in storms:
    years.append(table[x]['Year'])
  print(years)
  for year, storm in zip(years, storms):
    if year in new_table:
      new_table[year].append(hurricane_table[storm])
    else:
      new_table[year] = [hurricane_table[storm]]
  return new_table
# create a new dictionary of hurricanes with year and key

#print(sort_table_by_year())

# 4
# Counting Damaged Areas
def count_damaged_areas(table):
  areas = {}
  for storm, info in table.items():
    for area in info.get('Areas Affected'):
      if area in areas:
        areas[area] = areas[area] + 1
      else:
        areas[area] = 1   
  return areas
# create dictionary of areas to store the number of hurricanes involved in
damaged_areas = count_damaged_areas(hurricane_table)

# 5 
# Calculating Maximum Hurricane Count
def calc_most_affected(dictionary):
  area = max(dictionary, key=lambda key: dictionary[key])
  value = dictionary[area]
  return area, value  
# find most frequently affected area and the number of hurricanes involved in
#print(calc_most_affected(damaged_areas))

# 6
# Calculating the Deadliest Hurricane
def calculate_deadliest(table):
  storm_deaths = {}
  for storm, info in table.items():
    storm_deaths[storm] = info.get('Deaths')
  storm = max(storm_deaths, key=lambda key: storm_deaths[key])
  value = storm_deaths[storm] 
  return storm, value
# find highest mortality hurricane and the number of deaths
deadliest = calculate_deadliest(hurricane_table)
print(deadliest)
# 7
# Rating Hurricanes by Mortality
def calc_mortality(table):
  mort = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  storm_mortality = {}
  for storm, info in table.items():
    storm_mortality[storm] = info.get('Deaths')
  for storm, deaths in storm_mortality.items():
    if deaths == 0:
      mort[0].append(storm)
    elif deaths <= 100:
      mort[1].append(storm)
    elif deaths <= 500:
      mort[2].append(storm)
    elif deaths <= 1000:
      mort[3].append(storm)
    elif deaths <= 10000:
      mort[4].append(storm)
    else:
      mort[5].append(storm)
  return mort

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = calc_mortality(hurricane_table)
print(hurricanes_by_mortality)

# 8 Calculating Hurricane Maximum Damage
def calculate_most_damage(table):
  storm_damage = {}
  for storm, info in table.items():
    if info.get('Damage') != 'Damages not recorded':
      storm_damage[storm] = info.get('Damage')
  storm = max(storm_damage, key=lambda key: storm_damage[key])
  value = storm_damage[storm] 
  return storm, value
# find highest damage inducing hurricane and its total cost
most_damage = calculate_most_damage(hurricane_table)
print(most_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def calc_damages(table, damage_scale):
  conversion = {"M": 1000000, "B": 1000000000}
  sorted_by_damages = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  storm_damages = {}
  for storm, info in table.items():
    storm_damages[storm] = info.get('Damage')
  for storm, damages in storm_damages.items():
    if "M" in damages:
      damages = float(damages[:-1])*conversion["M"]
      storm_damages[storm] = damages
    elif "B" in damages:
      damages = float(damages[:-1])*conversion["B"]
      storm_damages[storm] = damages
  for storm, damages in storm_damages.items():    
    if damages != 'Damages not recorded':
      if damages == damage_scale[0]:
        sorted_by_damages[0].append(storm)
      elif damages <= damage_scale[1]:
        sorted_by_damages[1].append(storm)
      elif damages <= damage_scale[2]:
        sorted_by_damages[2].append(storm)
      elif damages <= damage_scale[3]:
        sorted_by_damages[3].append(storm)
      elif damages <= damage_scale[4]:
        sorted_by_damages[4].append(storm)
      else:
        sorted_by_damages[5].append(storm)
  return sorted_by_damages

dmg = calc_damages(hurricane_table, damage_scale)
print(dmg)
