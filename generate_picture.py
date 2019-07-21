import matplotlib.pyplot as plt
from wordcloud import WordCloud


with open(r'C:/Users/CY/Desktop/word_segmentation.txt', encoding='utf-8') as w:
    text_str = w.read()

wordcloud = WordCloud(
    background_color="white",
    max_words=50,
    max_font_size=300,
    random_state=80,
    width=1920,
    height=1080,
    margin=3,
    font_path=r"C:\Users\CY\Downloads\simsun.ttf").generate(text_str)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
wordcloud.to_file(r'C:/Users/CY/Desktop/test.png')
