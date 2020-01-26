import math
import sys
import webbrowser
import clipboard


#Val is any variable from iphone shortcuts

#print(val)
##################### DATA PROCESSING #################


class Data:
    def __init__(self):
        self.destination = str
        self.long = float
        self.lat = float
        
######## TEST FILE 1 ########
        
def cord_distance(user_loc, data):
    delta_long = user_loc.long - data[0]
    delta_lat = user_loc.lat - data[1]
    dist = math.sqrt(delta_long*delta_long + delta_lat*delta_lat)
    return dist
       
clipboard_input = clipboard.get()
#clipboard_input = "key key -82.83708492093993 34.6759872941903"
curr_loc = Data()
dest_0, dest_1, curr_loc.long, curr_loc.lat = clipboard_input.split()
curr_loc.destination = dest_0, dest_1
curr_loc.long = float(curr_loc.long)
curr_loc.lat = float(curr_loc.lat)

#Room to Waypoint ID Conversion

availableRooms = {"Staircase North": 'A',
                  "Elevator North": 'A',
                  "Room 335": 'B',
                  'Room 329': 'D',
                  'Room 331': 'D',
                  'Room 333': 'D',
                  'Room 327': 'D',
                  'Room 325': 'D',
                  'Room 316': 'C',
                  'Room 310': 'C',
                  'Room 319': 'F',
                  'Room 321': 'F',
                  'Room 323': 'F',
                  'Room 315': 'F',
                  'Room 308': 'E',
                  'Room 309': 'H',
                  'Room 313': 'H',
                  "Staircase South": 'I',
                  "Elevator South": 'I',
                  "Room 301": 'J',
                  "Room 303": 'J'}

destinationWaypoint = availableRooms[curr_loc.destination]

IDs = ['A','B','C', 'D','E','F', 'G','H','I','J']
watt_data = {'A': [ -82.83704861002522, 34.67620743066132],
             'B': [ -82.83708038125262, 34.67618073126286],
             'C': [ -82.83710728548732, 34.676121477791185],
             'D': [ -82.83709805523982, 34.67610798081648],
             'E': [ -82.83710268693474, 34.67605528867775],
             'F': [ -82.83709023356549, 34.67605226413455],
             'G': [ -82.83709703224152, 34.67602562033484],
             'H': [ -82.83708110357719, 34.675988789525],
             'I': [ -82.83708479743133, 34.67603639187172],
             'J': [ -82.83708043563308, 34.675995941443766] }
    


for i in range(1,10):
    print(watt_data[IDs[i-1]][0])
    print(watt_data[IDs[i-1]][1])
    
#GIVEN DISTANCE
min_distance = 1000
min_key = None
for key in IDs:
    temp_dist = cord_distance(curr_loc, watt_data[key])
    if temp_dist < min_distance:
        min_distance = temp_dist
        waypoint = key
        
print(waypoint)

################# END OF DATA PROCESSING ##############

#print(sys.argv[1])

clipboard.set("You are closest to waypoint " + waypoint + " and you would like to go to waypoint " + destinationWaypoint)

webbrowser.open("shortcuts://")

