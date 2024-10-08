
# SOAP UI test file
xml_file = "../Swiss-OJP-2.0/ojp2_testcases_soapui.xml"

# POSTMAN test file
postman_file = "../Swiss-OJP-2.0/ojp2_testcases_postman.json"

# Folder to write the examples
output_folder = "./examples"

# Some functions for the calculation of some given times
import datetime


def get_friday_before_second_sunday_december_1200():
    current_year = datetime.datetime.now().year
    december = datetime.datetime(current_year, 12, 1)
    second_sunday = december + datetime.timedelta(days=(6 - december.weekday()) + 7)
    friday_before_second_sunday = second_sunday - datetime.timedelta(days=2)

    if friday_before_second_sunday < datetime.datetime.now():
        current_year += 1
        december = datetime.datetime(current_year, 12, 1)
        second_sunday = december + datetime.timedelta(days=(6 - december.weekday()) + 7)
        friday_before_second_sunday = second_sunday - datetime.timedelta(days=2)
    friday_before_second_sunday.replace(hour=12, minute=0, second=0, microsecond=0)
    utc_timestamp=friday_before_second_sunday.astimezone(datetime.timezone.utc).isoformat()
    return utc_timestamp

def get_friday_before_second_sunday_december_2345():
    current_year = datetime.datetime.now().year
    december = datetime.datetime(current_year, 12, 1)
    second_sunday = december + datetime.timedelta(days=(6 - december.weekday()) + 7)
    friday_before_second_sunday = second_sunday - datetime.timedelta(days=2)

    if friday_before_second_sunday < datetime.datetime.now():
        current_year += 1
        december = datetime.datetime(current_year, 12, 1)
        second_sunday = december + datetime.timedelta(days=(6 - december.weekday()) + 7)
        friday_before_second_sunday = second_sunday - datetime.timedelta(days=2)
    friday_before_second_sunday.replace(hour=23, minute=45, second=0, microsecond=0)
    utc_timestamp=friday_before_second_sunday.astimezone(datetime.timezone.utc).isoformat()
    return utc_timestamp
def get_friday_before_second_sunday_december_date():
    current_year = datetime.datetime.now().year
    december = datetime.datetime(current_year, 12, 1)
    second_sunday = december + datetime.timedelta(days=(6 - december.weekday()) + 7)
    friday_before_second_sunday = second_sunday - datetime.timedelta(days=2)

    if friday_before_second_sunday < datetime.datetime.now():
        current_year += 1
        december = datetime.datetime(current_year, 12, 1)
        second_sunday = december + datetime.timedelta(days=(6 - december.weekday()) + 7)
        friday_before_second_sunday = second_sunday - datetime.timedelta(days=2)

    return friday_before_second_sunday.strftime("%Y-%m-%d")


def get_current_timestamp():
    current_utc_timestamp = datetime.datetime.utcnow().isoformat()
    return current_utc_timestamp

def get_current_timestamp_1200():
    current_utc_timestamp = datetime.datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0).isoformat()
    current_utc_timestamp
    return current_utc_timestamp


timestamp = get_current_timestamp()
dt = datetime.datetime.now()
mymap = {
    "{$isoTimestamp}": get_current_timestamp_1200(),
    "${IsoTimestampUTC}": get_current_timestamp_1200(),
    "{Freitag12UhrVorFahrplanwechsel}": get_friday_before_second_sunday_december_1200(), # TODO probably problem
    "${Freitag12UhrVorFahrplanwechsel}": get_friday_before_second_sunday_december_1200(),
    "{DatumFreitagVorFahrplanwechsel}": get_friday_before_second_sunday_december_date(), # TODO probably problem
    "${DatumFreitagVorFahrplanwechsel}": get_friday_before_second_sunday_december_date(),
    "${DatumFreitagVorFahrplanwechselohneT}": get_friday_before_second_sunday_december_2345(),
    "{DatumFreitagVorFahrplanwechselohneT}": get_friday_before_second_sunday_december_2345(),
    "{ActiveJourneyRef}": "NoActiveJourneyRef",
    "{ActiveOperatingDayRef}": dt.strftime('%Y-%m-%d'),
    "${Freitag2345UhrVorFahrplanwechsel}": get_friday_before_second_sunday_december_2345()
}
