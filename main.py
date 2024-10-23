from pymongo import MongoClient
import pandas as pd


#################################  Q1
data = pd.read_csv("abc.csv")
print(data)
print()

#################################   Q2
avgStuds = data.loc[:, "No of Studs"].mean()
print(f"Average students: {avgStuds}")

################################## Q3
# print()
# colbwranks = data["Rank" >10]
# print("@@@@@@@@@@@@@@@@@@@@@")
# print(colbwranks)

###################################  Q4
print()
conn = MongoClient("localhost", 27017)
db = conn["eval2"]
coll = db["collection"]

coll.drop()

dictData = data.to_dict(orient="records")
coll.insert_many(dictData)

################################## Q3
print()
res = coll.find({"Rank": {"$gt": 10, "$lt": 15}})
df = pd.DataFrame(list(res)).set_index("_id")
print("Colleges with rank between 10 and 15 exclusive:")
print(df)

###################################  Q5
print()
# stateData = data.sort_values("State", ascending=True)
# print("State-wise sorted data: ")
# print(stateData)

res = coll.find().sort({"State": 1})
stateData = pd.DataFrame(list(res)).set_index("_id")
print("Colleges Sorted by State:")
print(stateData)


################################### Q6
print()
# princ = data["Principal"][[False, True, False]]
# print(princ)

res = coll.find_one({"Rank": 5})
print(f"Principal with college rank 5: {res["Principal"]}")
