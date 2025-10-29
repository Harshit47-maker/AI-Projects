import matplotlib.pyplot as plt
def draw(a,b) :
    categories = ['Original Text','Summarized Text']
    values = [a , b]
    plt.bar(categories,values)
    plt.tight_layout()
    plt.show()
def draw2(data):
    labels, values = zip(*data)
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Terms')
    plt.ylabel('Scores')
    plt.title('Term Scores Visualization')
    plt.tight_layout()
    plt.show()