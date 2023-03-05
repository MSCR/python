def build_profile(first, last, **user_info):
    """Buld a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['second_name'] = last

    return user_info

user_profile = build_profile('manuel','cortes',
                            location = 'queretaro',
                            field = 'engineering',
                            age = 32,
                            county = 'mexico')

print(user_profile)