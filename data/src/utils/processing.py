import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns in a DataFrame to lowercase with underscores instead of spaces.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the columns to be renamed.

    Returns
    -------
    pd.DataFrame
        The DataFrame with renamed columns.
    """

    # Use list comprehension to create a new list of column names with spaces replaced by underscores and all lowercase letters
    new_columns = [col.lower().replace(" ", "_") for col in df.columns]
    
    # Use the pandas DataFrame rename() method to rename the columns using the new column names list
    df = df.rename(columns=dict(zip(df.columns, new_columns)))

    return df

def convert_str_num_to_int(df: pd.DataFrame, col_names: list) -> pd.DataFrame:
    """
    Converts string numerical values in a dataframe to int.

    Parameters:
        df (pandas.DataFrame): The dataframe to convert.
        col_names (list): A list of column names containing string numerical values.

    Returns:
        pandas.DataFrame: The modified dataframe.
    """
    
    # Taking a copy of the provided dataframe
    new_df = df.copy()
    
    # Looping over the column names list
    for col in col_names:
        # Replace 'K' with '000'
        new_df[col] = new_df[col].str.replace("K", "000")

        # Multiply the values by 1000 to handle decimal values correctly
        new_df[col] = new_df[col].map(lambda x: int(float(x) * 1000) if '.' in x else int(x))

    return new_df