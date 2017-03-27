ef make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$match": {"country" : "India"}},
            {"$unwind": "$isPartOf"},
            {"$group": {"_id" : "$isPartOf", "count" : {"$sum" : 1}} },
            {"$sort" : {"count" :-1}},
            {"$limit" : 1}]
    return pipeline
