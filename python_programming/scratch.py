def main():
    def meierSayHello():
        return f"Hello, my name is {firstname2} {lastnameMeier}"
    personMeier = {
        lastname: "Meier",
        firstname: "Hannah", 
        sayHello: meierSayHello
    }
    def sayHello():
        return f"Hello, my name is {firstname} {lastname}"

    personSawitzki = {
        lastname: "Sawitzki",
        firstname: "Rainer",
        sayHello: sayHello

    }
    print(sayHello())
    print(meierSayHello())
main()