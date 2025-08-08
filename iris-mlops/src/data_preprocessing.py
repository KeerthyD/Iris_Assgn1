from sklearn.datasets import load_iris
import pandas as pd

def load_and_save_data():
    iris = load_iris(as_frame=True)
    df = iris.frame
    df.to_csv('data/iris.csv', index=False)

if __name__ == "__main__":
    load_and_save_data()
