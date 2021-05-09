from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


# 增加数据
from book.models import BookInfo
from book.models import PeopleInfo

book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
book.save()
# ----------------2--------------
BookInfo.objects.create(
    name='Django企业开发实战',
    pub_date='2020-1-1',
    readcount=100
)

# 修改数据
book = BookInfo.objects.get(id=6)
book.name = '运维入门'
book.save()
# ----------------2--------------
BookInfo.objects.filter(id=6).update(name='爬虫入门', commentcount=777)

# 删除数据
# ---------1:物理删除---------------
book = BookInfo.objects.get(id=1)
book.delete()
# ---------2:物理删除---------------
BookInfo.objects.get(id=6).delete()

# 查询数据
# ---------1:查询单一结果---------------
book = BookInfo.objects.get(id=2)
# ---------2:查询多个结果---------------
books = BookInfo.objects.all()
# ---------3:查询多个结果数量---------------
book_count = BookInfo.objects.all().count()
book_count = BookInfo.objects.count()

# 过滤查询
# ----------查询编号为1的图书
BookInfo.objects.get(id__exact=1)
BookInfo.objects.filter(id=1)
# ----------查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# ----------查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# ----------查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# ----------查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])
# ----------查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# ----------查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# ----------查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

#################F对象################
from django.db.models import F
#查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount'))

#################Q对象################
#查询阅读量大于20，并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20,id__lt=3)
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
#查询阅读量大于20的图书
from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20))
#查询阅读量大于20，或编号小于3的图书
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
#查询编号不等于3的图书
BookInfo.objects.filter(~Q(id=3))

#################聚合函数################
from django.db.models import Sum
#查询图书的总阅读量
BookInfo.objects.aggregate(Sum('readcount'))

#################排序################
#升序
BookInfo.objects.all().order_by('readcount')
#降序
BookInfo.objects.all().order_by('-readcount')

#################级联查询################
#由一到多
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
#由多到一
person = PeopleInfo.objects.get(id=6)
person.book
#查询图书，要求图书人物为"郭靖"
book = BookInfo.objects.filter(peopleinfo__name='郭靖')
#查询图书，要求图书中人物的描述包含"八"
book = BookInfo.objects.filter(peopleinfo__description__contains='八')
#查询书名为“天龙八部”的所有人物
people = PeopleInfo.objects.filter(book__name='天龙八部')
#查询图书阅读量大于30的所有人物
people = PeopleInfo.objects.filter(book__readcount__gt=30)


