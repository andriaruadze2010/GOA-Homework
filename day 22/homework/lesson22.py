
#მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა. თუ მისი სიგრძე აღემატება სამს, დაბეჭდეთ მისი პირველი სამი ასო. ხოლო თუ ნაკლებია ან ტოლი სამის, დაბეჭდეთ სიტყვის პირველი ასო.



word = (input("please enter your word"))

if len(word) > 3:
    print(word[:3])
else:
    print(word[0])




numbers = (range(10, 21))

for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])





