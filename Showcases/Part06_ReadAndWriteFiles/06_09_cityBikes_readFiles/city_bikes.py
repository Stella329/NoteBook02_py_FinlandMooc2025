# Write your solution here
import math

# part 1: Distance between stations

def get_station_data(filename: str) -> dict:
    '''This function should read the names and locations of all the stations in the file, and return them in a dictionary'''
    with open (filename) as file:
        data = {}
        for line in file:
            cells = line.split(';')     #csv分隔符; return a list
            if cells[0] == 'Longitude':
                continue                # 跳过header（不是pass）
            name = cells[3].strip()     # 删除cell内空格
            long = cells[0].strip()
            lati = cells[1].strip()
            data[name]= (float(long),float(lati))
    return data


def distance(stations: dict, station1: str, station2: str):
    '''returns the distance between the two stations given as arguments.
    The distance is calculated using the Pythagorean theorem '''

    ''' NB: The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.'''
    x = (float(stations[station1][0]) - float(stations[station2][0])) * 55.26
    y = (float(stations[station1][1]) - float(stations[station2][1])) * 111.2
    distance = math.sqrt(x**2 + y**2)

    return distance



# part2: The greatest distance
def greatest_distance(stations: dict)->tuple:
    '''works out the two stations on the list with the greatest distance from each other. 
    The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.'''

    max_distance = 0
    station1 = ""
    station2 = ""

    for item1 in stations.items():
        i1 = item1[0]
        
        for item2 in stations.items():
            i2 = item2[0]
            d = distance(stations, i1, i2)

            if d > max_distance:
                station1 = item1[0]
                station2 = item2[0]
                max_distance = d

    return station1, station2, max_distance




# test
if __name__ == "__main__":
    # stations = get_station_data('stations1.csv')
    # d = distance(stations, "Designmuseo", "Hietalahdentori")
    # print(d)
    # d = distance(stations, "Viiskulma", "Kaivopuisto")
    # print(d)

    stations = get_station_data('stations1.csv')
    # greatest_distance(stations)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)


