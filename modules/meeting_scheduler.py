from datetime import datetime
from icalendar import Calendar, Event
import pytz

class MeetingScheduler:
    def schedule(self, title, start_time, end_time, description, attendees):
        cal = Calendar()
        event = Event()

        event.add('summary', title)
        event.add('dtstart', datetime.strptime(start_time, "%Y-%m-%d %H:%M").replace(tzinfo=pytz.UTC))
        event.add('dtend', datetime.strptime(end_time, "%Y-%m-%d %H:%M").replace(tzinfo=pytz.UTC))
        event.add('description', description)

        for attendee in attendees:
            event.add('attendee', f'MAILTO:{attendee}')

        cal.add_component(event)

        with open('meeting.ics', 'wb') as f:
            f.write(cal.to_ical())

        return "Meeting scheduled and ICS file created."

