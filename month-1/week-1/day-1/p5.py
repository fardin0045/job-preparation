# s1
def denomination(num):
    a = num // 1000
    num %= 1000

    b = num // 500
    num %= 500

    c = num // 100
    num %= 100

    d = num // 50
    num %= 50

    print("BDT 1000:", a)
    print("BDT 500:", b)
    print("BDT 100:", c)
    print("BDT 50:", d)
    print("Remaining:", num)

denomination(1200)

# s2
def denomin(num):
    notes = [1000,500,200,100,50,20,10,5,1]

    for note in notes:
        count= num //note
        num = num % note
        
        print(f"BDT {note}: {count}")
        
denomin(12000)

a =10 + 2 * 3 ** 2
print(a)
print(int(7.9) + float('2.5'))