def check_loc(point, lat, longi):
    # YOUR CODE HERE
    p =  point.split()
    return lat == p[0] and  longi == p[1]
