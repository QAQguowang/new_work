from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo' #修改表的名字
        verbose_name = '书籍管理' #admin站点使用
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):

    #有序字典用于枚举
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    #外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
