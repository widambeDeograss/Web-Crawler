import redis
import json
r = redis.Redis()


# def makeFilter(name):
with open('../scraper/sitemapUrl.jl') as f:
    for jsonObj in f:
        objDict = json.loads(jsonObj)
        r.sadd('links', objDict['loc'])


# data = []
# with open('../scraper/updated2L.jl') as f:
#     for jsonObj in f:
#         objDict = json.loads(jsonObj)
#         data.append(objDict)
#
# newData = list({v['url']: v for v in data}.values())
# print(len(newData))
# 784709 real number
# 5552521 number with redundancy

# def check_presence(name, value):
#     return r.sismember(name, value)


# makeFilter('links')
