# Sentiment-analysis

In this project, a Stochastic Gradient Descent Classifier is trained for sentiment analysis task. The data used in this project is obtained from http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz. There are two sub-directories pos/ for positive texts and neg/ for negative ones.

## Data preprocessing
Use data_preprocessing.py file to extract and store the data for training the SGD classifier. This python file should output “imdb_tr.csv” file. The csv file should have three columns, "row_number" and “text” and “polarity”. The column “text” contains review texts from the aclImdb database and the column “polarity” consists of sentiment labels, 1 for positive and 0 for negative.

The csv. files for both training and testing are provided. Since the filesize of the datasets are large, they have been split and uploaded. Please merge the respective data before training.

In addition, common English stopwords should be removed. Many English stopwords are provided in stop_words.txt. In addition, some stop words are also mentioned within the python file SGD_classifier.py.

## Unigram and bigram models
A common approach to represent the text data is using a document-term vector where each document is encoded as a discrete vector that counts occurrences of each word in the vocabulary it contains. For example, consider two one-sentence documents:  

d1: “I love Columbia Artificial Intelligence course.
d2: “Artificial Intelligence is awesome”

The vocabulary V = {artificial, awesome, Columbia, course, I, intelligence, is, love} and two documents can be encoded as v1 and v2 as follow:

![Unigram](https://user-images.githubusercontent.com/81757215/160071320-4391f62d-549c-43aa-a9e8-b45c6adfc902.JPG)

A more sophisticated data representation model is the bigram model where occurrences depend on a sequence of two words rather than an individual one. Taking the same example like before, v1 and v2 are now encoded as follow:

![bigram](https://user-images.githubusercontent.com/81757215/160071419-0033222d-1d38-41d4-9c6a-d28109e0ef88.JPG)

## tf-idf
Sometimes, a very high word counting may not be meaningful. For example, a common word like “say” may appear 10 times more frequent than a less-common word such as “machine” but it does not mean “say” is 10 times more relevant to our sentiment classifier. To alleviate this issue, we can instead use term frequency tf[t] = 1 + log(f[t,d] ) where f[t,d] is the count of term t in document d. The log function dampens the unwanted influence of common English words.

Inverse document frequency (idf) is a similar concept. To take an example, it is likely that all of our training documents belong to a same category which has specific jargons. For example, Computer Science documents often have words such as computers, CPU, programming and etc  appearing over and over. While they are not common English words, because of the document domain, their occurrences are very high. To rectify, we can adjust using inverse term frequency idf[t] = log( N / df[t] ) where df[t] is the number of documents containing the term t and N is the total number of document in the dataset.

Therefore, instead of just word frequency, tf-idf for each term t can be used, tf-idf[t] = tf[t] ∗idf[t]. 

## Model training
Four variants of SGD classifier were trained with hinge loss and l1 penalty as follows.

1) Unigram model (Counts)
2) Bigram model (Counts)
3) Unigram model (tf-idf)
4) Bigram model (tf-idf)

For each model, the sentiment class (positive or negative) for each review is stored in the text files (e.g. unigram.output).
