print("\n============================================================================")
print("Q5. Write a script to count words in a given sentence (using dict).")
print("")
print("============================================================================\n")

s1 = input("Enter the Sentence\t\t: ") #Vimala mam it is tested in python 3.7.8 (VScode) & Google colab please note that it may vary in other version. raw_input in python 2 or we can try manual string value also.

dic=dict()
count = 0
for i in s1.split():
    if i not in dic.keys():
        dic[i]=0
    dic[i]+=1
dic_c=len(dic)+0
for j in dic:
    count+=dic[j]
print("Total words in Entered sentence\t:",count)