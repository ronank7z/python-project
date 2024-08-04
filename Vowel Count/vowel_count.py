def vowel_count(sentence):
    
    # Set initial value for found vowel in sentence
    count = 0

    # Loop each character in sentences
    for char in sentence:
        # Check if character is vowel
        if char in 'aeiouAEIOU':
            count += 1

    return count

sentence = "Abacadabra Abacadabra"

print("Sentence: '{}', (count: {})".format(sentence, vowel_count(sentence)))