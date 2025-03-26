import pygame

class Coords():
    def __init__(self ):

        
        width , height = pygame.display.get_surface().get_size()
        topMiddle = (width/2, 0)
        bottomMiddle = (width/2, height)

        middleLeft = (0, height/2)
        middleRight = (width, height/2)



        self.xAxis = (middleLeft, middleRight)
        self.yAxis = (topMiddle,bottomMiddle)
        self.increments = 10

        self.BLACK = (0,0,0)







    def draw(self, screen):
        pygame.draw.line(screen, self.BLACK, self.xAxis[0], self.xAxis[1])
        pygame.draw.line(screen, self.BLACK, self.yAxis[0], self.yAxis[1])

        #draws the tick marks for x axis
        self.increments = self.increments if self.increments >=1 else 1
        for i in range(self.xAxis[0][0], self.xAxis[1][0], self.increments):
                
            pygame.draw.line(screen, self.BLACK, (i, self.xAxis[0][1]+5), (i, self.xAxis[0][1]-5))  
            pygame.draw.line(screen, self.BLACK, (self.yAxis[0][0]+5,i ), (self.yAxis[0][0]-5,i )) 
             


              

    def update(self):
        width , height = pygame.display.get_surface().get_size()
        topMiddle = (width/2, 0)
        bottomMiddle = (width/2, height)

        middleLeft = (0, height/2)
        middleRight = (width, height/2)



        self.xAxis = (middleLeft, middleRight)
        self.yAxis = (topMiddle,bottomMiddle)
        self.increments = self.increments


