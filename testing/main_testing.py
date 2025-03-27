import re 

def find_time(user):
    match = re.search(r"(\d+)\s*(hours?|minutes?|seconds?)", user, re.IGNORECASE)
    print(match)

user = input()
find_time(user)