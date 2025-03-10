people:dict = {"Erik":{"name":"Erik", "surname":"Wilson", "age":20, "city":"Liverpool"}, "Mark":{"name":"Mark", "surname":"Jonhson","age":24, "city":"Cardiff"}, "Marie":{"name":"Marie", "surname":"Gibbs", "age":18, "city":"Manchester"}}

for key, value in people.items():
    print(f"{key}:\n{value}")