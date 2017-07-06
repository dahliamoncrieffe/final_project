from django import forms
from django.contrib.auth.models import User
from event_a_mom.models import UserProfile, Event, EventDetails


class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Please enter the event name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Event
        fields = ('name','views', 'count')

class EventDetailsForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Please enter the title of the page.")
    url = forms.CharField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if not url.startswith('http://'):
            url = 'http://' + url

        cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = EventDetails
        fields = ('title', 'url','views')

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):

    # website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = [ 'picture']
