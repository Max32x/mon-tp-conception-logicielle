import datetime
import pytz

# Set the Réunion timezone
reunion_tz = pytz.timezone('Indian/Reunion')

# Get the current date and time in UTC
utc_now = datetime.datetime.utcnow()

# Convert the UTC datetime to the Réunion timezone
reunion_dt = utc_now.astimezone(reunion_tz)

# Print out the current date and time in the Réunion timezone
print("The current date and time in Réunion is:")
print(reunion_dt.strftime("%Y-%m-%d %H:%M:%S"))