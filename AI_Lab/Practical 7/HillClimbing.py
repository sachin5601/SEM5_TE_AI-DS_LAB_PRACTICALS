import random

def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i - 1]] for i in range(len(tour)))

def hill_climbing(distance_matrix):
    num_cities = len(distance_matrix)
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    current_distance = total_distance(current_tour, distance_matrix)

    while True:
        neighbors = []
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                # Create a neighbor by swapping two cities
                neighbor = current_tour[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)

        # Find the neighbor with the minimum distance
        next_tour = min(neighbors, key=lambda tour: total_distance(tour, distance_matrix))
        next_distance = total_distance(next_tour, distance_matrix)

        # If no better neighbor is found, exit the loop
        if next_distance >= current_distance:
            break

        current_tour, current_distance = next_tour, next_distance

    return current_tour, current_distance

# Distance matrix representing the distances between cities
distance_matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

# Running the hill climbing algorithm
best_tour, best_distance = hill_climbing(distance_matrix)
print("Best tour:", best_tour)
print("Best distance:", best_distance)



'''Function total_distance(tour, distance_matrix):
    Return the sum of distances for the given tour

Function hill_climbing(distance_matrix):
    Initialize current_tour with city indices
    Randomly shuffle current_tour
    Calculate current_distance for the shuffled tour

    While True:
        Initialize an empty list for neighbors
        For each pair of cities (i, j):
            Create a neighbor tour by swapping cities i and j
            Add the neighbor to the neighbors list

        Find the neighbor with the minimum distance
        If the minimum distance is not better than current_distance:
            Break the loop

        Update current_tour and current_distance with the best neighbor

    Return current_tour and current_distance
'''