import pandas as pd

def solution(df):
    df = df.loc[:, df.isnull().mean() <= 0.5]

    df = df.loc[ df.isnull().mean(axis = 1) <= 0.5,:]

    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:    
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    object_cols = df.select_dtypes(exclude='number').columns
    if len(object_cols) > 0: 
        df[object_cols] = df[object_cols].fillna(df[object_cols].mode().iloc[0])   

    return  df.reset_index(drop=True)