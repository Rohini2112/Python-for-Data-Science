## 1. Reading the MoMA Dataset ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date
    
print(row[6])

## 2. Calculating Artist Ages ##

ages = []

for row in moma:
    date = row[6]
    birth = row[3]
    
    if type(birth) == int:
        age = date - birth
    
    else:
        age = 0

    ages.append(age)

final_ages = []

for age in ages:
    
    if age > 20:
        final_age = age
        
    else:
        final_age = "Unknown"
        
    final_ages.append(final_age)

print(final_ages)
        

## 3. Converting Ages to Decades ##

decades = []

for age in final_ages:
    if age == "Unknown":
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + "0s"
        
    decades.append(decade)
print(decades)
        

## 4. Summarizing the Decade Data ##

decade_frequency = {}
for age in decades:
    if age in decade_frequency:
        decade_frequency[age] += 1
    else:
        decade_frequency[age] = 1
        
print(decade_frequency)

## 5. Inserting Variables into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

output = "{name}'s birth year is {year}".format(name = artist, year = birth_year)

print(output)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}

for row in moma:
    name = row[1]
    if name in artist_freq:
        artist_freq[name] +=1
    else:
        artist_freq[name] = 1
        
print(artist_freq)

## 7. Creating an Artist Summary Function ##

def artist_summary(name):
    num_artworks = artist_freq[name]
    output = "There are {number} artworks by {artist} in the data set".format(number = num_artworks, artist = name)
    return output

final = artist_summary("Henri Matisse")
print(final)

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {} is {:,.2f} million"

for c in pop_millions:
    name = c[0]
    population = c[1]
    output = template.format(name, population)
    print(output)

## 9. Challenge: Summarizing Artwork Gender Data ##

freq_gender = {}

for row in moma:
    gender = row[5]
    
    if gender in freq_gender:
        freq_gender[gender] += 1
    else:
        freq_gender[gender] = 1

for gender,artworks in freq_gender.items():
    output = "There are {a:,} artworks by {g} artists".format(a=             artworks, g = gender )
    print(output)
    
    