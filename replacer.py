# replacing commas with dots
with open('words.txt', 'rt', encoding='utf8') as fin, open('words_formated.txt', 'wt', encoding='utf8') as fout:
    for line in fin:
        fout.write(line.replace(',', '.'))
        
# replacing tabs with commas
with open('words_formated.txt', 'rt', encoding='utf8') as fin, open('words.csv', 'wt', encoding='utf8') as fout:
    for line in fin:
        fout.write(line.replace('\t', ','))

