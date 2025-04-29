class Person:
    # TODO: Please write your code here
    def __init__(self, firstname, lastname, age, hobby):
        self.firstname = firstname
        self.lastname = lastname
        self._age = age
        self.hobby = list(hobby)

    def introduce(self):

        hobbys = ""
        minehobby = self.hobby
        if len(minehobby) == 1:
            hobbys = minehobby[0]
        elif len(minehobby) == 0:
            hobbys = ""
        elif len(minehobby) == 2:
            hobbys = minehobby[0] + " and " + minehobby[1]
        else:
            hobbys = ", ".join(minehobby[0: -1]) + ", and " + str(minehobby[-1])

        output = "Hi, my name is " + self.firstname + " "+ self.lastname + ". I like " + hobbys + "."
        return output

    def add_hobbies(self, new_hobby):
        origi_hobby = self.hobby
        for i in new_hobby:

            if i not in self.hobby:
                origi_hobby.append(i)
                self.hobby = origi_hobby

    # pass


# Do not change or remove the code below this point
def main():
    # Instantiate the first person and display their introduction.
    p1 = Person("John", "Doe", 20, ["playing guitar"])
    print(p1.introduce())
    # Expected Output:
    # Hi, my name is John Doe. I like playing guitar.

    # Instantiate the second person and display their introduction.
    p2 = Person("Peter", "Wang", 24, ["driving cars", "jogging"])
    print(p2.introduce())
    # Expected Output:
    # Hi, my name is Peter Wang. I like driving cars and jogging.

    # Test adding hobbies to the second person.
    p2.add_hobbies(["jogging", "diving"])
    print(p2.introduce())
    # Expected Output:
    # Hi, my name is Peter Wang. I like driving cars, jogging, and diving.

    # Additional test: Instantiate a third person.
    p3 = Person("Alice", "Smith", 30, ["reading", "swimming"])
    print(p3.introduce())
    # You may test additional scenarios by adding more hobbies.
    p3.add_hobbies(["swimming", "cycling", "reading"])
    print(p3.introduce())

    p4= Person("Geo", "Wang", 20, [])


if __name__ == "__main__":
    main()
