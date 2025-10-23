from datasets import load_dataset
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from datetime import datetime
import pandas as pd
from multiprocessing import Pool

# year_list = ["1866", "1867", "1868", "1869", "1870",
#             "1871"]

# year_list = ["1872", "1873", "1874", "1875", "1876",
#              "1877", "1878", "1879", "1880", "1881",
#              "1882", "1883", "1884", "1885", "1886",
#              "1887", "1888", "1889", "1890", "1891",
#              "1892", "1893", "1894", "1895", "1896",
#              "1897", "1898", "1899", "1900", "1901",
#              "1902", "1903", "1904", "1905", "1906",
#              "1907", "1908", "1909", "1910", "1911",
#              "1912", "1913", "1914"]

year_list = ["1915", "1916", "1917", "1918", "1919",
            "1920", "1921", "1922", "1923", "1924",
            "1925", "1926", "1927", "1928", "1929",
            "1930", "1931", "1932", "1933", "1934",
            "1935", "1936", "1937", "1938", "1939",
            "1940", "1941", "1942", "1943", "1944"]

# year_list = ['1774', '1798', '1799', '1800', '1801', 
#              '1802', '1803', '1804', '1805', '1806', 
#              '1807', '1808', '1809', '1810', '1811', 
#              '1812', '1813', '1814', '1815', '1816', 
#              '1817', '1818', '1819', '1820', '1821', 
#              '1822', '1823', '1824', '1825', '1826', 
#              '1827', '1828', '1829', '1830', '1831', 
#              '1832', '1833', '1834', '1835', '1836', 
#              '1837', '1838', '1839', '1840', '1841', 
#              '1842', '1843', '1844', '1845', '1846', 
#              '1847', '1848', '1849', '1850', '1851', 
#              '1852', '1853', '1854', '1855', '1856', 
#              '1857', '1858', '1859', '1860', '1861', 
#              '1862', '1863', '1864', '1865', '1866', 
#              '1867', '1868', '1869', '1870', '1871', 
#              '1872', '1873', '1874', '1875', '1876', 
#              '1877', '1878', '1879', '1880', '1881', 
#              '1882', '1883', '1884', '1885', '1886', 
#              '1887', '1888', '1889', '1890', '1891', 
#              '1892', '1893', '1894', '1895', '1896', 
#              '1897', '1898', '1899', '1900', '1901', 
#              '1902', '1903', '1904', '1905', '1906', 
#              '1907', '1908', '1909', '1910', '1911', 
#              '1912', '1913', '1914', '1915', '1916', 
#              '1917', '1918', '1919', '1920', '1921', 
#              '1922', '1923', '1924', '1925', '1926', 
#              '1927', '1928', '1929', '1930', '1931', 
#              '1932', '1933', '1934', '1935', '1936', 
#              '1937', '1938', '1939', '1940', '1941', 
#              '1942', '1943', '1944', '1945', '1946', 
#              '1947', '1948', '1949', '1950', '1951', 
#              '1952', '1953', '1954', '1955', '1956', 
#              '1957', '1958', '1959', '1960', '1961', 
#              '1962', '1963']

search_term_1 = ['klan']
search_term_2 = ['knight', 'rider']
search_term_3 = ['night', 'rider']
search_term_4 = ['nightrider']
search_term_5 = ['wizard']
search_term_6 = ['grand', 'dragon']
search_term_7 = ['kloran']
search_term_8 = ['klavern']
search_term_9 = ['klankraft']
search_term_10 = ['klandom']
search_term_11 = ['royal', 'rider']
search_term_12 = ['red', 'robe']
search_term_13 = ['hooded']
search_term_14 = ['masked']
search_term_15 = ['klux', 'kluxer']
search_term_16 = ['konvention']

# Define a function to process the data
def process_data(data):
    result = {}
    date_object = datetime.strptime(data['date'], '%Y-%m-%d').date()
    
    if date_object >= datetime.strptime(data['year'] + '-01-01', '%Y-%m-%d').date():
        tokens = word_tokenize(data['article'].lower())
        overlap = set(search_term_1).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap) == 1: #klan #1
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }

        knight_index = tokens.index('knight') if 'knight' in tokens else -1 #knight rider #2
        rider_index = tokens.index('rider') if 'rider' in tokens else -1
        if (knight_index != -1 and rider_index != -1 and abs(knight_index - rider_index) <=5): #knight rider
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        # overlap2 = set(search_term_2).intersection(set(word_tokenize(data['article'].lower())))
        # if len(overlap2) == 2: #knight rider
        #     result[data['article_id']] = {
        #         'headline': data['headline'],
        #         'newspaper_name': data['newspaper_name'],
        #         'date': data['date'],
        #         'article': data['article']
        #     }
        
        night_index = tokens.index('night') if 'night' in tokens else -1 #night rider #3
        rider_index = tokens.index('rider') if 'rider' in tokens else -1
        if (night_index != -1 and rider_index != -1 and abs(night_index - rider_index) <=5): #night rider
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        # overlap3 = set(search_term_3).intersection(set(word_tokenize(data['article'].lower())))
        # if len(overlap3) == 2: #night rider
        #     result[data['article_id']] = {
        #         'headline': data['headline'],
        #         'newspaper_name': data['newspaper_name'],
        #         'date': data['date'],
        #         'article': data['article']
        #     }
       
        overlap4 = set(search_term_4).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap4) == 1: #nightrider #4
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap5 = set(search_term_5).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap5) == 1: #wizard #5
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        # overlap6 = set(search_term_6).intersection(set(word_tokenize(data['article'].lower())))
        # if len(overlap6) == 2: #grand dragon
        #     result[data['article_id']] = {
        #         'headline': data['headline'],
        #         'newspaper_name': data['newspaper_name'],
        #         'date': data['date'],
        #         'article': data['article']
        #     }
        
        grand_index = tokens.index('grand') if 'grand' in tokens else -1
        dragon_index = tokens.index('dragon') if 'dragon' in tokens else -1
        if (grand_index != -1 and dragon_index != -1 and abs(grand_index - dragon_index) <=5): #grand dragon #6
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }

        overlap7 = set(search_term_7).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap7) == 1: #kloran #7
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap8 = set(search_term_8).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap8) == 1: #klavern #8
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap9 = set(search_term_9).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap9) == 1: #klankraft #9
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap10 = set(search_term_10).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap10) == 1: #klandom #10
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        royal_index = tokens.index('royal') if 'royal' in tokens else -1
        rider_index = tokens.index('rider') if 'rider' in tokens else -1
        if (royal_index != -1 and rider_index != -1 and abs(royal_index - rider_index) <=5): #royal rider #11
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        # overlap11 = set(search_term_11).intersection(set(word_tokenize(data['article'].lower())))
        # if len(overlap11) == 2: #royal rider
        #     result[data['article_id']] = {
        #         'headline': data['headline'],
        #         'newspaper_name': data['newspaper_name'],
        #         'date': data['date'],
        #         'article': data['article']
        #     }
        
        red_index= tokens.index('red') if 'red' in tokens else -1
        robe_index = tokens.index('robe') if 'robe' in tokens else -1
        if (red_index != -1 and robe_index != -1 and abs(red_index - robe_index) <=5): #red robe #12
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }

        # overlap12 = set(search_term_12).intersection(set(word_tokenize(data['article'].lower())))
        # if len(overlap12) == 2: #red robe
        #     result[data['article_id']] = {
        #         'headline': data['headline'],
        #         'newspaper_name': data['newspaper_name'],
        #         'date': data['date'],
        #         'article': data['article']
        #     }
        
        overlap13 = set(search_term_13).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap13) == 1: #hooded #13
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }

        overlap14 = set(search_term_14).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap14) == 1: #masked #14
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        
        overlap15 = set(search_term_15).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap15) >= 1: #klux kluxer #15
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        
        overlap16 = set(search_term_16).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap16) == 1: #konvention #16
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }

    return result

# Download data for the specified years
if __name__ == '__main__':
    # dataset = load_dataset("dell-research-harvard/AmericanStories", "subset_years", year_list=year_list)
    dataset = load_dataset("dell-research-harvard/AmericanStories", year_list=year_list)

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
    df.to_csv('/Volumes/T7/chroniclingamerica/american-stories/kkk-all-revival.csv', index=False)
