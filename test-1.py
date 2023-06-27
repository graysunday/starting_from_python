import pygame , sys, random

class Raindrop:
    def __init__(self):
        self.x = random.randint(0,1000)
        self.y = -5

    def move(self):
        self.y += 7

    def draw(self):
        print("x={} and y={}".format(self.x, self.y))


raindrops = []
count = 0

while 1:
    count += 1
    if count > 5:
        break

    raindrops.append(Raindrop())

    for raindrop in raindrops:
        print("count: "+str(count))
        raindrop.move()
        raindrop.draw()
    

    """i = 0
    while i < len(raindrops):
        raindrops[i].move()
        raindrops[i].draw()
        i += 1
"""

