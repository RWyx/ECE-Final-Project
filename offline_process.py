import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter
class Offline_Process:
    def coordinate_translation(df):
        translated_df = df.copy()
        x_min = translated_df["longitude"].min()
        y_min = translated_df["latitude"].min()
        translated_df["x_~"] = translated_df["longitude"] - x_min
        translated_df["y_~"] = translated_df["latitude"] - y_min
        return translated_df, x_min, y_min

    def discretization(df, c):
        dis_df = df.copy()
        dis_df["i"] = np.floor(dis_df["x_~"] / c).astype(int)
        dis_df["j"] = np.floor(dis_df["y_~"] / c).astype(int)

        return dis_df
    
    def form_matrix(df):
        matrix_df = df.copy()
        W_fine = int(matrix_df["i"].max()) + 1
        H_fine = int(matrix_df["j"].max()) + 1

        binary_grids = {}
        
        for uid, user_df in matrix_df.groupby("user_id", sort=False):
            i = user_df["i"].to_numpy(dtype=int)
            j = user_df["j"].to_numpy(dtype=int)

            X = np.zeros((W_fine, H_fine), dtype=np.uint8)
            X[i, j] = 1

            binary_grids[uid] = X

        return binary_grids, W_fine, H_fine
    
    def Gaussian_Smoothing(binary_grids, std):
        smoothed_grids = {}
        for uid, X in binary_grids.items():
            X_smooth = gaussian_filter(
                X.astype(np.float32),
                sigma = std,
                mode = "constant",
                cval = 0.0
            )
            smoothed_grids[uid] = X_smooth

        return smoothed_grids