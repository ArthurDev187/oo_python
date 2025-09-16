class Restaurant:
    name = ''
    category = ''
    active = False
    
restaurant_1 = Restaurant()
restaurant_1.name = 'BaysWater'
restaurant_1.category = 'Italian'
restaurant_1.active = False


restaurant_1.name = 'Bistro'

print(f'''
      Restaurant name: {restaurant_1.name};
      Restaurant category: {restaurant_1.category};
      Restaurant status: {'active' if restaurant_1.active == True else 'inactive'}.\n
      ''')


restaurant_2 = Restaurant()
restaurant_2.name = 'Pizzeto'
restaurant_2.category = 'Pizza'
restaurant_2.active = True

print(f'''
      Restaurant name: {restaurant_2.name};
      Restaurant category: {restaurant_2.category};
      Restaurant status: {'active' if restaurant_2.active == True else 'inactive'}.\n
      ''')