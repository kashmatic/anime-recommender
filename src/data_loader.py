import pandas as pd

class AnimeDataLoader:
  def __init__(self, original_csv: str, processed_csv: str):
    self.original_csv = original_csv
    self.processed_csv = processed_csv
  
  def load_and_process(self):
    ## Load the CSV file and drop rows with NA 
    df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip')
    df.dropna(inplace=True)

    ## our required columns
    required_cols = {'Name', 'Genres', 'synopsis'}

    ## check if the required cols are missing
    missing = required_cols - set(df.columns)
    if missing:
      raise ValueError("Missing column in CSV file")
  
    ## create a new column with combined info
    df['combined_info'] = (f""" Title {df['Name']} Overview: {df['synopsis']} Genres: {df['Genres']}""")

    ## only write out this column in the new csv
    df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

    return self.processed_csv
