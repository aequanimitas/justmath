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
# for each element in "users" array:
# - store the "user" id and the return value of the procedure number_of_friends()
#   into a tuple
# - number_of_friends is just a wrapper for getting a friend's friend count
# then append it into the array
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# sorted 
# - HOP 
# - takes an iterable as 1st argument, which in this case is an array of tuples
# lambda
# - for each tuple, the lambda is used to catch the values that are stored in the tuple
# and returns the number of friends, which it then uses as the key for sorted
#
# the reverse argument tells the sorted procedure to order the elements in a decreasing
# way
#
# the result shows the users who are "central" to the network
# this is also called as the network metric degree centrality
nfbi = sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends,
              reverse=True)

# this is not mutual friends, this is just friends of each of your friend
# this is a bad function
# shows repeatedly user ids
def friends_of_friend_ids_bad(user):
    return [foaf["id"] 
              for friend in user["friends"] 
                  for foaf in friend["friends"]]

def fofib(user):
    return friends_of_friend_ids_bad(user)

# let's make it right
from collections import Counter
def not_the_same(user, other_user):
    """ 
    check if two users have same ids
    this is only a utility function
    """
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """ compare via ids, if it exists in the list """
    """ all: returns if all items on an iterable passes the condition """
    return all(not_the_same(friend, other_user)
                  for friend in user["friends"])

# Counter
# - unordered collection where elements are stored as dictionary keys and their counts are
#   stored as dictionary values
# - Counts are allowed to be any integer value including zero or negative counts
# - a dict subclass
def friends_of_friend_ids(user):
    return Counter(foaf["id"] for friend in user["friends"]
                              for foaf in friend["friends"]
                                  if not_the_same(user, foaf) and not_friends(user, foaf))

# (id, interest)
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"),
    (0, "Cassandra"),
    (1, "NoSQL"),
    (1, "MongoDB"),
    (1, "Cassandra"),
    (1, "HBase"),
    (1, "Postgres"),
    (2, "Python"),
    (2, "scikit-learn"),
    (2, "scipy"),
    (2, "numpy"),
    (2, "statsmodels"),
    (2, "pandas"),
    (3, "R"),
    (3, "Python"),
    (3, "statistics"),
    (3, "regression"),
    (3, "probability"),
    (4, "machine learning"),
    (4, "regression"),
    (4, "decision trees"),
    (4, "libsvm"),
    (5, "Python"),
    (5, "R"),
    (5, "Java"),
    (5, "C++"),
    (5, "Haskell"),
    (5, "programming languages"),
    (6, "statistics"),
    (6, "probability"),
    (6, "mathematics"),
    (6, "theory"),
    (6, "machine learning"),
    (7, "scikit-learn"),
    (7, "Mahout"),
    (7, "neural networks"),
    (8, "neural networks"),
    (8, "deep learning"),
    (8, "Big Data"),
    (8, "artificial intelligence"),
    (9, "Hadoop"),
    (9, "Java"),
    (9, "MapReduce"),
    (9, "Big Data")
]

# this will work for lists with small data
def data_scientists_who_likes(interest):
    return [user_id for user_id, user_interest in interests
                        if user_interest == interest]

# optimize
from collections import defaultdict
# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id 
                       for interest in interests_by_user_id[user["id"]]
                       for interested_user_id in user_ids_by_interest[interest]
                       if interested_user_id != user["id"])

# the plot of this data will be available in chapter 3
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                       (48000, 0.7), (76000, 6),
                       (69000, 6.5), (76000, 7.5),
                       (60000, 2.5), (83000, 10),
                       (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# this doesn't work, this just reports each scientist's salary
average_salary_by_tenure = {
    tenure: sum(salaries)/ len(salaries) for tenure, salaries in salary_by_tenure.items()
}

# it might be more helpful if we bucket by tenure
# bucket == group
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than 5"

# now using the tenure_bucket as an identifier
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# our choice here on grouping is arbitrary/eyeballed (look at the tenure_bucket function)
average_salary_by_bucket = {
    tenure: sum(salaries)/ len(salaries) 
    for tenure, salaries in salary_by_tenure_bucket.iteritems()
}

words_and_counts = Counter(word for user, interest in interests
                                 for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print word, count
