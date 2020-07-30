from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import Issue, Comment, Reply


TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class IssueEditForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'id':'id_description_edit'}), 
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Issue
        fields = ('title', 'issue_type', 'is_resolved', 'resolved_date', 'description', 'image', 'tags', )
        widgets = {
            'is_resolved': forms.Select(choices=TRUE_FALSE_CHOICES, attrs={'style':'width:150px;'}),
            'resolved_date': forms.DateInput(attrs={'type': 'date', 'style':'width:200px;'}),
        }

class IssueCreateForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'id':'id_description_edit'}), 
        max_length=4000,
        required=False,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Issue
        fields = ('title', 'issue_type', 'description', 'image', 'tags', )

    def clean_description(self):
        '''Ensure field is not empty'''
        desc = self.cleaned_data.get('description')
        if not desc:
            raise forms.ValidationError(_('This field should not be empty.'), code='invalid')
        return desc


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply',)