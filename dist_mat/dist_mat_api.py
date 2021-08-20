def od_pair(origins,destinations):
    """takes in origin and destinations coordinates as lists, retruns o-d pair as tuples in a list """
    od_pair=[]
    for i in range(len(origins)):
        for j in range(len(destinations)):
            od=origins[i],destinations[j]
            od_pair.append(od)
    return od_pair

def od_format(coords):  
    """takes in cordinates of origin or destination coordinates as lists, retunns origin format
        requred for distance matrix api"""
    
    o_d_format='|'.join(coords)
    return o_d_format


def distance_matrix(origins,destinatins,key):
    """takes in origin and destiantions coordinates in distance matrix api format and api key, 
        returns pretty print of json responses from the api for driving mode and current departure time"""
    import pprint as pp
    mode="driving"
    departure_time="now"
    traffic_model="best_guess"
    units="imperial"
    url="https://api.distancematrix.ai/maps/api/distancematrix/json?origins="+origins+"&destinations="+destinations+ \
    "&mode="+mode+"&traffic_model="+traffic_model+"&departure_time="+departure_time+ \
    "&units="+units+"&key="+key
    
    dist_mat_=requests.get(url).json()
    dist_mat=pp.pprint(dist_mat_)
    return dist_mat

def od_pair_addresses(dist_mat):
    """takes in the json output from the distance_matric function,
        retuns od pair addresses as tuples in a list"""
    o=dist_mat['origin_addresses']
    d=dist_mat['destination_addresses']
    od_pair_addresses=[]
    for i in range(len(o)):
        for j in range(len(d)):
            OD=o[i],d[j]
            od_pair_addresses.append(OD)
    return od_pair_addresses
    

def distance(dist_mat):
    """takes in the json output from the distance_matric function, 
        returns distance list between origin and destination"""
    distance=[]
    for i in range(len(dist_mat['origin_addresses'])):
        for j in range(len(dist_mat['destination_addresses'])):
            dist_= json_dict['rows'][i]['elements'][j]['distance']['text']
            distance.append(dist_)
            #duration.append(dur_)
            #duration_in_traffic.append(dur_tr)
    return distance


def duration(dist_mat):
    """takes in the json output from the distance_matric function, 
        returns distance list between origin and destination"""
    duration=[]
    for i in range(len(dist_mat['origin_addresses'])):
        for j in range(len(dist_mat['destination_addresses'])):
            dist_= json_dict['rows'][i]['elements'][j]['duration']['text']
            distance.append(dist_)
            #duration.append(dur_)
            #duration_in_traffic.append(dur_tr)
    return duration


def duration_in_traffic(dist_mat):
    """takes in origin and destination lists and json_response dictionary from distance matrix api, returns duration_in_traffic list 
        between origin and destination"""
    duration_in_traffic=[]
    for i in range(len(dist_mat['origin_addresses'])):
        for j in range(len(ist_mat['destination_addresses'])):
            dur_tr=json_dict['rows'][i]['elements'][j]['duration_in_traffic']['text']
            duration_in_traffic.append(dur_tr)
    return duration_in_traffic
    
