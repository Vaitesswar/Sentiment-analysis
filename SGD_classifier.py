if __name__ == "__main__":
    # Creating a list of stop words
    list_stop_words = pd.read_csv('stop_words.txt',header = None)
    list_stop_words = list_stop_words.values
    stop_words = list()

    for i in range(len(list_stop_words)):
        stop_words.append(list_stop_words[i][0])

    punctuations_and_num = ['.',',','/',';','[',']','<','>','?','{','}','|','0,1,2,3,4,5,6,7,8,9']
    stop_words = stop_words + punctuations_and_num + ['81', 'zy', 'zyada', 'zyuranger', 'zz', 'zzzz', 'zzzzz', 'zzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zé', 'álex', 'álvaro', 'ángel', 'ángela', 'âme', 'ääliöt', 'äänekoski', 'åge', 'åmål', 'æsthetic', 'écran', 'élan', 'émigré', 'émigrés', 'était', 'état', 'étc', 'évery', 'êxtase', 'ís', 'ísnt', 'østbye', 'über', 'üvegtigris'] + ['00', '000', '0000000000001', '00001', '00015', '001', '003830', '006', '007', '0079', '0080', '0083', '0093638', '00am', '00pm', '00s', '01', '01pm', '02', '020410', '029', '03', '04', '05', '050', '06', '06th', '07', '08', '087', '08th', '09', '0f', '0ne', '0r', '0s', '10', '100', '1000', '10000', '100000', '1000000', '10000000', '10000000000000', '1000lb', '1000s', '1001', '100k', '100m', '100min', '100mph', '100s', '100th', '100x', '100yards', '101', '101st', '102', '102nd', '103', '104', '1040', '1040a', '1040s', '105', '1050', '105lbs', '106', '106min', '107', '108', '109', '10am', '10lines', '10mil', '10min', '10minutes', '10p', '10pm', '10s', '10star', '10th', '10the', '10unnamed', '10waste', '10which', '10x', '10yr', '11', '110', '1100', '11001001', '1100ad', '111', '112', '112001sandler', '1138', '114', '1146', '115', '116', '117', '11f', '11m', '11th', '11unnamed', '12', '120', '1200', '12000', '120000', '12000000', '1200f', '1201', '1202', '123', '123000000', '12345', '1235', '12383499143743701', '125', '125000', '125m', '127', '128', '12a', '12hr', '12m', '12mm', '12s', '12th', '12young', '13', '130', '1300', '13000', '1300s', '131', '131516', '1318', '132', '134', '135', '135m', '136', '137', '138', '139', '13but', '13i', '13k', '13s', '13th', '13unnamed', '14', '140', '1400', '1408', '140hp', '1415', '1430', '145', '1454', '146', '147', '1473', '149', '1492', '14a', '14ieme', '14old', '14s', '14th', '14yr', '14ème', '15', '150', '1500', '15000', '150000', '1500000', '15000000', '1500s', '150k', '150m', '151', '153', '1547', '155', '1561', '157', '158', '1594', '15mins', '15minutes', '15s', '15th', '15years', '16', '160', '1600', '16000', '1600s', '160lbs', '161', '1610', '163', '163000', '164', '165', '165m', '166', '1660s', '168', '169', '1692', '16ewwww', '16ieme', '16k', '16mm', '16mmdvdvhs', '16s', '16th', '16x9', '16ème', '17', '170', '1700', '17000', '1700s', '1701', '171', '172003', '175', '177', '1780s', '1790s', '1794', '1798', '17million', '17th', '18', '180', '1800', '18000', '1800mph', '1800s', '1801', '1805', '1809', '180d', '1812', '1813', '18137', '1814', '1816', '1820', '1824', '183', '1830', '1832', '1836', '1837', '1838', '1839', '1840', '1840s', '1844', '1846', '1847', '185', '1850', '1850ies', '1850s', '1852', '1853', '1854', '1855', '1859', '1860', '1860s', '1861', '1862', '1863', '1864', '1865', '1870', '1870s', '1871', '1873', '1874', '1875', '1876', '188', '1880', '1880s', '1881', '1886', '1887', '1888', '1889', '1890', '1890s', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '18a', '18ron', '18s', '18th', '18this', '18unnamed', '18year', '19', '190', '1900', '19000000', '1900s', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1910s', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '192', '1920', '1920ies', '1920s', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1930europe', '1930ies', '1930s', '1931', '1932', '1933', '1933when', '1934', '1935', '1936', '1936in', '1937', '1938', '1939', '194', '1940', '1940s', '1941', '1942', '1943', '1944', '1945', '1945film', '1946', '1947', '1948', '1949', '1949er', '195', '1950', '1950s', '1951', '1952', '1953', '1954', '1955', '195519561957', '1956', '1956and', '1956title', '1957', '1958', '1959', '1960', '1960hardly', '1960s', '1961', '1961s', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '197', '1970', '1970ies', '1970s', '1971', '1972', '1973', '1974', '1974a', '1975', '1976', '1977', '1978', '1978on', '1979', '19796', '1980', '1980s', '1981', '1982', '1982s', '1983', '1983s', '1984', '1984ish', '1984while', '1985', '1986', '1987', '1988', '1989', '1990', '1990s', '1991', '1992', '1993', '1994', '1995', '1995i', '1996', '1997', '1998', '1999', '1999999', '19k', '19th', '19thc', '19unnamed', '1am', '1and', '1cute', '1d', '1h', '1h30', '1h40', '1h40m', '1h53', '1hour', '1however', '1hr', '1is', '1min', '1mln', '1o', '1s', '1simply', '1st', '1stillzombie', '1ton', '1tv', '1unnamed', '1which', '1why', '1whywhy', '1½', '1ç', '20', '200', '2000', '20000', '200000', '20001several', '2000ad', '2000s', '2001', '2001and', '2002', '2003', '2004', '2004s', '2005', '2005george', '2005well', '2006', '2007', '2007reality', '2008', '2009', '2009the', '200ft', '200th', '201', '2010', '2012', '2013', '2017', '2019', '2020', '2022', '2023', '2030', '2031', '2033', '2035', '2036', '2038', '2040', '2044', '2046', '2047', '2050', '2053', '2054', '206', '2060', '2070', '2080', '209', '2090', '20c', '20ft', '20k', '20m', '20mins', '20minutes', '20mn', '20mr', '20p', '20perr', '20s', '20th', '20that', '20ties', '20widow', '20x', '20year', '20yrs', '21', '210', '2100', '212006', '214', '215', '2151', '21699', '21st', '22', '220', '2200', '22000', '221', '2210', '22101', '222', '223', '225', '2257', '225mins', '227', '22d', '22h45', '22nd', '22the', '23', '2300', '23000', '230lbs', '230mph', '231', '232', '233', '234', '236', '237', '23978', '23d', '23i', '23rd', '24', '240', '2400', '241', '242', '248', '2480', '249', '24but', '24m30s', '24th', '24years', '25', '250', '2500', '25000', '250000', '25million', '25mins', '25s', '25th', '25yo', '25yrs', '26', '260', '2600', '261k', '262', '2642', '269', '26take', '26th', '27', '270', '27000', '272', '273', '274', '275', '278', '27th', '27x41', '28', '280', '28000000', '2819', '28th', '29', '29th', '2am', '2d', '2fast', '2for', '2furious', '2h', '2h30', '2hour', '2hours', '2hr', '2hrs', '2in', '2inch', '2it', '2k', '2maybe', '2more', '2nd', '2pac', '2point4', '2s', '2unnamed', '2x4', '2you', '30', '300', '3000', '30000', '300000', '300000000', '300ad', '300c', '300mln', '3012', '303', '305', '30am', '30ish', '30k', '30lbs', '30min', '30mins', '30pm', '30s', '30something', '30th', '30ties', '31', '3199', '31st', '32', '3200', '320x180', '32lb', '32nd', '33', '330am', '330mins', '332960073452', '336th', '33m', '34', '34000', '345', '3462', '3469', '34th', '35', '350', '3500', '35000', '350000', '3516', '357', '35c', '35mins', '35mm', '35pm', '35th', '35yr', '36', '360', '36000', '365', '36th', '37', '370', '372', '378', '38', '3849', '38k', '38th', '39', '395', '39th', '3am', '3bs', '3d', '3dvd', '3dwell', '3i', '3k', '3lbs', '3m', '3mins', '3p', '3p0', '3pm', '3po', '3rd', '3rds', '3th', '3there', '3who', '3x5', '3yrs', '40', '400', '4000', '40000', '4000000', '401k', '405', '409', '40am', '40min', '40mins', '40mph', '40s', '40th', '41', '42', '420', '4200', '425000', '428', '42nd', '43', '44', '440', '44000000', '442nd', '44c', '44yrs', '45', '450', '4500', '45000', '451', '454', '45am', '45min', '45mins', '45s', '46', '465', '47', '475', '477', '47s', '48', '480m', '480p', '48and', '48hrs', '48unnamed', '49', '498', '49th', '4am', '4but', '4cylinder', '4eva', '4ever', '4f', '4h', '4hrs', '4its', '4k', '4kids', '4m', '4o', '4pm', '4th', '4unnamed', '4w', '4ward', '4x', '4x4', '50', '500', '5000', '50000', '500000', '5000000', '50000000', '500ad', '500db', '500lbs', '50c', '50ft', '50ies', '50ish', '50k', '50min', '50mins', '50s', '50sas', '50th', '50unnamed', '50usd', '51', '51b', '51st', '52', '5200', '5250', '529', '52s', '53', '54', '5400', '540i', '54th', '55', '5539', '55th', '56', '57', '571', '576', '578', '58', '58000', '59', '598947', '59th', '5but', '5even', '5hrs', '5ive', '5kph', '5million', '5min', '5mins', '5s', '5seconds', '5th', '5there', '5unnamed', '5with', '5x', '5x5', '5years', '5yo', '5yrs', '60', '600', '6000', '60000', '6000000', '607', '60ies', '60ish', '60mph', '60s', '60ties', '61', '62', '6200', '62006', '62229249', '63', '637', '63rd', '64', '65', '6500000', '66', '660', '666', '66er', '67', '6723', '67th', '68', '69', '699', '69so', '69th', '6am', '6b', '6but', '6ft', '6hours', '6k', '6million', '6pm', '6th', '6unnamed', '6wks', '6yo', '70', '700', '7000', '701', '707', '70ies', '70m', '70mm', '70s', '70smovie', '70th', '71', '713', '72', '72nd', '73', '7300', '735', '737', '73the', '74', '740000', '740il', '747', '74th', '75', '750', '75000', '750000', '750000000', '75054', '75c', '75m', '76', '7600', '77', '78', '788', '78rpm', '79', '79817937', '79th', '7but', '7days', '7even', '7eventy', '7ft', '7ish', '7mm', '7th', '7unnamed', '7½th', '80', '800', '8000', '80000', '80ies', '80ish', '80min', '80s', '80yr', '81', '82', '820', '8217', '8230', '83', '84', '84f', '84s', '85', '850', '850pm', '86', '86s', '87', '8700', '8763', '878138', '87minutes', '88', '88min', '89', '89or', '89s', '8bit', '8ftdf', '8k', '8mm', '8o', '8p', '8pm', '8seriously', '8star', '8th', '8th1993', '8u', '8unnamed', '8½', '90', '900', '9000', '90000', '900000', '90210', '905', '90c', '90ish', '90min', '90mins', '90s', '90salong', '91', '911', '914', '917', '92', '921', '92fs', '92is', '92nd', '93', '94', '9484', '94s', '94th', '95', '950', '95000000', '95th', '96', '97', '970', '974th', '98', '987', '98minutes', '99', '998', '999', '9999', '99cents', '99p', '99½', '9_', '9am', '9as', '9do', '9ers', '9lbs', '9mm', '9of10', '9pm', '9s', '9th', '9unnamed', '____', '_____', '______', '_________', '____________________________________', '_____________________________________', '__________________________________________________________________']
    
    # Import training set
    training_set = pd.read_csv('imdb_tr.csv',encoding = "ISO-8859-1",header = None)
    X_list = training_set.values[:,1]
    y_list = training_set.values[:,2]
    X = list()
    y = list()

    for i in range(len(X_list)):
        X.append(X_list[i])
        y.append(y_list[i])

    # Import test set
    test_set = pd.read_csv('imdb_te.csv',encoding = "ISO-8859-1")
    X_list = test_set.values[:,1]
    X_test = list()

    for i in range(len(X_list)):
        X_test.append(X_list[i])

    # Unigram (frequency)
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(stop_words = stop_words, ngram_range = (1, 1))
    X_1 = vectorizer.fit_transform(X)

    from sklearn import linear_model
    classifier = linear_model.SGDClassifier(loss = 'hinge', penalty = 'l1')
    classifier.fit(X_1,y)

    X_test_1 = vectorizer.transform(X_test)
    y_pred_1 = classifier.predict(X_test_1)

    file = open("unigram.output.txt","w") 
    for i in y_pred_1:
        file.write(str(i) + "\n")
    file.close()   

    # Unigram (tf-idf)
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words = stop_words, ngram_range = (1, 1))
    X_2 = vectorizer.fit_transform(X)

    from sklearn import linear_model
    classifier = linear_model.SGDClassifier(loss = 'hinge', penalty = 'l1')
    classifier.fit(X_2,y)

    X_test_2 = vectorizer.transform(X_test)
    y_pred_2 = classifier.predict(X_test_2)

    file = open("unigramtfidf.output.txt","w") 
    for i in y_pred_2:
        file.write(str(i) + "\n")
    file.close() 

    # Bigram (frequency)

    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(stop_words = stop_words, ngram_range = (1, 2))
    X_3 = vectorizer.fit_transform(X)

    from sklearn import linear_model
    classifier = linear_model.SGDClassifier(loss = 'hinge', penalty = 'l1')
    classifier.fit(X_3,y)

    X_test_3 = vectorizer.transform(X_test)
    y_pred_3 = classifier.predict(X_test_3)

    file = open("bigram.output.txt","w") 
    for i in y_pred_3:
        file.write(str(i) + "\n")
    file.close()   

    # Bigram (tf-idf)
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words = stop_words, ngram_range = (1, 2))
    X_4 = vectorizer.fit_transform(X)

    from sklearn import linear_model
    classifier = linear_model.SGDClassifier(loss = 'hinge', penalty = 'l1')
    classifier.fit(X_4,y)

    X_test_4 = vectorizer.transform(X_test)
    y_pred_4 = classifier.predict(X_test_4)

    file = open("bigramtfidf.output.txt","w") 
    for i in y_pred_4:
        file.write(str(i) + "\n")
    file.close()  