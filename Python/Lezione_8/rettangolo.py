from forma_generica import Forma_generica

class Rettangolo(Forma_generica):

    def __init__(self):
        super().__init__()
        self.set_shape("rettangolo")

    def draw(self):
        print(f"\n {self.get_shape()}\n")

        for i in range(5):
            for j in range(5 * 2):
                if i == 0 or i == 5 - 1:
                    print("*", end = " ")
                elif j == 0 or j == 5 * 2 - 1:
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
            
            print("\n", end = "")