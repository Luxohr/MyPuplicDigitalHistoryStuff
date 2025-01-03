a = True
c = "stranger"
p = 0
i = 0
x = 0
e = 0


print (f"hello {c}")

random = input("Who is ill today?")
name = input("Whats your name?")

if name == "Mika":
    print ("welcome master")
    a = False
elif name in ["Sophie","Basti", random]:
    print("You are sick, stay at home!")
    a = False
else:
    print(f"hello {name}")

    if a == True:
        print("you may bow to your master")
        while p <= 5:
            gift = input("You may offer a gift")
            if gift == "Kekse":
                print("acceptable")
                quit()
            else:
                print("no taste")
            p = p+1
        print("You failed")


while i < 100:
    i = i +1
    if (i % 5)== 0 and (i % 3) == 0: #Ich weiß dass auch %15 gehen würde.
        print("FizzBuzz")
    elif (i % 5) == 0:
        print("Buzz")
    elif (i % 3) == 0:
        print("Fizz")
    else:
        print(i)

magic = input("Tell me a number and I tell you if it's smaller then 11")
if int(magic) < 11:
    print("Gratulation, you picked a number smaller than 11")
elif int(magic) == 11:
    print("Philosophers will talk about the mystery of 11 being smaller or greater then 11")
elif int(magic) > 11:
    print("Your number is in fact bigger then 11")



