__version__ = "1.0.0"

from django.conf import settings

CALENDARAPP_MODEL = getattr(settings, "CALENDARAPP_MODEL", "calendarapp.Event")

def get_calendarapp_model():
    from django.apps import apps
    return apps.get_model(CALENDARAPP_MODEL)
