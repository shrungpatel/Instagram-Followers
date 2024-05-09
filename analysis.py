import json

following = open('following.json')
data = json.load(following)
following_set = set()
for person in data['relationships_following']:
    following_set.add(person['string_list_data'][0]['value'])
following.close()

followers = open('followers_1.json')
data = json.load(followers)
followers_set = set()
for person in data:
    followers_set.add(person['string_list_data'][0]['value'])
followers.close()

print(following_set.difference(followers_set))
