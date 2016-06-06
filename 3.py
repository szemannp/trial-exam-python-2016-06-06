# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume


class Cuboid():

    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def get_surface(self):
        self.surface = (self.width * self.height + self.width * self.length + self.height * self.length) * 2
        return self.surface

    def get_volume(self):
        self.volume = self.width * self.height * self.length
        return self.volume


# stgstg = Cuboid(10, 20, 30)
# 
# print(stgstg.get_surface())
# print(stgstg.get_volume())
