from django import forms

from challenges.models import ReadingGoal

#Adding challenges
class ReadingGoalsForm(forms.ModelForm):

    class Meta:
        model = ReadingGoal
        fields = ['year','target_book']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['year'].disabled = True

        labels = {
            'year': 'Goal Year',
            'target_book': 'Target Book'
        }

        widgets = {
         'year':  forms.NumberInput(attrs = {
             'class' : 'form-control',
             'placeholder' : 'Enter Year(e.g. 2026)'
         }),
            'target_book' : forms.NumberInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'How many books do you want to read?',
                'min' : '1'
            })
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if not self.instance.pk and ReadingGoal.objects.filter(year = year).exists():
            raise forms.ValidationError(f'A reading goal for {year} already exists')
        return year
