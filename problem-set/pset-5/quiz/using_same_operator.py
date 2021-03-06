def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$match": {"country" : "India"}},
                {"$unwind": "$isPartOf"},
                {"$group":{"_id":"$isPartOf","avg":{"$avg":"$population"}}},
                {"$group" : {"_id":"India Regional City Population Average","avg":{"$avg":"$avg"}}}
                ]
    return pipeline
