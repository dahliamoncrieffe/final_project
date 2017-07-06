import os
import sys
import django

def populate():
    educational_event = add_evnt('Educational Event', views=50, count=25)

    add_details(evnt=educational_event,
        title="Toddler Story time",
        cost="Free",
        url="http://libwww.freelibrary.org/calendar/calbydate.cfm?SeriesID=Storytimes")

    add_details(evnt=educational_event,
        title="GFS Explore Camp",
        cost = "125.00",
        url="https://phillyfunguide.com/kids/gfs-explorer-camp")

    add_details(evnt=educational_event,
        title="Puzzling Adventures",
        cost="49.99",
        url="https://phillyfunguide.com/kids/puzzling-adventures")

    outdoors_event = add_evnt("Outdoors Events", views=64, count=50)

    add_details(evnt=outdoors_event,
        title="Summer Spectale",
        cost="50.00",
        url="outdoors_event")

    add_details(evnt=outdoors_event,
        title="Philadephia Zoo",
        cost="20.00",
        url="https://phillyzoo.pivvit.com/purchase-tickets")

    add_details(evnt=outdoors_event,
        title="Smith Playground",
        cost="Free",
        url="http://smithplayground.org/")

    skillbuilding_event = add_evnt("Skill Building", views=120, count=102)

    add_details(evnt=skillbuilding_event,
        title="YMCA: Toddler Swim Class",
        cost="100.00",
        url="https://philaymca.org/program/swim-parent-child-18-mo-3-yrs/")

    add_details(evnt=skillbuilding_event,
        title="Suziki Piano Program",
        cost="175",
        url="http://www.philasuzukipiano.com/2011/Tuition_%26_Fees.html")

    # Print out what we have added to the user.
    for e in Event.objects.all():
        for d in EventDetails.objects.filter(event=e):
            print("- {0} - {1}".format(str(e), str(d)))


def add_details(evnt, title, cost, url, views=0):
    d = EventDetails.objects.get_or_create(event=evnt, title=title, cost=cost, url=url, views=views)[0]
    return d

def add_evnt(name, views=0, count=0):
    e = Event.objects.get_or_create(name=name,views=views,count=count)[0]
    return e

# Start execution here!
if __name__ == '__main__':

    print
    "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
    django.setup()
    from event_a_mom.models import Event, EventDetails
populate()
