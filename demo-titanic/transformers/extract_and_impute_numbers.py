from pandas import DataFrame
import math
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def select_number_columns (df:DataFrame) -> DataFrame:
    return df[['Age', 'Fare', 'Parch', 'Pclass', 'SibSp', 'Survived']]

def fill_missing_values_with_median (df:DataFrame) -> DataFrame:
    for col in df.columns:
        values = sorted(df[col].dropna().tolist())
        median_val = values[math.floor(len(values)/2)]
        df[[col]] = df[[col]].fillna(median_val)
    return df

@transformer
def transform_df(df:DataFrame, *args, ) -> DataFrame:
    return fill_missing_values_with_median(select_number_columns(df))

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
