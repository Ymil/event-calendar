from django.views.generic import ListView

# from calendarapp.models import Event

from .. import get_calendarapp_model

Event = get_calendarapp_model()

class AllEventsListView(ListView):
    """ All event list views """

    template_name = "events_list.html"
    model = Event

    def get_queryset(self):
        qs = super().get_queryset()
        return self.model.objects.get_all_events(user=self.request.user)


class RunningEventsListView(ListView):
    """ Running events list view """

    template_name = "events_list.html"
    model = Event

    def get_queryset(self):
        return self.model.objects.get_running_events(user=self.request.user)
