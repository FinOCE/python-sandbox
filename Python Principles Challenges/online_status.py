def online_count(dict):
    return len([person for person in dict if dict[person] == "online"])

print(online_count({"Alice": "online", "Bob": "offline", "Eve": "online"}))