# Requirements to run the ai
# 


from transformers import pipeline
import pandas as pd

print("Initializing Pipeline")
tqa = pipeline(task="table-question-answering",
               model="google/tapas-base-finetuned-wtq")

print("Loading Data")
table = pd.read_csv("Athletes.csv")
table = table.astype(str)
print(table)

while True:
    print("Asking a question")
    query = input()
    result = tqa(table=table, query=query)
    print(result)
