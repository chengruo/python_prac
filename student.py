class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s:%s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

f = open("C:\\Users\\utsc0990\\Desktop\\startup_Script\\student.py",'a')
f.write('abc')

bart = Student("simpson",95)
print(bart.get_name())
bart.print_score()
print(type(bart))
print(isinstance(bart,Student))
print(dir(bart))