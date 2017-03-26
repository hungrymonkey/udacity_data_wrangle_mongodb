def in_query():
    # Modify the below line with your query; try to use the $in operator.
    query = {"manufacturer":"Ford Motor Company","assembly":{"$in":["Germany","United Kingdom","Japan"]}}
    
    return query
