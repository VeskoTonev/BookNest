from django import forms

from challenges.models import ReadingGoal

#Adding challenges
class ReadingGoalsForm(forms.ModelForm):

    class Meta:
        model = ReadingGoal
        fields = '__all__'

        widgets = {
         'year':  forms.NumberInput(attrs = {
             'class' : 'form-control',
             'placeholder' : 'Enter Year'
         }),
            'target_book' : forms.NumberInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter Number of books'
            })
        }
