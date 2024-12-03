import pandas as pd

train = pd.read_csv("data/train.csv")
train_text = train["text"]
train_label = train["label"]

test = pd.read_csv("data/test.csv")
test_id = test["id"]
test_text = test["text"]

print(train.head())
print(test.head())
