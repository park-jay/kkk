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

#Organization
search_term_1 = ['klan']
search_term_2 = ['khan'] #I saw OCR errors 
search_term_3 = ['klux']
search_term_4 = ['kloran']
search_term_5 = ['klavern']
search_term_6 = ['klankraft']
search_term_7 = ['klandom']
search_term_8 = ['konvention']
search_term_9 = ['klonverse']
search_term_10 = ['invisible', 'empire']
search_term_11 = ['imperial', 'wizard']
search_term_12 = ['grand', 'dragon']
#violence
search_term_13 = ['knight', 'rider']
search_term_14 = ['night', 'rider']
search_term_15 = ['nightrider']
search_term_16 = ['mask', 'mob']
search_term_17 = ['cross', 'burn']
search_term_18 = ['flog']
search_term_19 = ['lynch']
search_term_20 = ['vigilante']
search_term_21 = ['whip']

# search_term_12 = ['royal', 'rider'] #Too many false positives
# search_term_13 = ['red', 'robe'] #Too many false positives
# search_term_14 = ['hooded'] #Too many false positives
# search_term_15 = ['masked'] #Too many false positives
# search_term_16 = ['klux', 'kluxer']

# Define a function to process the data
def process_data(data):
    result = {}
    date_object = datetime.strptime(data['date'], '%Y-%m-%d').date()
    
    if date_object >= datetime.strptime(data['year'] + '-01-01', '%Y-%m-%d').date():
        tokens = word_tokenize(data['article'].lower())
        overlap_klan = set(search_term_1).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_klan) == 1: #klan #1
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_khan = set(search_term_2).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_khan) == 1: #khan #2
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_klux = set(search_term_3).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_klux) == 1: #klux #3
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_kloran = set(search_term_4).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_kloran) == 1: #kloran #4
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_klavern = set(search_term_5).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_klavern) == 1: #klavern #5
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_klankraft = set(search_term_6).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_klankraft) == 1: #klankraft #6
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_klandom = set(search_term_7).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_klandom) == 1: #klandom #7
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_konvention = set(search_term_8).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_konvention) == 1: #konvention #8
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_klonverse = set(search_term_9).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_klonverse) == 1: #klonverse #9
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        invisible_index = tokens.index('invisible') if 'invisible' in tokens else -1 #invisible empire #10
        empire_index = tokens.index('empire') if 'empire' in tokens else -1
        if (invisible_index != -1 and empire_index != -1 and abs(invisible_index - empire_index) <=5): #invisible empire 
            # check if both words are within 5 words of each other
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        imperial_index = tokens.index('imperial') if 'imperial' in tokens else -1 #imperial wizard #11
        wizard_index = tokens.index('wizard') if 'wizard' in tokens else -1
        if (imperial_index != -1 and wizard_index != -1 and abs(imperial_index - wizard_index) <=5): #imperial wizard
            # check if both words are within 5 words of each other
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']   
            }
        grand_index = tokens.index('grand') if 'grand' in tokens else -1 #grand dragon #12
        dragon_index = tokens.index('dragon') if 'dragon' in tokens else -1
        if (grand_index != -1 and dragon_index != -1 and abs(grand_index- dragon_index) <=5): #grand dragon
            # check if both words are within 5 words of each other
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        knight_index = tokens.index('knight') if 'knight' in tokens else -1 #knight rider #13
        rider_index = tokens.index('rider') if 'rider' in tokens else -1
        if (knight_index != -1 and rider_index != -1 and abs(knight_index - rider_index) <=5): #knight rider
            # check if both words are within 5 words of each other
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        night_index = tokens.index('night') if 'night' in tokens else -1 #night rider #14
        rider_index = tokens.index('rider') if 'rider' in tokens else -1
        if (night_index != -1 and rider_index != -1 and abs(night_index - rider_index) <=5): #night rider
            # check if both words are within 5 words of each other
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        overlap_nightrider = set(search_term_15).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_nightrider) == 1: #nightrider #15
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        mask_index = tokens.index('mask') if 'mask' in tokens else -1 #mask mob #16
        mob_index = tokens.index('mob') if 'mob' in tokens else -1
        if (mask_index != -1 and mob_index != -1 and abs(mask_index - mob_index) <=5): #mask mob
            # check if both words are within 5 words of each other
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'], 
                'date': data['date'],
                'article': data['article']
            }
        cross_index = tokens.index('cross') if 'cross' in tokens else -1 #cross burn #17
        burn_index = tokens.index('burn') if 'burn' in tokens else -1
        if (cross_index != -1 and burn_index != -1 and abs(cross_index - burn_index) <=5): #cross burn
            # check if both words are within 5 words of each other
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_flog = set(search_term_18).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_flog) == 1: #flog #18
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_lynch = set(search_term_19).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_lynch) == 1: #lynch #19
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_vigilante = set(search_term_20).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_vigilante) == 1: #vigilante #20
            result[data['article_id']] = {
                'headline': data['headline'],
                'newspaper_name': data['newspaper_name'],
                'date': data['date'],
                'article': data['article']
            }
        overlap_whip = set(search_term_21).intersection(set(word_tokenize(data['article'].lower())))
        if len(overlap_whip) == 1: #whip #21
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
    df.to_csv('/Volumes/T7/chroniclingamerica/american-stories/kkk-revival.csv', index=False)
