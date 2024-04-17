from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from .models import UserSkill
from .models import UserLocation
from .models import Review, Event
from .models import SkillPointRequest, Resource
from .models import PreferredSkill, Community
from datetime import datetime
from django.utils import timezone

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocation
        fields = ('country', 'state', 'city')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'profile_picture',
            'about_me',
        )


class SkillForm(forms.ModelForm):
    class Meta:
        model = UserSkill
        fields = ['category', 'name', 'description']

class PreferredSkillsForm(forms.Form):
    skill_categories = forms.MultipleChoiceField(
        choices=UserSkill.SkillCategory.choices,
        widget=forms.CheckboxSelectMultiple,
    )


class UserSearchForm(forms.Form):
    query = forms.CharField(label='Skill', max_length=100)


class SkillSessionForm(forms.Form):
    date_and_time = forms.DateTimeField(
        label='Date and Time',
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    duration_minutes = forms.IntegerField(label='Duration (minutes)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the minimum value for the date_and_time field to the current date and time
        self.fields['date_and_time'].widget.attrs['min'] = datetime.now().strftime(
            '%Y-%m-%dT%H:%M')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']


class SkillPointRequestForm(forms.ModelForm):
    class Meta:
        model = SkillPointRequest
        fields = ['points_requested']


class CollabSessionForm(forms.Form):
    date_and_time = forms.DateTimeField(
        label='Date and Time',
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    def __init__(self, *args, **kwargs):
        super(CollabSessionForm, self).__init__(*args, **kwargs)
        # Set the min attribute to the current datetime
        self.fields['date_and_time'].widget.attrs['min'] = datetime.now().strftime(
            '%Y-%m-%dT%H:%M')

class CreateCommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description', 'profile_picture']


class ResourceUploadForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['file', 'name', 'description']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'venue', 'address', 'timestamp']
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'min': timezone.now().strftime('%Y-%m-%dT%H:%M'), 'type': 'datetime-local'}),
        }