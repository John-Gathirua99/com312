from django import forms

class FriendProfileSearchForm(forms.Form):
    SEARCH_CHOICES = [
         ('hometown', 'Hometown'),
        ('age', 'Age'),
        ('full_name', 'Name'),
        ('school', 'School'),
        ('secondary_school', 'Secondary School'),
        ('University_or_college', 'University or College'),
        ('country', 'Country'),
        ('year', 'Year'),
        ('interests', 'Interests'),
       
    ]
    
    search_field = forms.ChoiceField(choices=SEARCH_CHOICES, required=True, label='Search By')
    search_value = forms.CharField(max_length=255, required=True, label='Search Value')
