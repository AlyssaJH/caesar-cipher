# add your code here
key = {
    "a": "f", "b": "g", "c": "h",
    "d": "i", "e": "j", "f": "k",
    "g": "l", "h": "m", "i": "n",
    "j": "o", "k": "p", "l": "q",
    "m": "r", "n": "s", "o": "t",
    "p": "u", "q": "v", "r": "w",
    "s": "x", "t": "y", "u": "z",
    "v": "a", "w": "b", "x": "c",
    "y": "d", "z": "e", 
}

user_sentence = input("Please enter a sentence: ")
user_sentence = user_sentence.lower()

encrypted_sentence = ""
for char in user_sentence: 
    if char in key: 
        char = key[char]
    encrypted_sentence += char
    
print("The encrypted sentence is " + encrypted_sentence)