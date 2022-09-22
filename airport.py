class Airport(object):
    name: str
    neighbors: list['Airport']
    def __init__(self, name: str):
        self.name = name
        self.neighbors = []

def dfs(path: list[Airport], length: int) -> bool:
    cur_airport = path[-1]
    neighbors = cur_airport.neighbors.copy()
    for neighbor in neighbors:
        cur_airport.neighbors.remove(neighbor)
        path.append(neighbor)
        if dfs(path, length):
            return True
        path.remove(neighbor)
        cur_airport.neighbors = neighbors
    if len(path) == length:
        return True
    return False

def setup(tickets: list[list[str]]) -> list[str]:
    airports: dict[str, Airport] = {}
    for airport_from, airport_to in tickets:
        if airport_from not in airports:
            airports[airport_from] = Airport(airport_from)
        if airport_to not in airports:
            airports[airport_to] = Airport(airport_to)
        airports[airport_from].neighbors.append(airports[airport_to])
    for airport in airports.values():
        airport.neighbors.sort(key=lambda airport: airport.name)
    for airport in airports.values():
        cur_path = [airport]
        if dfs(cur_path, len(tickets) + 1):
            return [airport.name for airport in cur_path]
    raise ValueError('No possible path found!')

if __name__ == '__main__':
    print(setup([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))