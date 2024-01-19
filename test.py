import pandas as pd 

Data={

    {"name":"pradeep", "age":"28", "city":"bhopal"},
    {"name":"pardhu", "age":"29", "city":"hyd"},
    {"name":"krish", "age":"30", "city":"vskp"}

}

Data = pd.DataFrame(Data)
Data.to_csv("data/data.csv", index=False)
