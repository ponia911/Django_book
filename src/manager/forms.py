from django.forms import Form, TextInput, Textarea

from manager.models import Book


class AddBookForm(Form):
    class Meta:
        model = Book
        fields = ('title', 'text')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form_control'})
        }