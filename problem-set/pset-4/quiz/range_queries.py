def range_query():
    # Modify the below line with your query.
    # You can use datetime(year, month, day) to specify date in the query
    query = {"foundingDate": { "$lte": datetime(2100,12,31), "$gte": datetime(2001,1,1) } }
    return query
