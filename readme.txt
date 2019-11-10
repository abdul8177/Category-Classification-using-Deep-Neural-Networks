You have been given a json file, which is a dataset of conversation between two (Customer & Customer Service Executive) in a json structured format which also contains some information such as Category of each dialogue. There are total of seven categories.

Your task is to build a deep learning model which classifies the input sentences/dialogues into one of the seven categories. You also have to build a predictor which accepts the input sentences and classifies them into a category based on the model you built, in a manner so that one can just use the predictor to deploy anywhere without retraining the model.

""Sample Output""
"Sentence" --> "For verification purpose, could you please share your name as in the records?"
"Predicted Category" --> "request_name"

NOTE: You are requested to submit the solution in Jupyter Notebook with proper comments where required, you should be able to demonstrate your work.
