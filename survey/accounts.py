class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.todo_items = []
        self.blog_posts = []
        

    def add_item_to_do(self, todo_item):
        self.todo_items.append(todo_item)

    def add_blog_post(self, blog_post):
        self.blog_posts.append(blog_post)
    
    def get_todo_items(self):
        return self.todo_items

    def get_blog_posts(self):
        return self.blog_posts

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password