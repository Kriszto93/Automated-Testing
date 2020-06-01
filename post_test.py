from unittest import TestCase #TestCase is part of the unittest library
from post import Post

class PostTest(TestCase): #This is a test case
    def test_create_post(self):# kell a tesztelés objektuma
        p = Post('Test', 'Test content') # Ezzel kreáltunk egy új posztot, aminek van címe (title) és kontentje (content)
        # 'Post' is an object
        self.assertEqual('Test',p.title) #itt használjuk a 'TestCase' API-t, ami egy 'self object' és amit örököltünk a 'TestCase'-ből
        self.assertEqual('Test content', p.content) #'TestCase' megbizonyosodik, hogy a str 'Test' és a
        # post title (p = Post('Test', 'Test content')), amit kreáltunk az ugyanaz e
        #MAKING SURE THAT THE PROPERTIES MATCH!
    def test_json(self):
        p = Post('Test', 'Test content')
        expected = {'title': 'Test', 'content': 'Test content'}

        self.assertDictEqual(expected, p.json())

