"""
DFS(u):
    mark u as "Explored" and add it to R

    for each edge (u, v) incident to u:
        if v is not marked "Explored":
            call DFS(v) recursively
        endIf
    endFor
"""