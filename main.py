class new:
    def sum(a:int,b:int) -> int:
        c = a + b
        return c


class get:
    def num() -> int:
        a = int(input("Give me a number: "))
        return a


answer = new.sum(get.num(),get.num())
x = "Sum of the numbers are : "
print(x,answer)