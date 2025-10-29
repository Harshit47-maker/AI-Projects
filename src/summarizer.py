from transformers import pipeline
from pathlib import Path
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")
def stxt(text,chunk_size= 700):
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0,len(words),chunk_size)]
    psummaries = []
    for chunk in chunks:
        partial = summarizer(chunk)
        summary_text =  partial[0]['summary_text']
        psummaries.append(summary_text)
    ctext = " ".join(psummaries)
    print('Summary is :',ctext)
    a = input('Do you want to save the summary..........(y/n) : ')
    if a == 'y':
        with open('summary.txt',"w") as file:
            file.write(ctext)
            b = Path('summary.txt')
            print(b.resolve())
    else:
        print('Your summary is not saved.')
    return ctext