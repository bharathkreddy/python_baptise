# %%
# NATIVELY EVERY TIME AND DATE IS MEASURED AS SECONDS SINCE EPOC
import time

# Gives seconds since epoch (time from 1st Jan 1970)
time.time()


#converts epoch time to timestruc objectect
time.gmtime(time.time())


# Formats timestruc to string.
time.strftime('%Y-%m-%d %H:%M:%S T-%z(%Z)', time.gmtime(time.time()))


#Parces string to timestruc
s = "12/21/2023 11:07:02 PM"
time.strptime(s, '%m/%d/%Y %H:%M:%S %p')


# converts timestuc to epoch
from calendar import timegm
timegm(time.strptime(s, '%m/%d/%Y %H:%M:%S %p'))

# %%
# DATETIME MODULE ABSTRACTS AWAY EPOCT TIME ETC.

import datetime

# Returns a datetime object
dt = datetime.date(2023, 1, 26)
print(dt, type(dt))


# Returns today in local time not UTC
dt = datetime.datetime.today()
print(dt)


# Convert to and from ISO formated strings
print(datetime.date.fromisoformat('2023-01-26'))
dt = datetime.date(2023, 1, 26)
print(dt.isoformat())
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday())


# Time object in datetime module
t = datetime.time(15, 30, 45, 135)
print(t) 
# time has to be provided in 24 hour clock format and microseconds have to be either 3 or 6 digits

t = datetime.time.fromisoformat('13:30:45.123')
print(t, type(t))


#time object has many properties, tzinfo returns None if no timezone info is available.
print(t.hour, t.minute, t.second, t.microsecond, t.tzinfo)


# Datetime object in datetime module
dt = datetime.datetime(2020, 3, 1, 13, 30, 45, 123)
print(dt, type(dt))

print(dt.isocalendar())
print(dt.isoformat())


# from iso format to sting
print(datetime.datetime.fromisoformat('2020-02-15T04:30:15'))


# local time & UTC time
print(datetime.datetime.now())
print(datetime.datetime.now(datetime.UTC))


# Working with Time Zones
s = "2020-04-02T18:30:30+05:30" # 5 and half hours ahead of UTC
dt = datetime.datetime.fromisoformat(s)
print(dt)
print(dt.timetz())

s = "2020-04-02T18:30:30-07:00" # 7 hours before of UTC
dt = datetime.datetime.fromisoformat(s)
dt

# %%
# TIME DETAL OBJECTS 

dt1 = datetime.datetime.now()
dt2 = datetime.datetime.fromisoformat('2023-12-21T00:00:00')
td = dt1 - dt2
print(repr(td))

# To get total seconds we can calculate by below two methods
td_secs = td.days * 24 * 60 * 60 + td.seconds + td.microseconds / (10 ** 6)
td_secs_2 = td.total_seconds()
print(td_secs, td_secs_2)

# Creating time deltas
td = datetime.timedelta(hours=1, minutes=3)
print(repr(td))


# add time delta to a datetime object
dt = datetime.datetime.now()
print(dt, dt-td)


# how to find last day of a month from a string 
s = '2020-02-13T13:35:00'
# step1: convert to date time and extract date object
dt = datetime.datetime.fromisoformat(s)
start_dt = datetime.date(year=dt.year, month=dt.month, day=dt.day)
print(dt, start_dt)
# Create 1st of next month from this date by adding time delta of 1 month

if start_dt.month == 12:
    new_year = start_dt.year + 1
    new_month = 1
else:
    new_year = start_dt.year
    new_month = start_dt.month + 1

new_dt = datetime.date(year=new_year, month=new_month, day=1)
print(new_dt)
# Subtract time delta of a day from this and let python figure out if prev month was leap year feb etc.
last_month_day = new_dt - datetime.timedelta(days=1)
print(last_month_day)

# %%
# WORKING WITH TIME ZONES
# Note1: UTC is not a timezone, its a standard (hence it doesnt have a notion of day light saving)
# GMT is UTC + 0 and every other tz is a timedelta from UTC (these have a notion of DLS)
# Allways work on UTC (tz naive) and let client app deal with tz awareness

s = "2020-03-15T13:30:00-07:00"
repr(datetime.datetime.fromisoformat(s))

#Take the timedetla from above and see how many hours in that
td = datetime.timedelta(days=-1, seconds=61200)
print(td.total_seconds() / 60 / 60)


# Creating a timezone (takes 2 parameters, time delta and name of tz)
tz_BRK = datetime.timezone(datetime.timedelta(hours=+5, minutes=+30), "BRK")
repr(tz_BRK)
# We can cross verify if time delta in tz_BRK is 5.5 hrs ahead.
print(datetime.timedelta(seconds=19800).total_seconds() /60 /60 )
# create a datetime object with this new tz
dt_BRK = datetime.datetime(year=2023, month=12, day=22, hour=18, minute=42 , tzinfo=tz_BRK)
print(dt_BRK)


# Convert to a new timezome.
## astimezone is a method available on tz aware datetime objects.
## .utc is a native timezones available in datetime module
print(dt_BRK.astimezone(datetime.timezone.utc))


# Convert now in UTC to India time.
tz_IND = datetime.timezone(datetime.timedelta(hours=5, minutes=30), 'tz_IND')

print(
    f'Time now in UTC: {datetime.datetime.now(datetime.UTC)}\n' \
    f'Time in India: {datetime.datetime.now(datetime.UTC).astimezone(tz_IND)}\n' \
    f'Time Locally: {datetime.datetime.now()}\n'
    )


# Stripping out the TimeZone information
# method .replace can be used to change anything , hour, day etc even tzinfo. 
dt_utc = datetime.datetime.now(datetime.UTC)
dt_utc_modified = dt_utc.replace(tzinfo=None)
print (repr(dt_utc), repr(dt_utc_modified))


# take a tz aware datetime and get UTC Date
s = "2020-05-15T13:30:00-04:00"

dt_aware = datetime.datetime.fromisoformat(s)
print(repr(dt_aware))

dt_utc_aware = dt_aware.astimezone(datetime.UTC)
print(repr(dt_utc_aware))

dt_utc = dt_utc_aware.replace(tzinfo=None)
print(repr(dt_utc))


# CONVERSION TO AND FROM STRINGS
t = datetime.time(22, 30, 45)
print(repr(t))

print(t.strftime('Time is : %I hours, %M mins, and %S secs, %p'))

d = datetime.date(2020, 5, 15)
print(d.strftime('%B %d %Y'))

s = "10:30 PM on May 15, 2020"
dt = datetime.datetime.strptime(s, "%I:%M %p on %B %d, %Y")
print(dt)
print(datetime.datetime.isoformat(dt))
# %%
#Function to take in an epoch time and return dt object
def epoch_to_dt(epoch_string):
    time_obj = time.gmtime(epoch_string)

    return datetime.datetime(year=time_obj.tm_year, month=time_obj.tm_mon, day=time_obj.tm_mday, hour=time_obj.tm_hour, minute=time_obj.tm_min, second=time_obj.tm_sec)

print(epoch_to_dt(12345678.9))

# %%
# Function to take 2 iso formated strings and returns hour diff
def hrs_diff(iso1, iso2):
    dt1 = datetime.datetime.fromisoformat(iso1)
    dt2 = datetime.datetime.fromisoformat(iso2)
    time_delta = dt2 - dt1
    return round(time_delta.total_seconds()/60/60)

a = hrs_diff('2001-01-01T13:50:23', '2001-06-12T14:23:50')
print(a)


# %%

# PYTZ LIBRARY
# a. Implements Olson (or IANA) database
# b. supports DST (Daylight Saving times)
# c. uniform naming convention. 
# d. Goes back to 1970 accurately with all changes in dst and timezones.a

import pytz

# To see all time zones.
for tz in pytz.all_timezones: 
 print(tz)
# %%
# pytz object can be used instead of tzinfo objects.
dt = datetime.datetime(year=2023, month=1, day=13 ,tzinfo=pytz.timezone('Asia/Calcutta'))
print(dt)
# %%

# These are DstTZ objects i.e. have awareness of dst
tz_chicago = pytz.timezone('America/Chicago')
print(repr(tz_chicago))
print(tz_chicago.zone)
print(pytz.timezone('UTC').zone)
# %%

# convert Naive datetimes to be time aware, 
# the DST in output means the timezone was in daylight savings
# if not it shows up as STD.
dt_naive = datetime.datetime(2020,5,30,10,0,0)
dt_chicago = tz_chicago.localize(dt_naive)
print(repr(dt_naive))
print(repr(repr(dt_chicago)))
print(repr(tz_chicago.localize(datetime.datetime(2020,12,31,10,0,0))))
# %%
# convert between time zones.
tz_melb = pytz.timezone('Australia/Melbourne')
dt_chicago.astimezone(tz_melb)
# %%
# UTC naive can be directly converted to pytz
tz_chicago.fromutc(datetime.datetime.utcnow())
# %%

# DATEUTILS LIBRARY (to parse dates)
# Assumes month first , override by dayfirst keyword arg
from dateutil import parser

print(repr(parser.parse('2020-01-01 10:30:00 am +5:30')))
print(repr(parser.parse('3/6/2020')))
print(repr(parser.parse('3/6/2020', dayfirst=True)))

# use fuzzy_with_tokens=True to return tupe (parsed date, ignored text)
s = "Today is May the 23, 2020 at 3pm UTC"
try:
    parser.parse(s)
except Exception as ex:
    print(type(ex),ex)

# any parser failure gives ParserError.
print(parser.parse(s, fuzzy_with_tokens=True))
