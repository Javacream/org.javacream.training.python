text = """
Der Morgen begann ruhig, doch voller kleiner Erwartungen. Ein leichter Nebel hing über den Straßen, während Menschen hastig zur Arbeit eilten. In einem Café klirrten Tassen, und der Duft von frischem Kaffee mischte sich mit Gesprächen. Eine Frau las Zeitung, ein Kind lachte, jemand tippte Nachrichten auf seinem Handy. Die Stadt wirkte gleichzeitig vertraut und neu. Gedanken wanderten, Pläne entstanden, Zweifel verschwanden. Zeit verging unbemerkt. Zwischen Terminen und Pausen blieb Raum für kurze Begegnungen. Sie erinnerten daran, dass Alltag aus Momenten besteht, die Bedeutung gewinnen, wenn man innehält und aufmerksam bleibt. Manchmal helfen solche Augenblicke, Mut zu fassen im Leben.
"""

print(f'Länge des Texttes: {len(text)}')
print(f'Anzahl Wörter: {len(text.split())}')
print(f'Anzahl unterschiedlicher Wörter: {len(set(text.split()))}')
print(f'Anzahl unterschiedlicher Wörter unabhängig von Groß-/Kleinschreibung: {len(set(text.upper().split()))}')

