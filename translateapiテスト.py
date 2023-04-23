from googletrans import Translator
translator = Translator()
translation = translator.translate("こんにちは", dest='en')
print(translation.text)
#output:'　Hello　'
print(translator.translate('안녕하세요.', dest='ja'))
#output:"　Translated(src=ko, dest=ja, text=こんにちは。, pronunciation=Kon'nichiwa., extra_data="{'translat...")　"

