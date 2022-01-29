def tower_of_hanoi(disc, from_tower, using_tower, to_tower):
    """
    Always use this general idea
    1. Move n-1 disc from A to B using C
    2. Move disc from A to C
    3. Move n-1 disc from B to C using A
    """
    if disc >= 1:
        tower_of_hanoi(disc-1, from_tower, to_tower, using_tower)
        print(f'Move top disc from {from_tower} to {to_tower}')
        tower_of_hanoi(disc-1, using_tower, from_tower, to_tower)


tower_of_hanoi(3, 'A', 'B', 'C')