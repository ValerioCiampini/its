cities:dict = {"Rome":{"country":"Italy", "population":"2000000", "fact":"a"}, "Milan":{"country":"Italy", "population":"1000000", "fact":"b"}, "Berlin":{"country":"Germany", "population":"1500000", "fact":"c"}}

for key, value in cities.items():
    print(f"{key}:\n{value}")