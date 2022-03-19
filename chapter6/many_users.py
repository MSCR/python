users = {
    'aeinstein':{
        'first':'albert',
        'second':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'second':'curie',
        'location':'paris',       
    },
}

for user,usr_info in users.items():
    print(f"\nUsername: {user}")
    full_name = f"{usr_info['first'].title()} {usr_info['second'].title()}"
    location = f"{usr_info['location'].title()}"

    print(f"{full_name}")
    print(f"{location}")