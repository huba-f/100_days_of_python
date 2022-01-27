from django import forms
 
COFFEES = [
     ('✘', '✘'),
     ('☕', '☕'),
    ('☕☕', '☕☕'),
    ('☕☕☕', '☕☕☕'),
]
WIFIS = [
     ('✘', '✘'),
     ('💪', '💪'),
    ('💪💪', '💪💪'),
    ('💪💪💪', '💪💪💪'),
]
ADAPTERS = [
     ('✘', '✘'),
     ('🔌', '🔌'),
    ('🔌🔌', '🔌🔌'),
    ('🔌🔌🔌', '🔌🔌🔌'),
]


class AddCafe(forms.Form):
    name = forms.CharField()
    location = forms.CharField()
    opening_hour = forms.CharField()
    closeing_hour = forms.CharField()
    coffee = forms.CharField(label='Taste of coffee', widget=forms.Select(choices=COFFEES))
    wifi = forms.CharField(label='how strong the wifi was', widget=forms.Select(choices=WIFIS))
    power = forms.CharField(label='power adapter slots', widget=forms.Select(choices=ADAPTERS))
    