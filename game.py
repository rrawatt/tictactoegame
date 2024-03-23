import pygame
from pygame.locals import *
import src.tictactoebot as tictactoebot
from src.box import Box

pygame.init()

grey = (33, 33, 33)
slate = (192, 194, 201)
cloud = (123, 123, 123)

WIDTH, HEIGHT = 720, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def victory(board):
    Lis=[]
    for j in range(3):
        sum=0
        for i in range(3):
            sum+=board[j*3+i]
        Lis.append(sum)  #vertical
    for i in range(3):
        sum=0
        for j in range(3):
            sum+=board[j*3+i]
        Lis.append(sum) #horizontal
    sum1=0
    sum2=0
    for i in range(3):
        sum1+=board[i*3+i]
        sum2+=board[(2-i)*3+i]
    Lis.append(sum1) #diag1
    Lis.append(sum2) #diag2
    return Lis


def draw_line(lis):
    for i in range(3):
        if lis[i] == 0 or lis[i] == 3:
            start = (120 + (240) * i, 50)
            end = (120 + (240) * i, 670)
            pygame.draw.line(WIN, cloud, start, end, 10)

    for i in range(3, 6):
        if lis[i] == 0 or lis[i] == 3:
            start = (50, 120 + (240) * (i - 3))
            end = (670, 120 + (240) * (i - 3))
            pygame.draw.line(WIN, cloud, start, end, 10)

    if lis[6] == 0 or lis[6] == 3:
        start = (120, 120)
        end = (600, 600)
        pygame.draw.line(WIN, cloud, start, end, 15)
    elif lis[7] == 0 or lis[7] == 3:
        start = (600, 120)
        end = (120, 600)
        pygame.draw.line(WIN, cloud, start, end, 15)

def main():
    run = True
    clock = pygame.time.Clock()

    boxes = [Box(x, y, 2) for x in range(3) for y in range(3)]

    sumboard=[10 for x in range(9)]

    p = 1
    while run:
        WIN.fill(grey)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for _ in range(9):
                    if boxes[_].is_clicked(pos, event.button == 1, p):
                        p += 1
                        sumboard[_]=p%2
                        break
        
        for box in boxes:
            box.draw_box(WIN)
        if 3 in victory(sumboard) or 0 in victory(sumboard):
            draw_line(victory(sumboard))
            run = False
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
