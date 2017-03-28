
def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ {"$unwind": "$isPartOf"}, 
                {"$group" : {"_id":{"country": "$country", "region":"$isPartOf"},"avg": {"$avg":"$population"} }},
                {"$group" : {"_id": "$_id.country", "avgRegionalPopulation" : {"$avg":"$avg"}}}]
    return pipeline
