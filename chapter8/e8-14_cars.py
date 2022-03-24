def make_car(manufacture, model, **car_info):
    """This function makes a car"""
    car_info['manufacture'] = manufacture
    car_info['model'] = model
    return car_info

# My car
car = make_car('Honda', 'Civic', color='gray', year=2002)
print(car)

# Mom's car
car = make_car('Nissan', 'Versa', misc='Luxury', tow_package=True)
print(car)
