from django.db import models
from django.urls import reverse  # Для создания URL-адресов по идентификатору объекта

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)
    photo = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    photo = models.ImageField(upload_to='images', blank=True)

    def display_author(self):
        return ', '.join(author.last_name for author in self.author.all())
    display_author.short_description = 'Authors'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    inv_nom = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
