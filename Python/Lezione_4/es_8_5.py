def describe_city(name_city:str, name_country:str = "Italy"): 
    print(f"{name_city} is in {name_country}")

describe_city("Roma")
describe_city("Firenze")
describe_city("Bruxelles", "Belgium")
