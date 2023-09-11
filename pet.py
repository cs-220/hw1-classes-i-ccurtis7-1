from time import time

class PyPet:
    def __init__(self):
        self.start = time()
        self.hatched = False

        print('Congratulations! You have been given a PyPet egg.')

    def care(self):
        pass

    def status(self):
        currentTime = time()
        hatched = currentTime - self.start > 10


        if (not self.hatched) & (not hatched):
            print('Your pet was created {:.0f} s ago'.format(currentTime - self.start))
        elif (not self.hatched) & hatched:
            # What happens when your pet hatches
            print('Congratulations! Your pet just hatched!')
            self.hatched = True
        else:
            # After your pet has hatched
            print('Your pet is just grooving')

    def feed(self):
        pass
