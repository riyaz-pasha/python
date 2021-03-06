from nltk import word_tokenize, pos_tag

#1 Read from a File
#1.1 Replce with required file name
file = open("text.txt")
#1.2 Read that entire file into one string
s = file.read()

#2 Run NLTK on the above string
#Creating a dictionary to maintain a key value pair of tag and their values
my_dict={}
for word, pos in pos_tag(word_tokenize(s)):
    l=my_dict.get(pos,[])
    l.append(word)
    my_dict[pos]=l

print("---------------------------------------")
print(my_dict)

print("---------------------------------------")
for action, values in my_dict.items():
    print(action + " : ",len(values))

print("---------------------------------------")
noun_count= len(my_dict.get("NN",[])) +len(my_dict.get("NNS",[])) +len(my_dict.get("NNP",[])) +len(my_dict.get("NNPS",[]))  
print("NOUN : " , noun_count)

verb_count= len(my_dict.get("VB",[])) +len(my_dict.get("VBD",[])) +len(my_dict.get("VBG",[])) +len(my_dict.get("VBN",[]))+len(my_dict.get("VBP",[]))+len(my_dict.get("VBZ",[]))
print("VERB : " , verb_count)
