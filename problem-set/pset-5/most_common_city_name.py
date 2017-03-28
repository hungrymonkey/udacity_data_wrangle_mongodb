def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ { "$match" : { 'name': { "$ne": None } } } ,
            {"$group":{"_id":"$name","count":{"$sum":1}}},
            {"$sort":{"count":-1}},
            {"$limit":1}]
    return pipeline
