import random
import pygame

pygame.init()
window = pygame.display.set_mode((500,600))
pygame.display.set_caption("Hangman Game")

errors = 0
pressed_key = []

word = open("word.txt", "r")
word = word.readlines()

list_count = len(word) - 1
num = random.randint(0, list_count)

print(word[num])

res = ''.join(word[num].splitlines())

founded_letters = []
errors_letter = []
errors = 0
win = 0

def hangman(num):
    if num == 1:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
    if num == 2:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
    if num == 3:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
        pygame.draw.line(window, (0,0,0), (40,150),(350,150),8)
    if num == 4:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
        pygame.draw.line(window, (0,0,0), (40,150),(350,150),8)
        pygame.draw.line(window, (0,0,0), (175,150),(175,180),8)
    if num == 5:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
        pygame.draw.line(window, (0,0,0), (40,150),(350,150),8)
        pygame.draw.line(window, (0,0,0), (175,150),(175,180),8)
        pygame.draw.circle(window, (0,0,0), (175,200),25,8)
    if num == 6:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
        pygame.draw.line(window, (0,0,0), (40,150),(350,150),8)
        pygame.draw.line(window, (0,0,0), (175,150),(175,180),8)
        pygame.draw.circle(window, (0,0,0), (175,200),25,8)
        pygame.draw.line(window, (0,0,0), (175,225),(175,325),8)
    if num == 7:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
        pygame.draw.line(window, (0,0,0), (40,150),(350,150),8)
        pygame.draw.line(window, (0,0,0), (175,150),(175,180),8)
        pygame.draw.circle(window, (0,0,0), (175,200),25,8)
        pygame.draw.line(window, (0,0,0), (175,225),(175,325),8)
        pygame.draw.line(window, (0,0,0), (200,270),(175,230),8)
    if num == 8:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
        pygame.draw.line(window, (0,0,0), (40,150),(350,150),8)
        pygame.draw.line(window, (0,0,0), (175,150),(175,180),8)
        pygame.draw.circle(window, (0,0,0), (175,200),25,8)
        pygame.draw.line(window, (0,0,0), (175,225),(175,325),8)
        pygame.draw.line(window, (0,0,0), (200,270),(175,230),8)
        pygame.draw.line(window, (0,0,0), (150,270),(175,230),8)
    if num == 9:
        pygame.draw.line(window, (0,0,0), (10,500),(300,500),8)
        pygame.draw.line(window, (0,0,0), (50,150),(50,500),8)
        pygame.draw.line(window, (0,0,0), (40,150),(350,150),8)
        pygame.draw.line(window, (0,0,0), (175,150),(175,180),8)
        pygame.draw.circle(window, (0,0,0), (175,200),25,8)
        pygame.draw.line(window, (0,0,0), (175,225),(175,325),8)
        pygame.draw.line(window, (0,0,0), (200,270),(175,230),8)
        pygame.draw.line(window, (0,0,0), (150,270),(175,230),8)
        pygame.draw.line(window, (0,0,0), (200,370),(175,320),8)

win_count = 0
win_list = []

i = 0

while i < len(res):
    if res.count(res[i]) == 1:
        if  win_list.count(res[i]) == 0:
            win_list.append(res[i])
            win_count+=1
            i+=1
        else:
            i+=1
    elif res.count(res[i]) >= 1:
        if  win_list.count(res[i]) == 0:
            win_list.append(res[i])
            win_count+=1
            i+=1
        else :
            i+=1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            win_list.append(res[i])
        if event.type == pygame.KEYDOWN and ((event.unicode >= 'a' and event.unicode <= 'z') or (event.unicode >= 'A' and event.unicode <= 'Z')):
            letter = event.unicode
            if letter in win_list:
                if founded_letters.count(letter) == 0:
                    founded_letters.append(letter)
                    win+=1
                else:
                    pass
            else:
                errors_letter.append(letter)
                errors+=1
        else:
            pass

    window.fill((255, 255, 255))

    printed_word = ""
    for letter in res:
        if letter in founded_letters:
            printed_word += letter + " "
        else:
            printed_word += "_ "

    if win == win_count:
        hangman(errors)
        you_win = pygame.font.Font(None, 36).render("You Win !", True, (0, 0, 0))
        window.blit(you_win, (190, 250))

    elif errors < 10 and win < win_count:
        hangman(errors)
        word_text = pygame.font.Font(None, 36).render(printed_word, True, (0, 0, 0))
        window.blit(word_text, (50, 50))

        errors_text = pygame.font.Font(None, 36).render("Wrong letters : " + ' '.join(errors_letter), True, (0, 0, 0))
        window.blit(errors_text, (50, 100))

    elif errors == 10:
        hangman(errors)
        game_over = pygame.font.Font(None, 36).render("You Loose...", True, (0, 0, 0))
        window.blit(game_over, (190, 250))

    pygame.display.update()

pygame.quit()