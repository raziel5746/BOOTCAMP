from star_wars import Jedi
from star_wars import Sith
from star_wars import ForceWielder


def war():
    jedi1 = Jedi()
    jedi2 = Jedi()
    jedi3 = Jedi()
    sith1 = Sith()
    sith2 = Sith()
    sith3 = Sith()

    jedis = [jedi1, jedi2, jedi3]
    siths = [sith1, sith2, sith3]

    j = 0
    losses = 0
    
    while j < 100 and losses < 3:
        for i in range(len(siths)):
            while siths[i].loses == 0:
                jedis[i].fight(siths[i])
                if siths[i].loses == 1:
                    losses += 1
                j += 1
    else:
        if j == 100:
            print("The Siths have won the war, and are taking the galaxy. Finally!\nTan tan tannn, tan taran, tan taran. TAN TAN TANNN, TAN TARANN TAN TARANN.")
        else:
            print("The jedis have won the battle, but not the war!\nOh, wait. They did. :Flies away:")
    print(f"There was a total of {j} fights")

    # if j < 100:
    #     war()


    # for i in range(len(siths)):
    #     while siths[i].loses == 0 and j < 100:
    #         jedis[i].fight(siths[i])
    #         j += 1
            # if siths[i].loses:
            #     dead = siths.pop(i)
            #     print(f"{dead.name} died")