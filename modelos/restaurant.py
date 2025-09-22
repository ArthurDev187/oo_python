class Restaurant:
      def __init__(self, name, category):
            restaurants = []
            self.name = name
            self.category = category
            self._active = False
            restaurants.append(self)
      
      def __str__(self):
            return (f'''
            Restaurant name: {self.name};
            Restaurant category: {self.category};
            Restaurant status: {'active' if self._active == True else 'inactive'}.\n
            ''')
            
            
      @classmethod
      def list_restaurants(cls):
            print(f'{'Restaurant name'.ljust(25)}| {'Category'.ljust(25)}| {'Active'}')
            for restaurant_temp in cls.restaurants:
                  print(f'{restaurant_temp.name.ljust(25)}| {restaurant_temp.category.ljust(25)}| {restaurant_temp.active}')
      
      
      @property
      def active(self):
            return '✔' if self._active else '✘'
      
      def alternar_status(self):
            self.active = not self.active
      
      
      

    
restaurant_1 = Restaurant('Bistro', 'Italian')
restaurant_2 = Restaurant('Pizzeto', 'Pizza')

Restaurant.list_restaurants()