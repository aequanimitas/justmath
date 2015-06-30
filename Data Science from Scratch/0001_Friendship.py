from __future__ import division

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue", },
    { "id": 3, "name": "Chi", },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
]

# user with id "0" is a friend of user with id "2"
# look at first tuple
friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

# since each "user" is a dict
# augmenting it is easy
# and this was a seperate for loop too
for user in users:
    user["friends"] = []

for i, j in friendships:
# "i" is not an index here
    users[i]["friends"].append(users[j]);
    users[j]["friends"].append(users[i]);

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)

avg_connections = total_connections / num_users

# number of friends by id
# list comprehension using the for loop
#
# for each element in "users" array
# store the "user" id and the return value of the procedure number_of_friends()
# into a tuple
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# the sorted HOP takes an iterable, which in this case is an array of tuples
# and for each tuple, a lambda is used to catch the values that are stored in the tuple
# and returns the number of friends, which it then uses as the key for sorted
#
# the reverse argument tells the sorted procedure to order the elements in a decreasing
# way
#
# the result shows the users who are "central" to the network
# this is also called as the network metric degree centrality
nfbi = sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends,
              reverse=True)

# mf: mutual_friends
# this is a bad function
# shows repeatedly user ids
def mf_bad(user):
  return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

# let's make it right
from collections import Counter
def not_the_same(user, other_user):
    return user["id"] != other_user["id"]
