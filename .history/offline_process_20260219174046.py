class Offline_Process:
    def coordinate_translation(df):
        import pandas as pd
        translated_df = df.copy()
        x_min = translated_df["longitude"].min()
        y_min = translated_df["latitude"].min()
        translated_df["x_~"] = translated_df["longitude"] - x_min
        translated_df["y_tilde"] = translated_df["latitude"] - y_min