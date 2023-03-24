import random
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from schedule.models import Physician, Appointment, Week, Year

# Get the current year
current_year = date.today().year

# Create a year object for the current year if it doesn't exist
year, created = Year.objects.get_or_create(year=current_year)

# Loop over all the weeks in the year and create a Week object for each week
start_date = date(year=current_year, month=1, day=1)
end_date = date(year=current_year, month=12, day=31)
week_start_dates = [start_date + timedelta(days=i) for i in range(7 - start_date.weekday(), (end_date - start_date).days, 7)]
for week_start_date in week_start_dates:
    week_obj, created = Week.objects.get_or_create(year=year, week_start_date=week_start_date)


# Get the user object for the physician
user = User.objects.get(username='jose')
physician = Physician.objects.get(user=user)

# Generate some random appointments for the physician
start_date = datetime(year=year.year, month=1, day=1)
end_date = datetime(year=year.year, month=12, day=31)
time_delta = timedelta(minutes=30)

for i in range(50):
    start_time = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(8, 16))
    end_time = start_time + time_delta * random.randint(1, 6)
    appointment_type = random.choice(['C', 'N'])
    appointment = Appointment.objects.create(start_time=start_time, end_time=end_time, type=appointment_type, physician=physician, user=user)
    week_start_date = appointment.start_time - timedelta(days=appointment.start_time.weekday())
    week_obj = Week.objects.get(week_start_date=week_start_date)
    week_obj.appointments.add(appointment)
