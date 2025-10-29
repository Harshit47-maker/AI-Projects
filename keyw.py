from keybert import KeyBERT
model = KeyBERT()
def ext(a):
    word = model.extract_keywords(a)
    return word