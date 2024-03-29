## 1. Introduction ##

from csv import reader
opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus= potus[1:]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt
ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)
print(ibm_founded)
print(man_on_moon)

## 5. Using Strptime to Parse Strings as Dates ##

date_format = "%m/%d/%y  %H:%M"

for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date,date_format)
    row[2] = start_date

print(row[2])
     
        

## 6. Using Strftime to Format Dates ##

visitors_per_month = {}

for row in potus:
    dt_object = row[2]
    dt_string = dt_object.strftime("%B, %Y")
    if dt_string in visitors_per_month:
        visitors_per_month[dt_string] += 1
    else:
        visitors_per_month[dt_string] = 1
        
print(visitors_per_month)

## 7. The Time Class ##

appt_times = []

for row in potus:
    date_time = row[2]
    time_obj = date_time.time()
    appt_times.append(time_obj)
print(appt_times)

## 8. Comparing Time Objects ##

min_time = min(appt_times)
max_time = max(appt_times)
print(min_time)
print(max_time)

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days = 56)
answer_3 = dt_4 - dt.timedelta(seconds = 3600)

print(answer_1)
print(answer_2)
print(answer_3)

## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
appt_lengths = {}
for row in potus:
    start_date = row[2]
    end_date = row[3]
    length = end_date - start_date
    
    if length in appt_lengths:
        appt_lengths[length] += 1
    else:
        appt_lengths[length] = 1
        
min_length = min(appt_lengths)
print(min_length)
max_length = max(appt_lengths)
print(max_length)