from django import forms

from games.models import BoardGame


class BoardGameBaseForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = '__all__'
        labels = {
            'title': 'Game Title',
            'min_players': 'Min. Players',
            'max_players': 'Max. Players',
            'play_time': 'Play Time (minutes)',
            'rating': 'Rating (1-10)',
            'description': 'Description',
            'cover_image_url': 'Cover Image URL',
            'publisher': 'Publisher',
            'categories': 'Categories',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Catan, Scythe...'}),
            'min_players': forms.NumberInput(attrs={'placeholder': 'e.g. 1'}),
            'max_players': forms.NumberInput(attrs={'placeholder': 'e.g. 4'}),
            'play_time': forms.NumberInput(attrs={'placeholder': 'e.g. 60'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'e.g. 7'}),
            'description': forms.Textarea(attrs={'placeholder': 'The goal of the game is...'}),
            'cover_image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/image.jpg'}),
        }
        help_texts = {
            'rating': 'Enter a whole number between 1 and 10',
            'categories': 'Hold CTRL (or CMD) to select multiple categories'
        }

class BoardGameCreateForm(BoardGameBaseForm):
    pass

class BoardGameDeleteForm(BoardGameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True