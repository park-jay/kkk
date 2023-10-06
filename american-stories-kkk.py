from datasets import load_dataset
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from datetime import datetime
import pandas as pd
from multiprocessing import Pool

year_list = ["1915", "1916", "1917", "1918", "1919",
            "1920", "1921", "1922", "1923", "1924",
            "1925", "1926", "1927", "1928", "1929",
            "1930", "1931", "1932", "1933", "1934",
            "1935", "1936", "1937", "1938", "1939"]

search_term_1 = ['klan']
search_term_2 = ['knight', 'rider']
search_term_3 = ['night', 'rider']
search_term_4 = ['nightrider']

# Define a function to process the data
def process_data(data):
    result = {}
    date_object = datetime.strptime(data['date'], '%Y-%m-%d').date()
    
    if date_object >= datetime.strptime(data['year'] + '-01-01', '%Y-%m-%d').date():
        overlap = set(search_term_1).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap) == 1:
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap2 = set(search_term_2).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap2) == 2:
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap3 = set(search_term_3).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap3) == 2:
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap4 = set(search_term_4).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap4) == 1:
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
    
    return result

# Download data for the specified years
if __name__ == '__main__':
    dataset = load_dataset("dell-research-harvard/AmericanStories", "subset_years", year_list=year_list)

    kkk_second = {}
    # Create a pool of worker processes
    with Pool(processes=20) as pool:
        for year in year_list:
            results = []
            for data in tqdm(dataset[year], desc=f"Processing Year {year}"):
                data['year'] = year
                result = pool.apply_async(process_data, (data,))
                results.append(result)
            # Collect the results from all the processes
            for result in results:
                kkk_second.update(result.get())

    # Convert the final dictionary to a DataFrame and save it to a CSV
    df = pd.DataFrame.from_dict(kkk_second).T.reset_index()
    df.to_csv('/Volumes/T7/chroniclingamerica/american-stories/kkk-second-new.csv', index=False)
