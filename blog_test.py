from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.post)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)') #b.__repr__() itt implementáltuk be
        self.assertEqual(b2.__repr__(), 'My day by Rolf (0 posts)')

    def test_repr_multiples_posts(self):
        b = Blog('Test', 'Test Author')
        b.post = ['Test']
        b2 = Blog('My day', 'Rolf')
        b2.post = ['Test','another']

        self.assertEqual(b.__repr__(),'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My day by Rolf (2 posts)')







