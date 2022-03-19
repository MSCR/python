cities = {
    'queretaro':{
        'country':'mexico',
        'population':1_005_000_000,
        'fact':'quiet',
    },
    'austin':{
        'country':'united states',
        'population':950_807,
        'fact':'festival',   
    },
    'tokio':{
        'country':'japan',
        'population':13_960_000_000,
        'fact':'anime',
    },
}

for place,info in cities.items():
    print(f"\nAbout {place.title()} information:")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact'].title()}")