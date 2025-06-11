# examples/simple_pipeline.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from errorex.main import explain_errors
import pandas as pd
from sklearn.linear_model import LogisticRegression

@explain_errors(log=True, suggest=True, raise_error=True)
def run():
    df = pd.DataFrame({
        'feature': [1, 2, None, 4],
        'label': [0, 1, 0, None]
    })
    df = df.dropna(subset=['feature'])  # bug: didn't drop NaN in 'label'
    X = df[['feature']]
    y = df['label']
    model = LogisticRegression()
    model.fit(X, y)  # This fails due to NaN in label

run()
