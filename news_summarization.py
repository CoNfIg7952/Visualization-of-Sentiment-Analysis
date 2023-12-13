import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

nltk.download('punkt')
nltk.download('stopwords')

def news_summarization(text, num_sentences=8):
    stop_words = set(stopwords.words('english'))

    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Tokenize words and remove stop words
    words = word_tokenize(text)
    word_freq = {}
    for word in words:
        word = word.lower()
        if word not in stop_words and word.isalnum():
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    # Calculate weighted frequencies for sentences
    sent_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sent_scores:
                        sent_scores[sentence] = word_freq[word]
                    else:
                        sent_scores[sentence] += word_freq[word]

    # Get the top 'num_sentences' sentences with highest scores
    summary_sentences = nlargest(num_sentences, sent_scores, key=sent_scores.get)

    # Create the summarized text
    summary = ' '.join(summary_sentences)
    return summary
