class BlogPost(): #blueprint for your objects e.g. house plan
    def __init__(self, title, text, date, author):  #function of the object
      
        self.id = id(self) # the id(self) assigns the object a unique ID, 
        # which will not be repeated again
        self.title = title # properties of the objects
        self.text = text #self. means "this object"
        self.date = date
        self.author = author
      
    def get_text(self):
        return self.text  

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id

    def change_text(self, text): #this allows the user to modify (overwrite) a previous blog post
        self.text = text

    def change_title(self, title):
        self.title = title

    def change_date(self, date):
        self.date = date

    def change_author(self, author):
        self.author = author

    

