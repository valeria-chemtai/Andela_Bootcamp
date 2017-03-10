def words(sentence):
	result = {}
    for word in sentence.split():
    	if word.isdigit(): # checking if word is a number, if so convert it to digit instead of using string
    		word = int(word)

        try:  #checking for word in rest of sentence
            result[word] += 1

        except: #if word does not exist in rest of word
            result[word] = 1


    return result