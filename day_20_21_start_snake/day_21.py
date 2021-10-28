class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('inhale -> exhale')


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print('breathing underwater')
    def swim(self):
        print('moving in water')


nemo = Fish()
nemo.swim()
nemo.breathe()
eye = nemo.num_eyes
print(eye)
