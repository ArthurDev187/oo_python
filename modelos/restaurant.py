class Restaurant:
      def __init__(self, name, category):
            self.name = name
            self.category = category
            self.active = False
      
      def __str__(self):
            return (f'''
            Restaurant name: {self.name};
            Restaurant category: {self.category};
            Restaurant status: {'active' if self.active == True else 'inactive'}.\n
            ''')
      

    
restaurant_1 = Restaurant('Bistro', 'Italian')
restaurant_2 = Restaurant('Pizzeto', 'Pizza')

print(restaurant_1)
print(restaurant_2)

restaurant_1.active = True

print(restaurant_1)