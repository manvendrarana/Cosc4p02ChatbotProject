# Requirements to run the ai
# 

import os

os.chdir(os.getcwd()+"/Chatbot/Back-End/components/ai/data")

from traceback import print_tb
from transformers import pipeline
import pandas as pd

if input() == "start":
    print("Initializing ai")
    tqa = pipeline(task="table-question-answering",
             model="google/tapas-base-finetuned-wtq")

    table = pd.read_csv("Topics.csv")
    table = table.astype(str)
    print("Ai is ready for query")
    while True:
        query = input()
        result = tqa(table=table, query=query)
        print(result)
