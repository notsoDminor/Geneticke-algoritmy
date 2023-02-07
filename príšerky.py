import random

cage = []

class Monster():
    def __init__(self, temp = []):
        self.dna = []
        if len(temp) == 0:
            for i in range(5):
                self.dna.append(random.randrange(0, 10))
        else:
            self.dna = temp

    def displayer(self):
        print(* self.dna)

    def cute(self):
        return self.dna.count(1)

    def __add__(self, other):
        temp = []
        for i in range(5):
            mutant = random.randrange(0, 101)
            if mutant < 13:
                temp.append(random.randrange(1, 10))
            else:
                parents = random.randrange(0,2)
                if parents == 0:
                    temp.append(self.dna[i])
                else:
                    temp.append(other.dna[i])

        return Monster(temp)

def generation_generator(n):
    for generation in range(n):
        if generation == 0:
            for i in range(10):
                temp = Monster()
                cage.append(temp)
        else:
            cage.sort(key = lambda x: x.cute(), reverse = True)
            for i in range(5):
                cage.pop(5)
            print("PARENTS FROM THE PREVIOUS GENERATION:")
            for i in range(5):
                female = random.randrange(0, 5)
                male = random.randrange(0, 5)
                #print(len(cage))
                while female == male:
                    male = random.randrange(0, 5)
                print((male + 1, female + 1), end = " ")
                child = cage[female] + cage[male]
                cage.append(child)
        print("\n" + "GENERATION " + str(generation + 1) + ":")
        for monster in cage:
            monster.displayer()
        print("\n")


generation_generator(10)
