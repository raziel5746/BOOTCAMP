def instance_check(func):
        def wrapper(self, obj):
            if isinstance(obj, self.__class__):
                output = func(self, obj)
                return output
            else:
                raise TypeError(f"Operation not supported between {self.__class__} and {type(obj)}")
        return wrapper


class Philosophy:
    def __init__(self, general_name, idea_list=[]):
        self.name = general_name
        if isinstance(idea_list, list):
            self.ideas = idea_list
        else:
            raise TypeError("idea_list should be a list")

    def __str__(self):
        paragraph = ""
        for idea in self.ideas:
            paragraph += f"{self.name}: {idea}\n"
        return paragraph

    def __repr__(self):
        return(f"Philosophy Object: {self.name}")

    def __len__(self):
        return len(self.ideas)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self):
            raise StopIteration
        else:
            resolve = self.ideas[self.index]
            self.index += 1
            return resolve

    # def __add__(self, other):
    #     if isinstance(other, self.__class__):
    #         add_name = ' + '.join([self.name, other.name])
    #         return self.__class__(add_name, self.ideas + other.ideas)
    #     else:
    #         raise TypeError(f"Operation not supported between {self.__class__} and {type(other)}")
    

    # def __sub__(self, other):
    #     if isinstance(other, self.__class__):
    #         sub_name = ' - '.join([self.name, other.name])
    #         return self.__class__(sub_name, [idea for idea in self.ideas if idea not in other.ideas])
    #     else:
    #         raise TypeError(
    #             f"Operation not supported between {self.__class__} and {type(other)}")
    
    @instance_check
    def __add__(self, other):
        add_name = ' + '.join([self.name, other.name])
        return self.__class__(add_name, self.ideas + other.ideas)

    @instance_check
    def __sub__(self, other):
        sub_name = ' - '.join([self.name, other.name])
        return self.__class__(sub_name, [idea for idea in self.ideas if idea not in other.ideas])

if __name__ == "__main__":
    general_name = "Existentialism"
    idea_list = ["idea1", "idea2", "idea3"]
    exist = Philosophy(general_name, idea_list)
    print(f"Blah:\n{exist}")
    print(f"Length: {len(exist)}")

    for item in exist:
        print(f"Iterating: {item}")

    s_name = "Structuralism"
    s_list = ["Everything is a structure",
              "Structure your life",
              "idea1"]
    structuralism = Philosophy(s_name, s_list)

    print("exist + structuralism: ")
    print(exist + structuralism)

    print("exist - structuralism: ")
    print(exist - structuralism)
