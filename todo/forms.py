from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control todoform',
                'placeholder': 'Add a Todo Task',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn'}))


class UpdateTodoForm(forms.Form):
    text = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'update-todo', 
                'placeholder': 'Update Todo Task',
                'aria-label': 'UpdateTodo',
                'aria-describedby': 'update-btn'}))
