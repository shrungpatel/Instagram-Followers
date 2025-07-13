def get_list_of_people(file):
    """
    Reads a file and returns a list of usernames.
    The file is expected to have usernames on even lines.
    """
    start_line = 5 if file.endswith('followers.txt') else 7
    with open(file, 'r') as f:
        lines = f.read().splitlines()[start_line:]  # Skip the first few lines with the header
        # the file has "username url \n date \n" format
        return [lines[i].split()[0] for i in range(len(lines)) if i % 2 == 0 and lines[i] != '']

followers = get_list_of_people('followers.txt')
following = get_list_of_people('following.txt')
following_but_not_following_back = set(following) - set(followers)
print(following_but_not_following_back, len(following_but_not_following_back))