from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='pt', target='en')
texto = 'Olá, Mundo!'
traducao = tradutor.translate(texto)
print(traducao)
