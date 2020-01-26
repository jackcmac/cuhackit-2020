import numpy as np
import math
import pyproj

def latlong_to_3d(latr, lonr):
    """Convert a point given latitude and longitude in radians to
    3-dimensional space, assuming a sphere radius of one."""
    return np.array((
        math.cos(latr) * math.cos(lonr),
        math.cos(latr) * math.sin(lonr),
        math.sin(latr)
    ))

def angle_between_vectors_degrees(u, v):
    """Return the angle between two vectors in any dimension space,
    in degrees."""
    return np.degrees(
        math.acos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))))

# The points in tuple latitude/longitude degrees space
A = (-82.83707404144522, 34.67597218057034)
B = (-82.83708190352426, 34.67603521356209)
C = (-82.83709584891056, 34.67603192723286)

# Convert the points to numpy latitude/longitude radians space
a = np.radians(np.array(A))
b = np.radians(np.array(B))
c = np.radians(np.array(C))

# Vectors in latitude/longitude space
avec = a - b
cvec = c - b

# Adjust vectors for changed longitude scale at given latitude into 2D space
lat = b[0]
avec[1] *= math.cos(lat)
cvec[1] *= math.cos(lat)

# # Find the angle between the vectors in 2D space
# angle2deg = angle_between_vectors_degrees(avec, cvec)
#
#
# # The points in 3D space
# a3 = latlong_to_3d(*a)
# b3 = latlong_to_3d(*b)
# c3 = latlong_to_3d(*c)
#
# # Vectors in 3D space
# a3vec = a3 - b3
# c3vec = c3 - b3
#
# # Find the angle between the vectors in 2D space
# angle3deg = angle_between_vectors_degrees(a3vec, c3vec)
#
#
# # Print the results
# print('\nThe angle ABC in 2D space in degrees:', angle2deg)
# print('\nThe angle ABC in 3D space in degrees:', angle3deg)

def calculate_angle(point_a, point_b):
    """ Calculate angle between two points """
    ang_a = np.arctan2(*point_a[::-1])
    ang_b = np.arctan2(*point_b[::-1])
    return np.rad2deg((ang_a - ang_b) % (2 * np.pi))

angleResult = calculate_angle(avec, cvec)
print('angleResult = ', angleResult)
if angleResult < 135:
    print('go right')
elif angleResult < 225:
    print('go straight')
else:
    print('go left')



geod = pyproj.Geod(ellps='WGS84')

lat0, lon0 = A
lat1, lon1 = B

azimuth1, azimuth2, distance = geod.inv(lon0, lat0, lon1, lat1)
print('distance in feet', distance * 3.28084)


if azimuth1 < 0:
    azimuth1 += 360
if azimuth2 < 0:
    azimuth2 += 360

print('    azimuth', azimuth1, azimuth2)

net = azimuth2 - azimuth1
if (net > 315 and net <= 365) or (net >= 0 and net < 45):
    print('straight')
elif net > 0:
    print('right')
else:
    print('left')
