def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$group": { "_id" : "$source", "count" : {"$sum" : 1} } }, {"$sort" : {"count":-1}}]
    return pipeline
