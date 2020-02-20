import random

import itertools


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i + 1}')

        # # Create friendships
        # possible_friendships = []
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))

        # random.shuffle(possible_friendships)

        total_friendships = num_users * avg_friendships // 2
        # random_friendships = possible_friendships[:total_friendships]

        for i in range(total_friendships):
            user_a = random.randint(1, num_users)
            user_b = random.randint(1, num_users)
            if user_a != user_b and user_a not in self.friendships[user_b] and user_b not in self.friendships[user_a]:
                self.add_friendship(user_a, user_b)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:
            path_to_current_user = queue.dequeue()
            current_user = path_to_current_user[-1]
            if current_user not in visited:
                visited[current_user] = path_to_current_user
                for friend in self.friendships[current_user]:
                    path_to_friend = [*path_to_current_user, friend]
                    queue.enqueue(path_to_friend)

        return visited

    def friends_info(self, user_id):
        extended_network = self.get_all_social_paths(user_id)
        users_in_network = len(extended_network) - 1
        other_users = len(self.users) - 1
        percent_in_network = 100 * users_in_network / other_users
        print('Extended Network:', users_in_network)
        print('Number of Other Users:', other_users)
        print('Percentage of Other Users in Network:', percent_in_network)

    def average_degree_of_separation(self, user_id):
        extended_network = self.get_all_social_paths(user_id)
        total_degrees_of_separation = 0
        users_in_network = len(extended_network) - 1
        for (key, value) in extended_network.items():
            if key != user_id:
                total_degrees_of_separation += len(value) - 1
        return total_degrees_of_separation / users_in_network


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)
    sg.friends_info(1)
    print(sg.average_degree_of_separation(1))
