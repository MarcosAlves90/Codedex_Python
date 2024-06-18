import wikipedia

search = input("Pesquisa: ")

wikipedia.set_lang('pt')

print(wikipedia.summary(wikipedia.WikipediaPage(search)))