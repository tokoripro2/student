#問０

string = "stressed"
print(string[::-1])

#問１

question1 = "パタトクカシーー"
answer = list(question1)

for i in range(len(answer)):
    #print(len(answer))
    #print(i)
    if not (i + 1) % 2 == 0:
        if not (i + 2) == len(answer):
            print(answer[i], end = '')
        else:
            print(answer[i])

#問２

ques3_1 = "パトカー"
ques3_2 = "タクシー"
ques3_1_list = list(ques3_1)
#ques3_1_list = [ques3_1]
ques3_2_list = list(ques3_2)
#ques3_2_list = [ques3_2]
answer = ""
#print(ques3_1_list)
for i in range(4):
    answer = answer + str(ques3_1_list[i]) + str(ques3_2_list[i])
print(str(answer))

#問３

word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word_list = word.replace(',', '').replace('.', '').split(" ")
#print(word_list)
ans = ""
for i in range(len(word_list)):
    ans = ans + str(len(word_list[i]))# , end=''
print(ans)