class Food():
    def __init__(self, name, cuisine, price, availability, spicy):  #function of the object
            #special function, BUILD THE HOUSE, (self, description, time, additional_info) - properties of the house
            #pass in the properties to build the house

            self.id = id(self) # the id(self) assigns the object a unique ID, 
            # which will not be repeated again
            self.name = name # properties of the objects
            self.cuisine = cuisine #self. means "this object"
            self.price = price
            self.availability= availability
            self.spicy = spicy

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_cuisine(self): 
        return self.cuisine 

    def get_price(self):
        return self.price

    def get_availability(self):
        return self.availability

    def get_spicy(self):
        return self.spicy

