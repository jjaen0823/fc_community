from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(max_length=128, label='Title',
        error_messages={
            'required': 'Title field is required'
        }
    )
    contents = forms.CharField(widget=forms.Textarea, label='Contents',
        error_messages={
            'required': 'Contents field is required'
        }) 
    tags = forms.CharField(required=False, widget=forms.Textarea, label='Tags',)
        