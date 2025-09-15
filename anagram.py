def is_anagram(word,word2):
    return sorted(word.lower()==sorted(word2.lower()))
    name=input("Enter a name:")
    word_check=input("Enter anothe name:")
    if is_anagram(name,word_check):
        print("yes! It's an anagram.")
    else:
        print("No,not an anagram.")