def get_word(sentence, n):
    
    words = sentence.split()

   
    if n > 0 and n <= len(words):
        
        return words[n - 1]
    else:
        return "Invalid word position"


sentence = "This is a Python programming lesson"
n = 4  

result = get_word(sentence, n)
print(result)
