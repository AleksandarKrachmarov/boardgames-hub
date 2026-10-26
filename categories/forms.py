from django import forms

from categories.models import Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter category description'}),
        }

class CategoryCreateForm(CategoryBaseForm):
    pass

class CategoryEditForm(CategoryBaseForm):
    pass

class CategoryDeleteForm(CategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True