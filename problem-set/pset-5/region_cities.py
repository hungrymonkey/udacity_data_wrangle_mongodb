def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ {"$match": {"country" : "India"}},
                {"$match": {'lon': {"$gte":75 , "$lte": 80}} },
                {"$unwind": "$isPartOf"},
                {"$group" : {"_id":"$isPartOf","count": {"$sum":1} }},
                {"$sort":{"count":-1}},
                {"$limit":1}]
    return pipeline
