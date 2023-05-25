word1, word2 = input(), input()
word1, word2 = word2, word1
print(f'!{word1} ! {word2}!')
print('!{word1} ! {word2}!'.format(word1=word1,word2=word2))
print('!'+word1+" "+'!'+' '+word2+"!")