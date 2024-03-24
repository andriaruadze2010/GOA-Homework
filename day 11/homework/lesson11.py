for i in range(1 , 51):
    print(i)

for i in range(1 , 51):
    if i % 5 ==0:
        print(i) 


for i in range(2 , 21, +2):
    print(i)





#1*
#5*
#6*
#7*
#8*
#9*
#10*

final_product = 1
for i in range(5, 11):
    final_product =final_product * i
print("ამ ეტაპზე ნამრავლი უდრის:",final_product, "ხოლო final product გავამრავლეთ",i,"ზე")


my_num = 5
# 5-ისფაქტორიალი - 1*2*3*4*5
my_num = 7
# 7-ისფაქტორიალი 1*2*3*4*5*6*7
user_num = int(input("enter a number: "))
final_product = 1
for i in range(user_num):
 final_product *= i
print(user_num, "ის ფაქტორიალი არის:", final_product)





user_num = int(input("please enter a number:"))
if user_num % 2 == 0:
 user_num /= 2
print(user_num)

user_num = user_num *-3 +1
print(user_num)



i=10
while 10 > 0:
   print(i)
   i-=1