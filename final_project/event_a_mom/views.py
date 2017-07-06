from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from event_a_mom.models import EventDetails, Event, UserProfile
from event_a_mom.forms import UserForm, UserProfileForm, EventForm, EventDetailsForm
#Create your views here.

def encode_url(str):
    return str.replace(' ', '_').lower()

def decode_url(str):

    return str.replace('_', ' ').capitalize()

def index(request):
    # event_list = Events.objects.order_by('-count')[:5]
    context = RequestContext(request)
    #context_dict = {'events': event_list}
    return render_to_response('event_a_mom/index.html', context)

def event(request, event_name_url):
    # Request our context
    context = RequestContext(request)

    # Change underscores in the category name to spaces.
    # URL's don't handle spaces well, so we encode them as underscores.
    event_name = decode_url(event_name_url)

    # Build up the dictionary we will use as out template context dictionary.
    context_dict = {'event_name': event_name, 'event_name_url': event_name_url}

    try:
        # Find the event with the given name.
        # Raises an exception if the event doesn't exist.
        # We also do a case insensitive match.
        event_model = Event.objects.get(name__iexact=event_name)

        # Retrieve all the associated pages.
        # Note that filter returns >= 1 model instance.
        eventDetails = EventDetails.objects.filter(category=event_model)

        # Adds our results list to the template context under name pages.
        context_dict['details'] = eventDetails
    except Event.DoesNotExist:
        # We get here if the category does not exist.
        # Will trigger the template to display the 'no category' message.
        pass

    # Go render the response and return it to the client.
    return render_to_response('event_a_mom/event.html', context_dict, context)

def add_event(request):
    # Get the context from the request.
    context = RequestContext(request)

    if request.method == 'POST':
        form = EventForm(request.POST)


        if form.is_valid():

            form.save(commit=True)

            return index(request)
        else:
            pass
    else:
        # If the request was not a POST, display the form to enter details.
        form = EventForm()

    return render_to_response('event_a_mom/add_event.html', {'form': form}, context)

# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']
#             profile.save()
#             registered = True
#         else:
#             print (user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm
#         render(request,'event_a_mom/register.html',{'user_form': user_form,'profile_form': profile_form,
#                                                     'registerd': registered})
# def user_login(request):
#     if request.method == "POST":
#         userName = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=userName, password=password)
#         if user:
#             login(request,user)
#             return HttpResponseRedirect('/users/home')
#         else:
#             error = " Sorry! Phone Number and Password didn't match, Please try again ! "
#             return render(request, 'event_a_mom/index.html',{'error':error})
#     else:
#         return render(request, 'event_a_mom/index.html')
#
# def users_signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         userName = request.POST.get('username')
#         pass_1 = request.POST.get('password1')
#         pass_2 = request.POST.get('password2')
#         if pass_1 == pass_2:
#              user = User.objects.create_user(
#                                               username=userName,
#                                               email=email,
#                                               password=pass_1,
#                                              )
#              return HttpResponseRedirect("/")
#         else:
#              error = " Password Mismatch "
#              return render(request, 'event_a_mom/signup.html',{"error":error})
#     else:
#          return render(request, 'event_a_mom/signup.html')
