from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField("Nomi", max_length=150)
    slug = models.SlugField("*")
    
    def __str__(self):
        return self.title


class Gellary(models.Model):
    title = models.CharField("izoh", max_length=150, blank=True)
    image = models.ImageField("rasm", upload_to='gellary/')

    def __str__(self):
        return self.image.url


class News(models.Model):
    author = models.ForeignKey("teachers.Teacher", related_name="news", on_delete=models.CASCADE)
    title = models.CharField("Sarlavha", max_length=350)
    image = models.ImageField("Rasmi", upload_to='news_images/')
    video = models.CharField("Video", max_length=60, blank=True)
    category = models.ForeignKey("main.Category", related_name="news", on_delete=models.CASCADE)
    gellary = models.ManyToManyField("main.Gellary", related_name="gnews", blank=True)
    body = models.TextField("Matni")
    date = models.DateField("sanasi", auto_now_add=True)

    def __str__(self):
        return self.title


class Reports(models.Model):
    title = models.CharField("Sarlavha", max_length=550)
    category = models.ForeignKey("main.Category", related_name="Reports", on_delete=models.CASCADE)
    image = models.ImageField("Rasmi", upload_to='report_images')
    description = models.TextField("Qoshimcha", blank=True)
    date = models.DateField("sanasi", auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    news = models.ForeignKey("main.News", related_name="comments", on_delete=models.CASCADE)
    name = models.CharField("Ismi", max_length=50)
    surname = models.CharField("Familiya", max_length=50)
    message = models.TextField("Message")
    date = models.DateTimeField("Date", auto_now_add=True)

    def create(self, news, name, surname, message):
        new = Comments.objects.create(
            news=news,
            name=name,
            surname=surname,
            message=message
        )
        new.save()


class Contact(models.Model):
    name = models.CharField("name", max_length=50)
    surname = models.CharField("surname", max_length=50)
    tel_number = models.CharField("tel_number", max_length=50)

    def __str__(self):
        return self.name