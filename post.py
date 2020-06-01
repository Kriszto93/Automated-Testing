class Post:
    def __init__(self,title,content):
        self.title = title
        self.content = content

    def json(self): #Java Script Object Notation (JSON), commonly used to transfer data, used database and API
        return {
            'title': self.title,
            'content': self.content,

        }
