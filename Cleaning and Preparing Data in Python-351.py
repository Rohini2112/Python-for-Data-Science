## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)
print(num_rows)

## 2. Reading our MoMA Dataset ##

opened_file = open('artworks.csv')
from csv import reader
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]
print(moma)

## 3. Replacing Substrings with the Replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace('one', 'two')
print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

for column in moma:
    nationality = column[2]
    gender = column[5]
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    column[2] = nationality
    column[5] = gender
    
    
    print(column[5])

## 5. String Capitalization ##

for row in moma:
    
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender

    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality
    
print(row[5])

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    if date != "":
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    begin_date = row[3]
    end_date = row[4]
    cleaned_begindate= clean_and_convert(begin_date)
    cleaned_enddate = clean_and_convert(end_date)
    row[3] = cleaned_begindate
    row[4] = cleaned_enddate
    

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")
    return string

stripped_test_data = []
for char in test_data:
    char = strip_characters(char)
    stripped_test_data.append(char)
    
print(stripped_test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(string):
    if '-' in string:
        string = string.split("-")
        string= (int(string[0])+int(string[1]))/2
        string = round(string)
    else:
        string = int(string)
    return string

processed_test_data = []
for date in stripped_test_data:
    date = process_date(date)
    processed_test_data.append(date)
    
print(processed_test_data)

for row in moma:
    date = row[6]
    striped_data = strip_characters(date)
    processed_date = process_date(striped_data)
    row[6] = processed_date
    
print(processed_date)