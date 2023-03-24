from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.utils.translation import gettext_lazy as _


class Physician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Year(models.Model):
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
    year = models.IntegerField()
    weeks = models.ManyToManyField('Week')

    @classmethod
    def create_year(cls, year, physician):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        num_weeks = (end_date - start_date).days // 7 + 1

        year_obj = cls.objects.create(year=year, physician=physician)

        for i in range(num_weeks):
            week_start_date = start_date + timedelta(days=i*7)
            week_obj = Week.create_week(week_start_date)
            year_obj.weeks.add(week_obj)

        return year_obj

    def __str__(self):
        return f'{self.year}'

    class Meta:
        ordering = ['year']


class Week(models.Model):
    week_start_date = models.DateField()
    appointments = models.ManyToManyField('Appointment')

    @classmethod
    def create_week(cls, start_date):
        end_date = start_date + timedelta(days=6)
        week = cls.objects.create(week_start_date=start_date)
        appointments = Appointment.objects.filter(start_time__gte=start_date, start_time__lte=end_date)
        week.appointments.set(appointments)
        return week

    def __str__(self):
        return f'{self.week_start_date}'

    class Meta:
        ordering = ['week_start_date']


class Appointment(models.Model):
    TYPE_CHOICES = (
        ('C', _('Chronic')),
        ('N', _('Normal')),
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='N')
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.start_time} - {self.end_time} ({self.get_type_display()})'
