import random
import csv
from collections import defaultdict

# Step 1: Load city names from the city_names.txt file
with open("city_names_list.txt", "r") as file:
    city_names = [line.strip() for line in file.readlines()]
city_names = list(dict.fromkeys(city_names))

# Step 2: Select 200 cities
selected_cities = random.sample(city_names, 200)


# Step 3: Generate unique city connections
num_edges = 3000
connections = []  # To store unique city pairs
data = []

for city in selected_cities:
    new_list = [c for c in selected_cities if c != city]
    random_city = random.choice(new_list)

    #Adding incoming connection per city
    while (city, random_city) in connections or (random_city, city) in connections:
        random_city = random.choice(new_list) #Ensuring no duplicate connections
    distance = random.randint(50, 2000)
    connections.append((city, random_city))
    data.append((city, random_city, distance))
    
    #Adding outgoing connection per city
    random_city = random.choice(new_list)
    while (city, random_city) in connections or (random_city, city) in connections:
        random_city = random.choice(new_list) #Ensuring no duplicate connections
    distance = random.randint(50, 2000)
    connections.append((random_city, city))
    data.append((random_city, city, distance))

    new_list = selected_cities #resetting new_list

#Adding additional connections
while len(connections) < num_edges:
    city1, city2 = random.sample(selected_cities, 2)
    distance = random.randint(50, 2000)

    # Ensuring no duplicate connections
    if (city1, city2) not in connections and (city2, city1) not in connections:
        connections.append((city1, city2))
        data.append((city1, city2, distance))



# Step 5: Validating the dataset

#Verify there are exactly 3000 unique connections in your dataset.
total_connections = len(connections)
print("Dataset has ", len(data), "unique connections.")

#Confirm that the average total (incoming + outgoing) is around 15 connections per city.
connections_count = defaultdict(int)

for city1, city2, distance in data:
    connections_count[city1] += 1  # Outgoing connection
    connections_count[city2] += 1  # Incoming connection

unique_cities = len(selected_cities)
average_connections = total_connections / unique_cities

print(f"Average total connections per city: {average_connections}")

#Show that your dataset contains no repeated city pairs or self-loops.
def check_no_repeats_or_loops(connections):
    normalized_connections = set()
    for city1, city2 in connections:
        if city1 == city2:
            return "Self-loop detected at: ({}, {})".format(city1, city2)
        # Normalize pairs to ensure (city1, city2) is the same as (city2, city1)
        pair = tuple(sorted((city1, city2)))
        if pair in normalized_connections:
            return "Duplicate connection detected: {}".format(pair)
        normalized_connections.add(pair)
    return "No duplicates or self-loops found."

result = check_no_repeats_or_loops(connections)
print(result)

#Ensure every city is part of the network (no isolated nodes).
def check_all_cities_connected(connections):
    # Extract all cities from the connections
    cities = set(city for pair in connections for city in pair)
    # Build the network graph
    network_graph = {city: set() for city in cities}
    for city1, city2 in connections:
        network_graph[city1].add(city2)
        network_graph[city2].add(city1)
    
    # Check for isolated nodes
    isolated_cities = [city for city, neighbors in network_graph.items() if not neighbors]
    if isolated_cities:
        return "Isolated cities found: {}".format(isolated_cities)
    return "No isolated cities. All cities are part of the network."

result = check_all_cities_connected(connections)
print(result)



# Step 6: Write the generated connections to a new CSV file
output_file = "road_network.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["city1", "city2", "distance"])

    # Write the selected city pairs with distances
    for city1, city2, distance in data:
        writer.writerow([city1, city2, distance])

print(f"Dataset generated and saved to {output_file}.")
