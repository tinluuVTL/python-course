# usernames = ["johndoe", "janedoe", "bob"]
# passwords = ["secret", "12345", "hunter2"]

# # users = list(zip(usernames, passwords))
# users = dict(zip(usernames, passwords))

# print(type(users))

# for k,v in users.items():
#     print(k,v)


usernames = ["johndoe", "janedoe", "bob"]
passwords = ["secret", "12345", "hunter2"]
login_date = ["2020-01-01", "2020-01-02", "2020-01-03"]

users = list(zip(usernames, passwords, login_date))

for user in users:
    print(user)


