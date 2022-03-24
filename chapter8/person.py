# A function can return any kind of data, from list to dictionaries.
def build_person(first_name,last_name,age=None):
    """Return a dictionary of information about a person"""
    person = {'first':first_name,'last':last_name}
    # NOTE: None is represented as a False in conditional test
    if age:
        person['age']=age
    return person

musician = build_person('jimmy','hendrix',27)
print(musician)

musician = build_person("jhon","hooker",)
print(musician)