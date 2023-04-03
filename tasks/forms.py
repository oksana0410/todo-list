from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    deadline_datetime = forms.DateTimeField(
        widget=forms.TextInput(attrs={"placeholder": "YYYY-MM-DD HH:MM:SS"}),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
