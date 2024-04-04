from django import forms


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100)  # Название
    description = forms.CharField(widget=forms.Textarea)  # Описание
    steps = forms.CharField(widget=forms.Textarea)  # Шаги приготовления
    cook_time = forms.DurationField()  # Время приготовления
    image = forms.ImageField()  # Изображение
    # author = forms.ForeignKey(User, on_delete=models.CASCADE)  # Автор

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
