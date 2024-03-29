from django import forms
from rango.models import Category, Page, User, UserProfile
import re

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                            help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text='Please enter the title of the page.')
    url = forms.URLField(max_length=200,
                        help_text='Please the URL of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        # exclude = ('category', 'views')
        fields = ('title', 'url')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        url = re.sub(r"http[s]:[\/]+","", url)
        if url:
            url = f'https://{url}'
            cleaned_data['url'] = url
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)
