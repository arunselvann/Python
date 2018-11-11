class person:
    def __init__(self):
        print('Hi')

    def __del__(self):
        print('Bye')

    def __a__(self):
        print('GM')


p = person()
p.__a__()
