# Example A
# =============================================================================================================================================
print("Basic A Example", "-" * 80)


class Sample:
    pass


sample1 = Sample
sample2 = Sample()
print("sample content of main block : ", dir())
print("Sample  content class of block : ", dir(Sample))
print("Sample 1 content object class of block : ", dir(sample1))
print("Sample 2 content class of block        : ", dir(sample2))

# Example B
# =============================================================================================================================================
print("Basic B Example", "-" * 80)


class ClassMember:
    first_member = 34


OBJECT_FIRST = ClassMember()
OBJECT_FIRST.first_member = 56  # initialize variable
print("the value of object member is : ", OBJECT_FIRST.first_member)  # 56
print("the value of class member is : ", ClassMember.first_member)  # 34

# Example C
# =============================================================================================================================================
print("Basic C Example", "-" * 80)


class ConstructorDisplayDelete:
    def __int__(self):
        print("Constructor Self : ", self)

    def display(self):
        print("Display Self     : ", self)

    def __delete__(self):
        print("Destructor Self      : ", self)


m = ConstructorDisplayDelete()
n = ConstructorDisplayDelete()
m.display()  # address of memory is different
n.display()  # address of memory is different

# Example D
# =============================================================================================================================================
print("Basic D Example", "-" * 80)


class InitialzeVariable:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Constructor initialize member variable : ", self, self.num1, self.num2)

    def display(self):
        print("Excuted the method : ", self, self.num1, self.num2)

    # def display2(self): # Can not access the directly member variable without self or reference
    #     print("Excuted the method : ", num1, num2)


initializeVariable = InitialzeVariable(11, 22)
initializeVariable.display()
# initializeVariable.display2() # can not access the directly member variable without self or reference
initializeVariable.__init__(44, 55)  # How to call constructor

print("Object attributed of initializeVariable is ", initializeVariable.num1, initializeVariable.num2)
print(' the components of class is  ', dir(InitialzeVariable))
print(' the components of object is ', dir(initializeVariable))
del initializeVariable

print('Destructor manually executed')
print(' the default container component', dir())
# print(' after delete the default container component', dir(initializeVariable)) # get error , bcoz deleted object


# Example E
# =============================================================================================================================================
print("Basic E Example", "-" * 80)


class CreateFunctionWithoutSelf:
    result = 5

    def calculate():
        CreateFunctionWithoutSelf.result += 2
        print("Increment Result : ", CreateFunctionWithoutSelf.result)

    def display():
        print("Display without self used as parameter")

    calculate = staticmethod(calculate)
    display = staticmethod(display)


createFunctionWithoutSelf = CreateFunctionWithoutSelf()
createFunctionWithoutSelf.calculate()
createFunctionWithoutSelf.display()
print("Result for object member variable : ", createFunctionWithoutSelf.result)
print("Result for Class member variable : ", CreateFunctionWithoutSelf.result)

# Example F
# =============================================================================================================================================
print("Basic F Example", "-" * 80)


class Parent1:
    def __int__(self):
        print("Hello Base")

    def display(self):
        print("Base Display")


class Child1:
    def __int__(self):
        print("Hello Derive")

    def display(self):
        print("Derive Display")


# Error get (bcoz Parent1 instead Parent1() )
# parent1 = Parent1
# parent1.display()

base = Parent1()
base.display()
base.__int__()  # How to Print Constructor

child1 = Child1()  # OR
child1.__init__()  # How to Print Constructor
child1.display()
Child1().display()

# Example G
# =============================================================================================================================================
print("Basic G Example", "-" * 80)


class Base_Test(object):
    def __init__(self):
        self.x = 10

    def displayBase(self):
        print("Display of Base Executed", self.x)


class Derived_Test(object):
    def __init__(self):
        self.a = 100

    def displayDerived(self):
        print("display of Derived Executed", self.a)


ob = Derived_Test()
ob.displayDerived()
Base_Test().displayBase()

# Example 1
# =============================================================================================================================================
print("First Example", "-" * 80)


class First:
    class_member = 10


class Second(First):
    pass


class Third(First):
    class_member = 20


class Forth(Second, Third):
    pass


# class Forth(Third, Second): # both are same
#     pass

# class Fifth(Second, Second): # can not pass duplicate value
#     pass

forth = Forth()
print("Class member Value is : ", forth.class_member)
# fifth = Fifth()
# print("Class member Value is : ", fifth.class_member)


print("Second Example", "-" * 80)


# Example 2
# =============================================================================================================================================
class Base1:
    def display_base(self):
        print("Base Display")


class Derived1(Base1):
    def display_derived(self):
        print("Derived Display")


derived1 = Derived1()
derived1.display_base()
derived1.display_derived()
print("*" * 80)
Base1().display_base()

print("Third Example", "-" * 80)


# Example 3
# =============================================================================================================================================
class Base3:
    def display_3(self):
        print(" Base 3 Display 3")

    def test_3(self):
        print("Base 3 Test_Amat 3")


class Derived3(Base3):
    def display_3(self):
        print(" Derived 3 Display 3")

    def test_4(self):
        print("Derived 3 Test_Amat 4")


derived3 = Derived3()  # output : only display only derived function(there is no confusion b/w Base and Derived )
derived3.display_3()

Base3().display_3()  # display base function

print("Forth Example", "-" * 80)


# Example 4
# =============================================================================================================================================
# class Derived4( Base3, Derived3): #get the error (bcoz order is very imp)
class Derived4(Derived3, Base3):
    def test_5(self):
        print(" Derived 4 ")


derived4 = Derived4()
# derived4.display_3() # error (confusion)
derived4.test_5()
derived4.test_4()
derived4.test_3()

print("Fifth Example", "-" * 80)


# Example 5
# =============================================================================================================================================
class Base5:
    def display_5(self):
        print("Base 5 display 5")


class Derived5:
    def display_5(self):
        print("Derived 5 display 5")


# class MultipleInheritance(Base5, Derived5): # Base 5 display 5
class MultipleInheritance(Derived5, Base5):  # Derived 5 display 5
    def multiple_inh(self):
        print("Multiple Inheritance")


multipleInheritance = MultipleInheritance()
multipleInheritance.multiple_inh()
multipleInheritance.display_5()

print("Sixth Example", "-" * 80)


# Example 6
# =============================================================================================================================================
class Base6:
    def calc(self):
        print("Calc of Base Executed")

    def display(self):
        print("Display of Base Exected")


class Derived6(Base6):
    pass


ob = Derived6()
ob.calc()
ob.display()

print("Seventh Example", "-" * 80)


# Example 7
# =============================================================================================================================================
class Base7:
    def calc(self):
        print("Calc of Base executed")

    def display(self):
        print("Display of Base Executed")


class Derived7(Base7):
    def calc(self):
        Base7.calc(self)
        Base7.display(self)
        print("Calc of derived Executed")

    def display(self):
        print("Display of Derived executed")


ob = Derived7()
ob.calc()
ob.display()

print("Eight Example", "-" * 80)


# Example 8
# =============================================================================================================================================
class First:
    @classmethod
    def displayFirst(self):
        print("display of First Executed")


class Second(First):
    @classmethod
    def displaySecond(self):
        print(
            "Display of Second Executed")


class Third(First):
    @classmethod
    def displayThird(self):
        print(
            "display of third Executed")


class Fourth(Second, Third):
    @classmethod
    def displayFourth(self):
        print(
            "display of Fourth Executed")


ob = Fourth()
ob.displayFourth()
ob.displayThird()
ob.displaySecond()
ob.displayFirst()
