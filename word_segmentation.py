import jieba


with open(r'C:/Users/CY/Desktop/text.txt') as f:
    all_text = f.read()

text_list = []
text_list = jieba.lcut(all_text)
stop_list = ['\n', '/', ' ', '也', '了']
for stop_word in stop_list:
    while stop_word in text_list:
        text_list.remove(stop_word)
text_str = ' '.join(text_list)
with open(r'C:/Users/CY/Desktop/word_segmentation.txt', 'a', encoding='utf-8') as w:
    w.write(text_str)


