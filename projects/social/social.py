import math, random

class User:
    def __init__(self, name):
        self.name = name

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
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        q = [[user_id]]
        while q:
            path = q.pop(0)
            node = path[-1]
            if node not in visited:
                visited[node] = path
                for friend in self.friendships[node]:
                    if friend not in visited:
                        q.append(path + [friend])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    
    people = 1000
    friends_each = 5
    total_percent = 0
    total_degrees = 0
    iterations = 100
    longest = 0

    for i in range(iterations):
        sg.populate_graph(people, friends_each)
        connections = sg.get_all_social_paths(1)
        total_percent += len(connections)
        total_connection_len = 0
        for each in connections:
            if len(connections[each]) > longest:
                longest = len(connections[each])
            total_connection_len += len(connections[each])
        avg_connection_len = total_connection_len / people
        total_degrees += avg_connection_len

    total_percent /= (10 * iterations)
    total_degrees /= iterations

    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    # print(len(connections))
    print("Test iterations: ", iterations)
    print("People: ", people)
    print("Friends: ", friends_each)
    print(f"{total_percent}%")
    print(f"{total_degrees} avg degrees")
    print(f"{longest} most degrees")