from django.test import TestCase

# Create your tests here.
from student.models import Student


class StudentTestCase(TestCase):
    def setUp(self) -> None:
        Student.objects.create(
            name = 'haha',
            sex = 1,
            email = '123456789@qq.com',
            profession='leader',
            qq='333121',
            phone='32222',
            status='2'
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='haha',
            sex=1,
            email='123456789@qq.com',
            profession='leader',
            qq='333121',
            phone='32222',
            status='1'
        )
        self.assertEqual(student.sex_show, '男', '性别字段不一致')
