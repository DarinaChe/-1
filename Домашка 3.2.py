# Написать функцию, которая принимает строку на английском языке, гарантируется что все слова - реально существующие английские слова. Функция должна
# возвращать русский перевод. Рекомендуется ипользовать внешнюю библиотеку для перевода, например translate
#
# дополнительно - можно принимать текст на любом языке, определять язык с помощью cld3 и выводить русский перевод


from translate import Translator
from langdetect import detect
text = input("Введите текст: ")
lunguage = detect(text)
translator= Translator(from_lang=lunguage,to_lang="ru")
translation = translator.translate(text)
print(translation)