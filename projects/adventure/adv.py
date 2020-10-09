from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Fill traversal path ##############################

def get_room(room, direction):
    if direction in room_graph[room][1]:
        return room_graph[room][1][direction]

def reverse_direction(direction):
    if direction == "n":
        return "s"
    if direction == "e":
        return "w"
    if direction == "s":
        return "n"
    if direction == "w":
        return "e"

def go(room, direction, backing=False):
    next_room = get_room(room, direction)
    room_map[room][direction] = next_room
    if next_room is not None:
        # move to the room, map exits for each room, keep a backup trail, log to visited
        room_map[next_room][reverse_direction(direction)] = room
        traversal_path.append(direction)
        visited.add(next_room)
        if not backing:
            backup.append(reverse_direction(direction))
        return next_room
    else:
        return room

room_map = dict()

for i in range(len(room_graph)):
    room_map[i] = {"n": "?", "e": "?", "s": "?", "w": "?"}

visited = set()
backup = []
room = 0
visited.add(room)

while len(visited) < 500:
    if "?" in room_map[room].values():
        if room_map[room]['n'] == "?":
            room = go(room, 'n')
        elif room_map[room]['e'] == "?":
            room = go(room, 'e')
        elif room_map[room]['s'] == "?":
            room = go(room, 's')
        else:
            room = go(room, 'w')
    else:
        back = backup[-1]
        backup.pop()
        room = go(room, back, True)

#################################

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
