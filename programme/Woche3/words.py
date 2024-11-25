text = 'Das ist ein einfacher Text ohne Kommas oder Punkte damit ist das Kriterium für Wörter das Leerzeichen'
words_list = text.split(' ')
recreated_text = ' '.join(words_list)
print(recreated_text)