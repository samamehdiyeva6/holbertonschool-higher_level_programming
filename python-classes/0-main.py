#!/usr/bin/python3
Square = __import__('0-square').Square

if __name__ == "__main__":
    my_square = Square()
    print(type(my_square))         # Obyektin növünü çap et
    print(my_square.__dict__)      # Obyektin atributlarını çap et