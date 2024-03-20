import pygame,sys,pymunk

def create_balls(space,pos):
    body = pymunk.Body(1,100,body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 40) #Body and radius
    space.add(body,shape)
    return shape

def draw_balls(balls):
    for ball in balls:
        pygame.draw.circle(screen,(0,0,0), ball.body.position, 40)
        ball_rect = ball_surface.get_rect(center = (ball.body.position.x,ball.body.position.y)) #for image surface
        screen.blit(ball_surface,ball_rect)

def static_square(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (450,500)
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape

def draw_static_ball(sball):
    for ball in sball:
            pygame.draw.circle(screen,(0,0,0), ball.body.position, 50)

pygame.init() #initiationg pygame
screen = pygame.display.set_mode((800,800)) # creating the display surface
clock = pygame.time.Clock() #creating the game clock
space = pymunk.Space() #creating the space 
space.gravity = (0,100) # gravity for x and y
ball_surface = pygame.image.load('ball_surface.png') #for image surface
balls = []

sball = []
sball.append(static_ball(space))

while True:
    for event in pygame.event.get(): #checking for user input
        if event.type == pygame.QUIT: #input to close the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(create_balls(space,event.pos))

    screen.fill((217,217,217)) #background color
    draw_balls(balls)
    draw_static_ball(sball)
    space.step(1/50) #updating 
    pygame.display.update() #rendering the frame
    clock.tick(120) #limiting the frames per second to 120