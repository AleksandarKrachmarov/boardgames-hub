from django import forms

from publishers.models import Publisher


class PublisherBaseForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter publisher name'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter publisher country'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter publisher website'}),
        }

class PublisherCreateForm(PublisherBaseForm):
    pass

class PublisherEditForm(PublisherBaseForm):
    pass

class PublisherDeleteForm(PublisherBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True