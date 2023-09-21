with open("fileprocessor.input", "r") as file:
    user_data = []
    for line in file:
         if not line.startswith("#"):
             parts = line.strip().split(':')
             if len(parts) >= 4:
                 username = parts[0].strip()
                 password = parts[1].strip()
                 userid = parts[2].strip()
                 groupid = parts[3].strip()

                 user_data.append((username, password, userid, groupid))

print("Printing out User Data:")
for user in user_data:
    username, password, userid, groupid = user
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")


