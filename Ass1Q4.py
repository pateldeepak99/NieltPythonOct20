print("\n============================================================================")
print("Q4. Write a script to print the total no. of palindrome words in a given sentence.")
print("Teste sentence is 'NAN NAN BOB NOR' output comes 3")
print("============================================================================\n")


s1 = input("Enter the Sentence\t:") #Vimala mam it is tested in python 3.7.8 (VScode) please note that it may vary in other version. raw_input in python 2 we can try manual string value also.
w1 = s1.split()
li_len = len(w1)
count = 0

for i in range(li_len):
    lt=list(w1[i])
    ltr= (lt[::-1])
    if(lt==ltr):
     count+=1
print("Total Palidrome word\t:", count)