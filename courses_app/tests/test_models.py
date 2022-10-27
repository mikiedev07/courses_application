from django.test import TestCase
from courses_app.models import Category


class CoursesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="Category_test", imgpath="some_path")

    def test_name_label(self):
        c = Category.objects.get(id=1)
        field_label = c._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_imgpath_label(self):
        c = Category.objects.get(id=1)
        field_label = c._meta.get_field('imgpath').verbose_name
        self.assertEqual(field_label, 'imgpath')

    def test_name_max_length(self):
        c = Category.objects.get(id=1)
        max_length = c._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)
