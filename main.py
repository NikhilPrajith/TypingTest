import time
import pandas as pd
import random

def accuracy(originalWords,userWords):
  correct=0
  userWordsSplit = userWords.split()
  if(len(userWordsSplit) > len(originalWords)):
    correct = 100000
  else:
    for i in range(0,len(userWordsSplit)):
      if(userWordsSplit[i].lower() in originalWords):
        correct+=1
  return correct


word_Join=" "
df=pd.read_csv("file.csv") 
#print(df.head)
rows = (len(df.axes[0]))
columns = (len(df.axes[1])) 
words=[]
#print(df.iloc[5][786])

print("THE RANDOM WORD TYPING TEST \n")
print("Welcome!")
print("Today we will be testing how fast you can type.\n ")
print("Would you like the averge test(20 words)")
print("Press 'Y' to take the default. Press 'N' to input a custom number of words.")
choice = input("Y/N: ")
if(choice.lower()=="y"):
  num=20
else:
  num=int(input("\nHow many words would you like?(**Warning the words are random**): "))
for i in range(0,num):
  words.append(df.iloc[random.randint(0,rows-1)][random.randint(0,columns-1)])


print("\n"+"Alright {0} words it is!".format(num))
print("Remember to press ENTER after you are done!")
time.sleep(0.5)
print("Ready")
time.sleep(0.5)
print("Set")
time.sleep(0.5)
print("Go!!")
print("")
word_Join = word_Join.join(words)
print(word_Join.capitalize()+"\n")
start = time.time()
user_type=input("TYPE:  ")
end = time.time()
time_took = round(end-start,2)
print("Time: {0}".format(time_took))
rate = round((num*60)/time_took)
correct = accuracy(words,user_type)
if(correct == 100000):
  print("Sorry, you failed the test! You inputted extra words!")
else:
  accurate = round((correct/num *100),2)
  if(accurate < 70):
    print("Sorry, it seems like you didn't even try!!")
    print("Accuracy= {0}%".format(accurate))
  else:
    print("Accuracy: {0}% , Rate: {1} words per minute.".format(accurate,rate))



