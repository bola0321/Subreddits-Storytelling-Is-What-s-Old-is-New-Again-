#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_data(file_str_list):
    concat_df = pd.DataFrame(columns=["post_id","selftext","subreddit","is_osr"])
    
    for file in file_str_list:
        #read in file
        df = pd.read_csv(file)
        #remove rows that don't contain selftext
        df = df.dropna(subset="selftext")
        #rename column to post_id for clarity
        df = df.rename(columns={"Unnamed: 0": "post_id"})
        #drop comments, title, create_utc columns
        df = df.drop(columns=["comments", "title","created_utc"])
        #assign new column to 0/1 if a row is from the osr subreddit or not
        df["is_osr"] = df["subreddit"].map({"rpg": 0, "osr": 1})

        #concatenate data 
        concat_df = pd.concat([concat_df, df])

    return concat_df