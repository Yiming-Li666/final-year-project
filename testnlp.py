import stanfordnlp
#stanfordnlp.download('zh')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline(lang='zh') # This sets up a default neural pipeline in English
#doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc = nlp("最近自己想接触下语音识别，经过一番了解和摸索，实现了对语音识别API的简单调用，正好写文章记录下。",)
doc.sentences[0].print_dependencies()
#Default download directory: /Users/liyiming/stanfordnlp_resources
#Download location: /Users/liyiming/stanfordnlp_resources/en_ewt_models.zip
print("----------------------")
doc.sentences[0].print_tokens()
print("----------------------")
doc.sentences[0].print_dependencies()