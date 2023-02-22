import nltk

nltk.download('punkt')

def check_last_sentence(text,):
    sentences = nltk.sent_tokenize(text)
    last_sentence = sentences[-1]
    words = nltk.word_tokenize(last_sentence)
    return len(words) > 5

def truncate_last_sentence(text):
    sentences = text.split(".")
    if check_last_sentence(sentences[-2]):
        return text
    else:
        truncated_sentences = sentences[:-2] + [sentences[-2].rsplit(" ", 5)[0] + "."]
        return "".join(truncated_sentences)

# split text into chunks of max 2000 characters
def split_text(text, chunk_size=2000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks
