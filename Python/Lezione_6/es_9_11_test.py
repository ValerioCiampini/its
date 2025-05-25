from es_9_11 import User, Privileges, Admin

u:User = User("a", "b", "c", "d")
p:Privileges = Privileges()
a:Admin = Admin(u, p)

a.user.describe_user()
print(a.privileges.show_privileges())