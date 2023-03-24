from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date, timedelta

@login_required(login_url='/accounts/login/')
def schedule(request, weeks=1):
    if request.method == 'POST':
        weeks_delta = int(request.POST['weeks'])
        action = request.POST['action']
        if action == 'back':
            weeks_delta = -weeks_delta
    else:
        weeks_delta = int(weeks_delta)

    weeks = request.session.get('weeks', 0)
    weeks += weeks_delta
    request.session['weeks'] = weeks

    # Calculate the date range for the schedule
    today = date.today()
    start_date = today + timedelta(days=-today.weekday()) + timedelta(weeks=weeks)
    end_date = start_date + timedelta(days=5)

    # Example data
    hours = ['9:00', '10:00', '11:00', '12:00', '1:00', '2:00', '3:00', '4:00', '5:00']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    appointments_0 = {
        'Monday': {'9:00': 'Appointment 1', '11:00': 'Appointment 2', '2:00': 'Appointment 3'},
        'Tuesday': {'10:00': 'Appointment 4', '1:00': 'Appointment 5', '4:00': 'Appointment 6'},
        'Wednesday': {'9:00': 'Appointment 7', '12:00': 'Appointment 8', '3:00': 'Appointment 9'},
        'Thursday': {'10:00': 'Appointment 10', '11:00': 'Appointment 11', '4:00': 'Appointment 12'},
        'Friday': {'9:00': 'Appointment 13', '1:00': 'Appointment 14', '5:00': 'Appointment 15'},
    }

    # Example data for week 1
    appointments_1 = {
        'Monday': {'9:00': 'Appointment 16', '11:00': 'Appointment 17', '2:00': 'Appointment 18'},
        'Tuesday': {'10:00': 'Appointment 19', '1:00': 'Appointment 20', '4:00': 'Appointment 21'},
        'Wednesday': {'9:00': 'Appointment 22', '12:00': 'Appointment 23', '3:00': 'Appointment 24'},
        'Thursday': {'10:00': 'Appointment 25', '11:00': 'Appointment 26', '4:00': 'Appointment 27'},
        'Friday': {'9:00': 'Appointment 28', '1:00': 'Appointment 29', '5:00': 'Appointment 30'},
    }

    # Example data for week 2
    appointments_2 = {
        'Monday': {'9:00': 'Appointment 31', '11:00': 'Appointment 32', '2:00': 'Appointment 33'},
        'Tuesday': {'10:00': 'Appointment 34', '1:00': 'Appointment 35', '4:00': 'Appointment 36'},
        'Wednesday': {'9:00': 'Appointment 37', '12:00': 'Appointment 38', '3:00': 'Appointment 39'},
        'Thursday': {'10:00': 'Appointment 40', '11:00': 'Appointment 41', '4:00': 'Appointment 42'},
        'Friday': {'9:00': 'Appointment 43', '1:00': 'Appointment 44', '5:00': 'Appointment 45'},
    }

    appointment_data = [appointments_0, appointments_1, appointments_2]

    appointments = appointment_data[weeks % len(appointment_data)]
    
    context = {
        'hours': hours,
        'days': days,
        'appointments': appointments,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'schedule.html', context)
