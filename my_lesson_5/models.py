from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
# from django.urls import reverse
# Create your models here.

User=get_user_model()

class Advertisment(models.Model):
    class Meta:
        db_table = "advertisment"
    photo = models.ImageField("изображение", upload_to="my_lesson_5")
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.SmallIntegerField("Категория")
    author = models.CharField("Автор", max_length=20)
    location = models.CharField("Локация", max_length=255)
    action = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    user = models.ForeignKey(User,verbose_name="Автор",on_delete=models.CASCADE)

    
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.title, self.description, self.price, 
        self.created_at, self.updated_at, self.category, self.author, self.location, self.action)
    
    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created_at == timezone.now().date():
            create_time=self.created_at.strftime("%H:%M.%S")
            return format_html('<span style="color: teal; font-weight: bold">Сегодня в </span>',create_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M.%S")

    @admin.display(description="Дата обновления")
    def updated_date(self):
        if self.updated_at == timezone.now().date():
            updated_time=self.updated_at.strftime("%H:%M.%S")
            return format_html('<span style="color: teal; font-weight: bold">Сегодня в </span>',updated_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M.%S")

    @admin.display(description="Изображение")
    def photo_img(self):
        if self.photo:
            return format_html('<img src="%s" height="50" width="50">' % self.photo.url)       
        else:
            return format_html('<img src="static/image/adv.png" width="50">') 
        
    
    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={"pk":self.pk})
    
