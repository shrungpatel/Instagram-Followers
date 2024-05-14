import json
following_set = {person['string_list_data'][0]['value'] for person in json.load(open('following.json'))['relationships_following'] }
followers_set = {person['string_list_data'][0]['value'] for person in json.load(open('followers_1.json')) }
print(following_set.difference(followers_set))
