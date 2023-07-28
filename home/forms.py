from django import forms

class questions(forms.Form):
    question = forms.CharField(label="Question", widget=forms.TextInput(attrs={'class':'form-control', 'style':'border:1px solid black'}), max_length=200)
#    que1 = forms.CharField(widget=forms.TextInput)

class answers(forms.Form):
    answer = forms.CharField(label= "Answer", widget=forms.Textarea(attrs={'class':'form-control', 'style':'border:1px solid black'}))
