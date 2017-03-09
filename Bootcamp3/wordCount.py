def word_occurance(sentence):
	result = {}
	
	for word in sentence.split():

		try: # checking for word in rest of sentence
		    result[word]+=1

        except: #if word does not exist in rest of word
        	result[word]=1

    for word in result:
    	print(word,":",result[word])
