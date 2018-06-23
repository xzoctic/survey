class ToDo(): #blueprint for your objects e.g. house plan
    def __init__(self, description, time, additional_info):  #function of the object
        #special function, BUILD THE HOUSE, (self, description, time, additional_info) - properties of the house
        #pass in the properties to build the house

        self.id = id(self) # the id(self) assigns the object a unique ID, 
        # which will not be repeated again
        self.description = description # properties of the objects
        self.time = time #self. means "this object"
        self.additional_info = additional_info
        self.done = False

    def mark_as_done(self): #functions e.g. actions you can do on your house
        self.done = True

    def get_description(self): 
        return self.description 

    def get_time(self):
        return self.time

    def get_status(self):
        return self.done

    def get_id(self):
        return self.id

    def get_additional_info(self):
        return self.additional_info 
