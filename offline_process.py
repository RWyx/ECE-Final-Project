import pandas as pd
import numpy as np
class Offline_Process:
    def coordinate_translation(df):
        translated_df = df.copy()
        x_min = translated_df["longitude"].min()
        y_min = translated_df["latitude"].min()
        translated_df["x_~"] = translated_df["longitude"] - x_min
        translated_df["y_~"] = translated_df["latitude"] - y_min
        return translated_df, x_min, y_min

    def discretization(df):
        dis_df = df.copy()
        c = 0.012138 #C is not provided in the paper, I just put my lucky number
        
        dis_df["i"] = np.floor(dis_df["x_~"] / c).astype(int)
        dis_df["j"] = np.floor(dis_df["y_~"] / c).astype(int)

        return dis_df
        
        
        
    