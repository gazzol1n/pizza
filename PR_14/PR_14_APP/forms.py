from django import forms

class UserForm(forms.Form):
    file = forms.FileField(label="Файл")
    file_path = forms.FilePathField(label="Выберите файл", path="C:/my_doc/", allow_files=True, allow_folders=True)
    num_float = forms.FloatField(label="Введите число с плавающей точкой")
    ip_address = forms.GenericIPAddressField(label="IP адрес", help_text="Пример формата 192.0.2.0")
    image = forms.ImageField(label="Изображение")
    num_integer = forms.IntegerField(label="Введите целое число")
    json_data = forms.JSONField(label="Данные формата JSON")
    countries = forms.MultipleChoiceField(
        label="Выберите страны",
        choices=((1, "Англия"), (2, "Германия"), (3, "Испания"), (4, "Россия"))
    )
    travel_choice = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")
    regex_text = forms.RegexField(label="Текст (формат 0A0)", regex="^[0-9][A-F][0-9]$")
    slug_text = forms.SlugField(label="Введите текст (Slug)")
    time = forms.TimeField(label="Введите время")
    city_choice = forms.TypedChoiceField(
        label="Выберите город",
        empty_value=None,
        choices=((1, "Москва"), (2, "Воронеж"), (3, "Курск"))
    )
    cities_multiple = forms.TypedMultipleChoiceField(
        label="Выберите несколько городов",
        empty_value=None,
        choices=((1, "Москва"), (2, "Воронеж"), (3, "Курск"), (4, "Томск"))
    )
    url = forms.URLField(label="Введите URL", help_text="Например http://www.yandex.ru")
    uuid = forms.UUIDField(label="Введите UUID", help_text="Формат xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
