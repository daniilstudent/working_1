
N=int(input("Введите целое и рациональное число экзаменов N<=20: "))
if N==1:
    print("Мы успешно сдали" , N , "экзамен.")
elif 1<N<5:
    print("Мы успешно сдали", N , "экзамена.")
elif 4<N<=20 or N==0:
    print("Мы успешно сдали", N , "экзаменов.")
else:
    print("Введенное число не является рациональным и целым.")

