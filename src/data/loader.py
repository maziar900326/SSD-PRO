import pandas as pd


class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        df = pd.read_csv(self.file_path)

        # تبدیل ستون زمان
        df["time"] = pd.to_datetime(df["time"])

        # مرتب سازی
        df = df.sort_values("time")

        # شماره گذاری مجدد
        df = df.reset_index(drop=True)

        return df