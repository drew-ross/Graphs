def earliest_ancestor(ancestors, starting_node):
    ad = dict()
    all_paths = []

    for t in ancestors:
        if t[0] not in ad:
            ad[t[0]] = []
        ad[t[0]].append(t[1])

    for v in ad:
        q = []
        q.append([v])
        while q:
            path = q.pop(0)
            if path[-1] == starting_node:
                all_paths.append(path)
                break
            elif path[-1] in ad:
                for node in ad[path[-1]]:
                    q.append(path + [node])
            
    print(all_paths)

    # get only longest paths
    all_paths = [
        path for path in all_paths if len(path) == max(len(path) for path in all_paths)
    ]

    # get lowest value ancestor
    ancestor = min([path[0] for path in all_paths])
    
    # return -1 if no answer
    if ancestor == starting_node:
        ancestor = -1

    return ancestor


test_ancestors = [
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (8, 9),
    (11, 8),
    (10, 1),
]
print(earliest_ancestor(test_ancestors, 10))