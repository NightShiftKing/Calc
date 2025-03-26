import pygame

class cords():
    def __init__(self ):

        
        WIDTH , HEIGHT = pygame.display.get_surface().get_size()
        TOP_MIDDLE = (WIDTH/2, 0)
        BOTTOM_MIDDLE = (WIDTH/2, HEIGHT)

        MIDDLE_LEFT = (0, HEIGHT/2)
        MIDDLE_RIGHT = (WIDTH, HEIGHT/2)



        self.X_Axis = (MIDDLE_LEFT, MIDDLE_RIGHT)
        self.Y_Axis = (TOP_MIDDLE,BOTTOM_MIDDLE)
        self.Increments = 10

        self.BLACK = (0,0,0)







    def draw(self, screen):
        pygame.draw.line(screen, self.BLACK, self.X_Axis[0], self.X_Axis[1])
        pygame.draw.line(screen, self.BLACK, self.Y_Axis[0], self.Y_Axis[1])

        #draws the tick marks for x axis
        try:
            for i in range(self.X_Axis[0][0], self.X_Axis[1][0], self.Increments):
                
                pygame.draw.line(screen, self.BLACK, (i, self.X_Axis[0][1]+5), (i, self.X_Axis[0][1]-5))  
                pygame.draw.line(screen, self.BLACK, (self.Y_Axis[0][0]+5,i ), (self.Y_Axis[0][0]-5,i )) 
        except ValueError as e:
            if str(e) != "range() arg 3 must not be zero": 
                raise e 
            else:
                self.Increments = 1 


              

    def UPDATE(self):
        WIDTH , HEIGHT = pygame.display.get_surface().get_size()
        TOP_MIDDLE = (WIDTH/2, 0)
        BOTTOM_MIDDLE = (WIDTH/2, HEIGHT)

        MIDDLE_LEFT = (0, HEIGHT/2)
        MIDDLE_RIGHT = (WIDTH, HEIGHT/2)



        self.X_Axis = (MIDDLE_LEFT, MIDDLE_RIGHT)
        self.Y_Axis = (TOP_MIDDLE,BOTTOM_MIDDLE)
        self.Increments = self.Increments


