from django import forms
from django.forms import inlineformset_factory
from reading_list.models import ReadingList, ReadingListItems


# Creating a List with books
class ListForm(forms.ModelForm):
        class Meta:
            model = ReadingList
            fields = [
                'name',
                'description',
            ]

            labels = {
                'name' : "Reading List",
                'description' : "Description",
            }

            widgets = {
                'name': forms.TextInput(attrs={
                    'class': "form-control",
                    'placeholder': "Enter a name for your list",

                }),

                'description': forms.Textarea(attrs={
                    'class': "form-control",
                    'rows': '3',
                    'placeholder': "Describe your list"
                }),

            }



class ReadingListItemForm(forms.ModelForm):
    class Meta:
        model = ReadingListItems
        fields = [
            'reading_list',
            'book',
            'notes'
        ]

        labels = {
            'reading_list': "Reading List",
            'book': "Book",
            'notes': 'Personal notes'
        }

        widgets = {
            'reading_list': forms.Select(attrs={
                'class': "form-select",
            }),

             'book': forms.Select(attrs={
                'class': "form-select",
            }),

            'notes': forms.Textarea(attrs={
                'class': "form-control",
                'rows': '3',
                'placeholder': "Optional notes about your list"
            })

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.initial.get('reading_list'):
            self.fields['reading_list'].disabled = True




    def clean(self):

        cleaned_data = super().clean()

        if cleaned_data is None:
            return cleaned_data

        reading_list = cleaned_data.get('reading_list')
        book = cleaned_data.get('book')


        if reading_list and book:
            duplicate = ReadingListItems.objects.filter(reading_list=reading_list, book=book)

            if self.instance.pk:
                duplicate = duplicate.exclude(pk=self.instance.pk)

            if duplicate.exists():
                raise forms.ValidationError('This book already exists in this reading list')

        return cleaned_data

ReadingListItemFormSet = inlineformset_factory(
    parent_model = ReadingList,
    model = ReadingListItems,
    form = ReadingListItemForm,
    fields = ['book', 'notes'],
    extra = 1,
    can_delete = True,
    widgets = {
    "book": forms.Select(attrs = {"class": "form-input"}),
    "notes": forms.Textarea(attrs = {
        "class" : "form-input",
        "rows": "2",
        "placeholder": "Optional notes"
    })

    }

)