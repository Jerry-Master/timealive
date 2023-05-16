from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date, timedelta
from .models import Appointment

@login_required(login_url='/accounts/login/')
def schedule(request, weeks_delta=1):
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

    user = request.user
    appointments = Appointment.objects.filter(user=user, start_time__gte=start_date, end_time__lte=end_date)

    hours = ['9:00', '10:00', '11:00', '12:00', '1:00', '2:00', '3:00', '4:00', '5:00']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    appointment_data = {}

    # Loop over all the appointments and populate the appointments dictionary
    for appointment in appointments:
        appointment_day = appointment.start_time.strftime('%A')
        appointment_hour = appointment.start_time.strftime('%-I:%M')
        appointment_type = appointment.type
        if appointment_day not in appointment_data:
            appointment_data[appointment_day] = {}
        appointment_data[appointment_day][appointment_hour] = appointment_type
    
    # Pass the appointments dictionary to the template context
    context = {
        'hours': hours,
        'days': days,
        'appointments': appointment_data,
        'start_date': start_date,
        'end_date': end_date - timedelta(days=1),
    }
    return render(request, 'schedule.html', context)
