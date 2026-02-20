class Offline_Process:
    def coordinate_translation(df):
        import pandas as pd
        translated_df = df.copy()
        x_min = translated_df["longitude"].min()
        
        