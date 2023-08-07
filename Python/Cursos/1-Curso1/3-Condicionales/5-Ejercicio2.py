word1=input('Insert the first word: ');
word2=input('Insert the second word: ');
if len(word1)<3 or len(word2)<3:
    print('Words are short');
else:
    if word1[-3:]==word2[-3:]:
        print('Words rhyme a lot');
    elif word1[-2:]==word2[-2:]:
        print('Words rhyme a little');
    else:
        print('Words do not rhyme'); 