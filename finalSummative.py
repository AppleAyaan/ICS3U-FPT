from pygame import *
import random

init()
size = width, height = 1000, 700
screen = display.set_mode(size)
display.set_caption('Save Earth: 2550')         #set the caption as the title

#fonts defined:
fontMainScreenTitle = font.Font("Burbank.otf",80) 
fontMenu = font.Font("Burbank.otf", 50)
fontVersion = font.Font("Burbank.otf", 35)
fontWelcomeScreen = font.SysFont("Didot", 60)
fontWelcomeScreenSmall = font.SysFont("Didot", 40)
fontSkip = font.SysFont("Times New Roman", 40)
fontBack = font.Font("Burbank.otf", 45)
#GAME 1
fontGameOneBegin = font.Font("Burbank.otf",100) 
fontGameOneQuestion = font.SysFont("Courier", 40)
fontGameOneAnswer = font.SysFont("Courier", 50)
fontCorrectWrong = font.Font("Burbank.otf", 90)
#GAME 2
fontScore = font.SysFont("Times New Roman",50, True)
fontInstructions = font.SysFont("Times New Roman", 30)
fontMeter = font.SysFont("Times New Roman", 20)
fontStage = font.SysFont("Courier", 100, True)
fontWinLose = font.Font("Burbank.otf", 120)
#GAME 3
fontRound = font.Font('Burbank.otf', 80)
fontBeginRound = font.SysFont("Times New Roman", 120, True)
fontRPS = font.Font('Burbank.otf', 40)
fontScore = font.Font('Burbank.otf', 40)
fontScoreText = font.SysFont('Burbank.otf', 70)
#CREDIT SCREEN
fontWelcomeScreenTitle = font.SysFont("Didot", 90)

#images load
recyclingBin = image.load("recyclingBin.webp") 
transformedRecyclingBinGameTwo = transform.scale(recyclingBin, (300, 200))
RAWmeter = image.load("recyclingMeter.png")
meter = transform.scale(RAWmeter, (50, 300))
RAWleftArrow = image.load("leftArrow.png")
leftArrow = transform.scale(RAWleftArrow, (25, 25))
mainScreenBackground = image.load("mainScreenBackground.png")          	 	
transformedMainScreenBackground = transform.scale(mainScreenBackground, (1000,700))
transformedEarth = transform.scale((image.load("earth.png")),(600, 600))
mainScreenBackground = image.load("mainScreenBackground.png")          
transformedMainScreenBackground = transform.scale(mainScreenBackground, (1000,700))  
tvShowIcon = image.load("tvShow.png") 
transformedtvShowIcon = transform.scale(tvShowIcon, (130,130))
recyclingBinIcon = image.load("recyclingBin.png") 
transformedRecyclingBin = transform.scale(recyclingBinIcon, (180, 180))
TBD = image.load("TBD.png") 
transformedTBD = transform.scale(TBD, (150, 150))
tvShowBackground = image.load("tvShowBackground.jpeg")          	 
transformedTVShowBackground = transform.scale(tvShowBackground, (1000,700))
gameOneLivesImage = image.load("gameOneLivesImage.png")         
transformedGameOneLivesImage = transform.scale(gameOneLivesImage, (75,75))
garbageOne = image.load("garbageOne.webp")
transformedGarbageOne = transform.scale(garbageOne, (100, 100))
garbageTwo = image.load("garbageTwo.png")
transformedGarbageTwo = transform.scale(garbageTwo, (100, 100))
garbageThree = image.load("garbageThree.webp")
transformedGarbageThree = transform.scale(garbageThree, (100, 100))
garbageFour = image.load("garbageFour.png")
transformedGarbageFour = transform.scale(garbageFour, (100, 100))
garbageFive = image.load("garbageFive.png")
transformedGarbageFive = transform.scale(garbageFive, (100, 100))
instructions = image.load('instructions.png')
transformedInstructions = transform.scale(instructions, (1000, 700))
RPSIcon = image.load('rockPaperScissorsIcon.png')
transformedRPSIcon = transform.scale(RPSIcon, (130, 130))
RAWRPSBackground = image.load('RPSBackground.png')
RPSBackground = transform.scale(RAWRPSBackground, (1000, 700))
rock = image.load('rock.png')
transformedRock = transform.scale(rock, (300, 300))
paper = image.load('paper.png')
transformedPaper = transform.scale(paper, (300, 300))
scissor = image.load('scissor.png')
transformedScissor = transform.scale(scissor, (300, 300))
tick = image.load("tick.png")
transformedTick = transform.scale(tick, (200, 200))
cross = image.load("cross.webp")
transformedCross = transform.scale(cross, (75, 75))
recyclingBinIcon = image.load("recyclingBin.png") 
transformedRecyclingBin = transform.scale(recyclingBinIcon, (180, 180))
gameTwoBackground = image.load('gameTwoBackground.jpeg')
gameTwoBackground = transform.scale(gameTwoBackground, (1000, 700))
TBDRPS = transform.scale(TBD, (300, 300))
lock = image.load('lock.png')
transformedLock = transform.scale(lock, (125, 125))

#sound files:
menuMusic = mixer.Sound('menuMusic.mp3')    	 	
menuMusic.set_volume(0.5)
gameOneMusic = mixer.Sound('gameOneMusic.mp3')
gameOneMusic.set_volume(0.5)
correctChoice = mixer.Sound('correctChoice.mp3')
wrongChoice = mixer.Sound('wrongChoice.mp3')
crowdCheer = mixer.Sound('crowdCheer.mp3')
crowdCheer.set_volume(0.5)
crowdBoo = mixer.Sound('crowdBoo.mp3')
gameTwoMusic = mixer.Sound('gameTwoMusic.mp3')
gameTwoMusic.set_volume(0.5)
stage = mixer.Sound('stage.mp3')
garbage = mixer.Sound('garbage.mp3')
youWin = mixer.Sound('youWin.mp3')
youLose = mixer.Sound('youLose.mp3')
RPSCountdown = mixer.Sound('RPSCountdown.mp3')

#colours defined:
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BEIGE = 255, 241, 204
DARKGREEN = 0, 185, 0
DARKRED = 185, 0, 0

#initializing variables
backgroundX = 0
user_name = ''
nameGiven = False
gameOneRunning = False

#STATES
STATE_MAIN = 0
STATE_WELCOME = 1
STATE_PLAY_SCREEN = 2
STATE_PLAY_GAME1 = 3
STATE_PLAY_GAME2 = 4
STATE_PLAY_GAME3 = 5
STATE_GAME1_WIN = 6
STATE_GAME1_LOSE = 7
STATE_GAME2_WIN = 8
STATE_GAME2_LOSE = 9
STATE_GAME3_WIN = 10
STATE_GAME3_LOSE = 11
STATE_GAME3_WELCOME = 12
STATE_CREDIT_SCREEN = 13
STATE_INSTRUCTIONS = 14
STATE_QUIT = 15

#FUNCTIONS ---------------------------------------------------------------------
def mainScreen(mx, my, button, backx):
    global state
    
    #left side
    screen.blit(transformedMainScreenBackground, Rect(backx,0,width,height))    
    #right side
    screen.blit(transformedMainScreenBackground, Rect(backx + width, 0, width, height))
    #earth drawing
    screen.blit(transformedEarth, (450, 175, 350, 350))
    
    #TITLE DRAWING
    title = fontMainScreenTitle.render("Save Earth: 2550 ®" , 1, WHITE)	
    screen.blit(title, (300,10,400,100))	
    
    #VERSION 
    versionText = fontVersion.render(str(version), 1, WHITE)
    screen.blit(versionText, (890, 670, 100, 100))
    
    #making the 3 buttons on main screen
    #taken from "samplemenu.py" on BrightSpace
    blockWidth = width//3
    blockHeight = height//6      
    
    mainScreenList = [Rect(25, 100 + blockHeight, blockWidth, blockHeight), #play button
                Rect(25, 250 + blockHeight, blockWidth, blockHeight), #instructions button
                Rect(25, 400 + blockHeight, blockWidth, blockHeight)] #quit button   
    stateList = [STATE_WELCOME, STATE_INSTRUCTIONS, STATE_QUIT]
    titleList = ["PLAY", "INSTRUCTIONS", "QUIT"]

    for i in range(len(mainScreenList)):
        rect = mainScreenList[i] #get the current Rect
        draw.rect(screen, BLACK, rect)  # draw the Rect
        text = fontMenu.render(titleList[i] , 1, WHITE)	# make the font`
        textWidth, textHeight = fontMenu.size(titleList[i]) # get the font size
        useW = (blockWidth - textWidth)//2  #use for centering
        useH = (blockHeight - textHeight)//2
        #getting a centered Rectangle
        textRect = Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
        screen.blit(text, textRect)	# draw to screen
        #hover effect on buttons
        if rect.collidepoint(mx, my):
            draw.rect(screen, RED, rect, 2)
            text = fontMenu.render(titleList[i] , 1, RED)	# make the font
            textWidth, textHeight = fontMenu.size(titleList[i]) # get the font size
            useW = (blockWidth - textWidth)//2  #use for centering
            useH = (blockHeight - textHeight)//2
            # getting a centered Rectangle
            textRect = Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
            screen.blit(text, textRect)	# draw to screen
            
            if button == 1:
                state = stateList[i] 
    return(state)
def welcomeScreen(mx, my, button, user_name):
    screen.fill(BLACK)
    
    #fade in the text
    for textFadeIn in range (0, 255, 20):
        text = fontWelcomeScreen.render("Welcome " + user_name , 1, (textFadeIn, textFadeIn, textFadeIn))	
        screen.blit(text, (350 - (12*len(user_name)),280,400,100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (240, -1, -20):
        text = fontWelcomeScreen.render("Welcome " + user_name, 1, (textFadeOut, textFadeOut, textFadeOut))	
        screen.blit(text, (350 - (12*len(user_name)),280,400,100))
        display.update()
        time.wait(100)
    screen.fill(BLACK)
    
    #main story
    #fade in the text
    for textFadeIn in range (0, 255, 17):
        text = fontWelcomeScreenSmall.render("You must save Earth before it's too late..." , 1, (textFadeIn, textFadeIn, textFadeIn))	
        screen.blit(text, (50,280,400,100))
        text2 = fontWelcomeScreenSmall.render("Humanity depends on you.", 1, (textFadeIn, textFadeIn, textFadeIn))
        screen.blit(text2, (50, 325, 400, 100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (240, -1, -17):
        text = fontWelcomeScreenSmall.render("You must save Earth before it's too late...", 1, (textFadeOut, textFadeOut, textFadeOut))	
        screen.blit(text, (50,280,400,100))
        text2 = fontWelcomeScreenSmall.render("Humanity depends on you.", 1, (textFadeOut, textFadeOut, textFadeOut))
        screen.blit(text2, (50, 325, 400, 100))        
        display.update()
        time.wait(100)
    screen.fill(BLACK)    
    
    #fade in the text
    for textFadeIn in range (0, 255, 20):
        text = fontWelcomeScreen.render("Good luck." , 1, (textFadeIn, textFadeIn, textFadeIn))	
        screen.blit(text, (350,280,400,100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (240, -1, -20):
        text = fontWelcomeScreen.render("Good luck.", 1, (textFadeOut, textFadeOut, textFadeOut))	
        screen.blit(text, (350,280,400,100))
        display.update()
        time.wait(100)
    screen.fill(BLACK)       
def playScreen(mx, my, button, backx):  
    global transformedtvShowIcon
    global transformedRecyclingBin
    global transformedTBD
    global playSound
    
    #background
    screen.fill(BLACK)
    #left side
    screen.blit(transformedMainScreenBackground, Rect(backx,0,width,height))    
    #right side
    screen.blit(transformedMainScreenBackground, Rect(backx + width, 0, width, height))    
    
    #title 
    title = fontMainScreenTitle.render("Save Earth: 2550 ®" , 1, WHITE)	
    screen.blit(title, (300,10,400,100))	
    
    #First Challenge TV SHOW -----------------------------------------------------------
    #display icon
    tvShowRect = Rect(150, 250, 130, 135)
    if tvShowRect.collidepoint(mx,my):
        if button == 1:
            playSound = True
            return(STATE_PLAY_GAME1) #tv show game is clicked
        tvShowRect = Rect(145, 240, 130, 140)
        transformedtvShowIconR = transform.rotate(transformedtvShowIcon, 10)
        screen.blit(transformedtvShowIconR, (135, 235, 100, 100))
        draw.rect(screen, RED, tvShowRect, 2)
    else:
        screen.blit(transformedtvShowIcon, (150, 250, 100, 100)) 
    
    tvShowText = fontMenu.render("TV Show", 1, WHITE)
    levelOne = fontMenu.render("Level I", 1, WHITE)
    screen.blit(levelOne, (150, 435, 100, 100))
    screen.blit(tvShowText, (150, 390, 100, 100))
    
    #Second Challenge -----------------------------------------------------------
    #display icon
    recyclingBinRect = Rect(440, 260, 100, 130)
    if recyclingBinRect.collidepoint(mx, my):
        transformedRecyclingBinR = transform.rotate(transformedRecyclingBin, 10)
        screen.blit(transformedRecyclingBinR, (385, 215, 100, 100))
        draw.rect(screen, RED, recyclingBinRect, 2)
    else:
        screen.blit(transformedRecyclingBin, (400, 235, 100, 100))
    
    #display lock icon
    screen.blit(transformedLock, (425, 260, 100, 100))
    
    recyclingBinText = fontMenu.render("Recy-catch", 1, WHITE)
    levelTwo = fontMenu.render("Level II", 1, WHITE)
    screen.blit(levelTwo, (400, 435, 100, 100))
    screen.blit(recyclingBinText, (400, 390, 100, 100))
    
    #Third Challenge -----------------------------------------------------------
    #display icon
    TBDRect = Rect(725, 235, 100, 100)
    screen.blit(transformedTBD, TBDRect)
    
    return(STATE_PLAY_SCREEN) 
def instructionScreen(mx, my, button, backx):
    #BACKGROUND
    #left side
    screen.blit(transformedMainScreenBackground, Rect(backx,0,width,height))    
    #right side
    screen.blit(transformedMainScreenBackground, Rect(backx + width, 0, width, height))

    #INSTRUCTIONS
    screen.blit(transformedInstructions, (0, 0))

    #BACK BUTTON
    backButtonRect = Rect(10, 10, 100, 50)
    
    if backButtonRect.collidepoint(mx, my):
        if button == 1:
            return(STATE_MAIN)
        draw.rect(screen, BLACK, backButtonRect)
        draw.rect(screen, RED, backButtonRect, 3)
        back = fontBack.render("BACK", 1, RED)
        screen.blit(back, (20, 17, 100, 50))
    else:
        draw.rect(screen, BLACK, backButtonRect)
        back = fontBack.render("BACK", 1, WHITE)
        screen.blit(back, (20, 17, 100, 50))
    return(STATE_INSTRUCTIONS)
def gameOneScreen(mx, my, button):
    global gameOneRunning
    global currentQuestionIndex
    global playSound
  
    gameOneWin = False
    gameOneLose = False    
    
    
    #BACKGROUND 
    screen.blit(transformedTVShowBackground, (0, 0, 1000, 700))
    
    #button to start the game
    startGameOneRect = Rect(415, 245, 190, 90)
    if startGameOneRect.collidepoint(mx, my):
        if button == 1:
            gameOneRunning = True
            currentQuestionIndex = 0
        startGameOne = fontGameOneBegin.render("START", 1, RED)
    else:
        startGameOne = fontGameOneBegin.render("START", 1, WHITE)
    
    screen.blit(startGameOne, startGameOneRect)
    
     
    if gameOneRunning == True:
        currentQuestionIndex, gameOneRunning, gameOneWin, gameOneLose = question(mx, my, button, currentQuestionIndex) 
        if gameOneWin == True:    
            playSound = True
            return(STATE_GAME1_WIN) 
        
        elif gameOneLose == True:
            playSound = True
            return(STATE_GAME1_LOSE)        
    return(STATE_PLAY_GAME1)
def question(mx, my, button, currentQuestionIndex):    
    global mouseRect
    global gameOneLives
    global gameOneRunning
    global gameOneWin
    global gameOneLose
    
    mouseRect = Rect(mx, my, 2, 2)
    
    #fill the screen and draw the question Rect
    screen.fill(BLACK)
              
    #list of questions to give to the user
    questionList = [
        'What is the annual weight of waste & produced per capita in Canada ? & (kg)',
        'How much e-waste is generated per & capita in Canada ? & (kg)',
        'Which color bin is for recycling in & Canada?',
        'How much percent of waste goes as & recycling in Canada in 2019? ',
        'How much of the total country area & does Canada\'s forests take up?'
    ]
    
    #the possible choices for each question
    questionChoices = [
        '600kg','657kg','720kg','873kg',
        '22.5kg','25.3kg','28.9kg','34.6kg',
        'Red','Green','Blue','Yellow',
        '9%','10%','11%','12%',
        '25%','30%','35%','40%'
    ]
    
    #correct answer
    correctAnswer = [
        2,
        1,
        2,
        0,
        3
        ]
    
    
    screen.blit(transformedTVShowBackground, (0, 0, 1000, 700))
    
    #show the amount of lives on the screen
    offsetX = 0
    for life in range (0, gameOneLives):
        screen.blit(transformedGameOneLivesImage, (385 + offsetX, 250, 150, 150))
        offsetX += 80
    #questionRect
    questionRect = (75, 15, 850, 175)
    draw.rect(screen, BLACK, questionRect)
    #choices Rect
    choiceList = [(20, 500, 460, 80), (500, 500, 460, 80),(20, 600, 460, 80), (500, 600, 460, 80)]
    #draw all four answer boxes
    for dimensions in choiceList:
        choiceRect = Rect(dimensions)
        draw.rect(screen, WHITE, choiceRect)
    #draw four choices
    k = 0
    for j in range(4*currentQuestionIndex, 4*(currentQuestionIndex+1)):
        if mouseRect.colliderect(choiceList[k]) != 1:
            choice = fontGameOneAnswer.render(questionChoices[j], 1, BLACK)
            screen.blit(choice, Rect(choiceList[k]))
            k += 1
        else:
            choice = fontGameOneAnswer.render(questionChoices[j], 1, RED)  #if hovered over, display text as red
            draw.rect(screen, RED, Rect(choiceList[k]), 2)          #and display boxes with an outline of red size 2
            screen.blit(choice, Rect(choiceList[k])) 
            k += 1
        
    

    #QUESTION
    #split the questions in order to get text formatted correctly
    questionSplit = questionList[currentQuestionIndex].split('&')
    offsetY = 0
    
    #print the questions
    for n in range(0, len(questionSplit)):
        question = fontGameOneQuestion.render(questionSplit[n], 1, WHITE)
        screen.blit(question ,(75, offsetY+15, 850, 175))
        offsetY += 45
    
    display.update()
    
    #get user input
    answerCheck = mouseRect.collidelist(choiceList)
    if answerCheck != -1:
        if button == 1:
            if answerCheck == correctAnswer[currentQuestionIndex]:
                currentQuestionIndex += 1
                #play correct sound effect
                correctChoice.play()
                crowdCheer.play()
                
                
                #display user clicked on correct answer
                for w in range(0, 2):
                    draw.rect(screen, BLACK, (345, 230, 320, 105))
                    win = fontCorrectWrong.render("Correct", 1, WHITE)
                    screen.blit(win, (395, 245, 400, 150))
                    display.update()
                    time.wait(250)
                    win = fontCorrectWrong.render("Correct", 1, GREEN)
                    screen.blit(win, (395, 245, 400, 150))      
                    draw.rect(screen, GREEN, (345, 230, 320, 105), 5)
                    display.update()
                    time.wait(250)                     
            else:
                #player wrong sound effect
                crowdBoo.play()
                wrongChoice.play()
                
                gameOneLives -= 1
                if gameOneLives <= 0:
                    gameOneRunning = False
                    gameOneLose = True
                    return(currentQuestionIndex, gameOneRunning, gameOneWin, gameOneLose)
                #display user clicked on wrong answer
                for l in range(0, 2):
                    draw.rect(screen, BLACK, (345, 230, 320, 105))
                    win = fontCorrectWrong.render("Wrong", 1, WHITE)
                    screen.blit(win, (405, 235, 400, 150))
                    display.update()
                    time.wait(250)
                    win = fontCorrectWrong.render("Wrong", 1, RED)
                    screen.blit(win, (405, 235, 400, 150))      
                    draw.rect(screen, RED, (345, 230, 320, 105), 5)
                    display.update()
                    time.wait(250)                   
                
    if currentQuestionIndex > 4:
        gameOneRunning = False
        gameOneWin = True
        return(currentQuestionIndex, gameOneRunning, gameOneWin, gameOneLose)
    return(currentQuestionIndex, gameOneRunning, gameOneWin, gameOneLose)
def gameOneWinScreen(mx, my, button, backx):
    global transformedtvShowIcon
    global tvShowIcon
    global transformedRecyclingBin
    global playSound
    
    #background
    screen.fill(BLACK)
    #left side
    screen.blit(transformedMainScreenBackground, Rect(backx,0,width,height))    
    #right side
    screen.blit(transformedMainScreenBackground, Rect(backx + width, 0, width, height))    
    
    #title 
    title = fontMainScreenTitle.render("Save Earth: 2550 ®" , 1, WHITE)	
    screen.blit(title, (300,10,400,100))	
    
    #First Challenge TV SHOW -----------------------------------------------------------
    #display icon
    tvShowRect = Rect(150, 250, 130, 135)
    
    if tvShowRect.collidepoint(mx,my):
        tvShowRect = Rect(145, 240, 130, 140)
        transformedtvShowIconRot = transform.rotate(transformedtvShowIcon, 10)
        screen.blit(transformedtvShowIconRot, (135, 235, 100, 100))
        draw.rect(screen, RED, tvShowRect, 2)
    else:
        screen.blit(transformedtvShowIcon, (150, 250, 100, 100)) 
    
    
    tvShowText = fontMenu.render("TV Show", 1, WHITE)
    levelOne = fontMenu.render("Level I", 1, GREEN)
    screen.blit(levelOne, (150, 435, 100, 100))
    screen.blit(tvShowText, (150, 390, 100, 100))
    screen.blit(transformedTick, (135, 250, 100, 100))   # FIRST CHALLENGE COMPLETE
    
    #Second Challenge -----------------------------------------------------------
    #display icon
    recyclingBinRect = Rect(440, 260, 100, 130)
    if recyclingBinRect.collidepoint(mx, my):
        if button == 1:
            playSound = True
            return(STATE_PLAY_GAME2) #recycling bin game is clicked
        transformedRecyclingBinRot = transform.rotate(transformedRecyclingBin, 10)
        screen.blit(transformedRecyclingBinRot, (385, 215, 100, 100))
        draw.rect(screen, RED, recyclingBinRect, 2)
    else:
        screen.blit(transformedRecyclingBin, (400, 235, 100, 100))
    
    recyclingBinText = fontMenu.render("Recy-catch", 1, WHITE)
    levelTwo = fontMenu.render("Level II", 1, WHITE)
    screen.blit(levelTwo, (400, 435, 100, 100))
    screen.blit(recyclingBinText, (400, 390, 100, 100))
    #Third Challenge -----------------------------------------------------------
    TBDRect = Rect(725, 235, 100, 100)
    screen.blit(transformedTBD, TBDRect)
    
    return(STATE_GAME1_WIN)  
def gameOneLoseScreen(mx, my, button, backx):
    #background
    screen.fill(BLACK)
    #left side
    screen.blit(transformedMainScreenBackground, Rect(backx,0,width,height))    
    #right side
    screen.blit(transformedMainScreenBackground, Rect(backx + width, 0, width, height))    
    
    #title 
    title = fontMainScreenTitle.render("Save Earth: 2550 ®" , 1, WHITE)	
    screen.blit(title, (300,10,400,100))	
    
    #First Challenge TV SHOW -----------------------------------------------------------
    #display icon
    tvShowRect = Rect(150, 250, 130, 135)
    
    if tvShowRect.collidepoint(mx,my):
        if button == 1:
            return(STATE_PLAY_GAME1)
        tvShowRect = Rect(145, 240, 130, 140)
        transformedtvShowIconRot = transform.rotate(transformedtvShowIcon, 10)
        screen.blit(transformedtvShowIconRot, (135, 235, 100, 100))
        draw.rect(screen, RED, tvShowRect, 2)
    else:
        screen.blit(transformedtvShowIcon, (150, 250, 100, 100)) 
    
    
    tvShowText = fontMenu.render("TV Show", 1, WHITE)
    levelOne = fontMenu.render("Level I", 1, RED)
    screen.blit(levelOne, (150, 435, 100, 100))
    screen.blit(tvShowText, (150, 390, 100, 100))
    screen.blit(transformedCross, (155, 475, 100, 100))   # FIRST CHALLENGE FAILED
    tryAgain = fontMenu.render("TRY AGAIN.", 1, RED)
    screen.blit(tryAgain, (125, 550, 100, 100))
    
    #Second Challenge -----------------------------------------------------------
    #display icon
    recyclingBinRect = Rect(440, 260, 100, 130)
    if recyclingBinRect.collidepoint(mx, my):
        transformedRecyclingBinRot = transform.rotate(transformedRecyclingBin, 10)
        screen.blit(transformedRecyclingBinRot, (385, 215, 100, 100))
        draw.rect(screen, RED, recyclingBinRect, 2)
    else:
        screen.blit(transformedRecyclingBin, (400, 235, 100, 100))
    
    recyclingBinText = fontMenu.render("Recy-catch", 1, WHITE)
    levelTwo = fontMenu.render("Level II", 1, WHITE)
    screen.blit(levelTwo, (400, 435, 100, 100))
    screen.blit(recyclingBinText, (400, 390, 100, 100))
    #Third Challenge -----------------------------------------------------------
    TBDRect = Rect(725, 235, 100, 100)
    screen.blit(transformedTBD, TBDRect)
    
    return(STATE_GAME1_LOSE)     
def gameTwoScreen(mx, my, button, rectList):
    #background of game two screen
    screen.blit(gameTwoBackground, (0, 0, 1000, 700))
    
    global recyclingBinRect
   
    #recycling bin position 
    recyclingBinPos = recyclingBinX, 525, 100, 100
    screen.blit(transformedRecyclingBinGameTwo, (recyclingBinPos))
    recyclingBinRect = Rect(recyclingBinPos[0] + 45, recyclingBinPos[1] + 15, recyclingBinPos[2]+ 120, recyclingBinPos[3])
    
    #meter on the left side
    stageOne = fontMeter.render("7", 1, BLACK)
    stageTwo = fontMeter.render("15", 1, BLACK)
    stageThree = fontMeter.render("25", 1, BLACK)
    screen.blit(stageOne, (5, 275, 100, 100))
    screen.blit(stageTwo, (5, 375, 100, 100))
    screen.blit(stageThree, (5, 470, 100, 100))
    
    screen.blit(meter, (25, 185, 100, 100))
    screen.blit(leftArrow, (80, arrowY, 100, 100))
    
    #draw the rectangles
    for i in range(0, len(rectList)):
        screen.blit(garbageList[i], Rect(rectList[i]))
    
    #score and instructions
    text = fontScore.render("Score :" + str(score) , 1, RED)
    screen.blit(text, (10,100,300,200))  
    text = fontInstructions.render("Reach a score of 25 to win." , 1, RED)
    screen.blit(text, (5,150,300,200))        
    display.update()
    
    return(STATE_PLAY_GAME2)
def garbageInit():
    choice = random.choice([transformedGarbageOne,transformedGarbageTwo,transformedGarbageThree,transformedGarbageFour,transformedGarbageFive])
    return(choice)
def speed(numberORectangles):
    speedList = []
    for s in range (0, numberOfRectangles):
        if score <= 5:
            speedList.append(random.uniform(0.5, 1.2))
        elif score <= 15 and score >= 6:
            speedList.append(random.uniform(1.8, 2.5))
        elif score <= 26 and score >= 16:
            speedList.append(random.uniform(2.8, 3.5))
    return (speedList)
def initRect():
    rectangle = []
    rectangle.append(random.randint(100, width-100))
    rectangle.append(random.randint(-300, 50))
    rectangle.append(100)
    rectangle.append(100)
    return(rectangle)
def gameTwoWinScreen(mx, my, button, backx):
    global transformedMainScreenBackground
        
    #background
    screen.fill(BLACK)
    #left side
    screen.blit(transformedMainScreenBackground, Rect(backx,0,width,height))    
    #right side
    screen.blit(transformedMainScreenBackground, Rect(backx + width, 0, width, height))    
    
    #title 
    title = fontMainScreenTitle.render("Save Earth: 2550 ®" , 1, WHITE)	
    screen.blit(title, (300,10,400,100))	
    
    #First Challenge TV SHOW -----------------------------------------------------------
    #display icon
    tvShowRect = Rect(150, 250, 130, 135)
    
    if tvShowRect.collidepoint(mx,my):
        tvShowRect = Rect(145, 240, 130, 140)
        transformedtvShowIconRot = transform.rotate(transformedtvShowIcon, 10)
        screen.blit(transformedtvShowIconRot, (135, 235, 100, 100))
        draw.rect(screen, RED, tvShowRect, 2)
    else:
        screen.blit(transformedtvShowIcon, (150, 250, 100, 100)) 
    
    
    tvShowText = fontMenu.render("TV Show", 1, WHITE)
    levelOne = fontMenu.render("Level I", 1, GREEN)
    screen.blit(levelOne, (150, 435, 100, 100))
    screen.blit(tvShowText, (150, 390, 100, 100))
    screen.blit(transformedTick, (135, 250, 100, 100))   # FIRST CHALLENGE COMPLETE
    
    #Second Challenge -----------------------------------------------------------
    #display icon
    recyclingBinRect = Rect(440, 260, 100, 130)
    if recyclingBinRect.collidepoint(mx, my):
        transformedRecyclingBinRot = transform.rotate(transformedRecyclingBin, 10)
        screen.blit(transformedRecyclingBinRot, (385, 215, 100, 100))
        draw.rect(screen, RED, recyclingBinRect, 2)
    else:
        screen.blit(transformedRecyclingBin, (400, 235, 100, 100))
    
    recyclingBinText = fontMenu.render("Recy-catch", 1, WHITE)
    levelTwo = fontMenu.render("Level II", 1, GREEN)
    screen.blit(levelTwo, (400, 435, 100, 100))
    screen.blit(recyclingBinText, (400, 390, 100, 100))
    screen.blit(transformedTick, (415, 250, 100, 100))   # SECOND CHALLENGE COMPLETE
    #Third Challenge -----------------------------------------------------------
    RPSIconRect = Rect(725, 260, 125, 125)
    
    if RPSIconRect.collidepoint(mx, my):
        if button == 1:
            return(STATE_GAME3_WELCOME)
        transformedRPSIconRot = transform.rotate(transformedRPSIcon, 10)
        screen.blit(transformedRPSIconRot, (710, 235, 100, 100))
        draw.rect(screen, RED, (720, 250, 130, 125), 2)
    else:
        screen.blit(transformedRPSIcon, (RPSIconRect))
      
    RPSText = fontMenu.render("Rock Paper Scissors", 1, WHITE)
    levelThree = fontMenu.render("Level III", 1, WHITE)
    screen.blit(levelThree, (665, 435, 125, 125))
    screen.blit(RPSText, (665, 390, 125, 125))
    
    return(STATE_GAME2_WIN)  
def gameTwoLoseScreen(mx, my, button, backx):
    global playAgain2
    global transformedMainScreenBackground
    global playSound
        
    #background
    screen.fill(BLACK)
    #left side
    screen.blit(transformedMainScreenBackground, Rect(backx,0,width,height))    
    #right side
    screen.blit(transformedMainScreenBackground, Rect(backx + width, 0, width, height))    
    
    #title 
    title = fontMainScreenTitle.render("Save Earth: 2550 ®" , 1, WHITE)	
    screen.blit(title, (300,10,400,100))	
    
    #First Challenge TV SHOW -----------------------------------------------------------
    #display icon
    tvShowRect = Rect(150, 250, 130, 135)  
    
    if tvShowRect.collidepoint(mx,my):
        tvShowRect = Rect(145, 240, 130, 140)
        transformedtvShowIconRot = transform.rotate(transformedtvShowIcon, 10)
        screen.blit(transformedtvShowIconRot, (135, 235, 100, 100))
        draw.rect(screen, RED, tvShowRect, 2)
    else:
        screen.blit(transformedtvShowIcon, (150, 250, 100, 100)) 
    
    
    tvShowText = fontMenu.render("TV Show", 1, WHITE)
    levelOne = fontMenu.render("Level I", 1, GREEN)
    screen.blit(levelOne, (150, 435, 100, 100))
    screen.blit(tvShowText, (150, 390, 100, 100))
    screen.blit(transformedTick, (135, 250, 100, 100))   # FIRST CHALLENGE COMPLETE
    
    #Second Challenge -----------------------------------------------------------
    #display icon
    recyclingBinRect = Rect(440, 260, 100, 130)
    if recyclingBinRect.collidepoint(mx, my):
        if button == 1:
            playAgain2= True
            playSound = True
            return(STATE_PLAY_GAME2) #recycling bin game is clicked
        transformedRecyclingBinRot = transform.rotate(transformedRecyclingBin, 10)
        screen.blit(transformedRecyclingBinRot, (385, 215, 100, 100))
        draw.rect(screen, RED, recyclingBinRect, 2)
    else:
        screen.blit(transformedRecyclingBin, (400, 235, 100, 100))
    
    recyclingBinText = fontMenu.render("Recy-catch", 1, WHITE)
    levelTwo = fontMenu.render("Level II", 1, RED)
    screen.blit(levelTwo, (400, 435, 100, 100))
    screen.blit(recyclingBinText, (400, 390, 100, 100))
    screen.blit(transformedCross, (415, 475, 100, 100))   # SECOND CHALLENGE FAILED
    tryAgain = fontMenu.render("TRY AGAIN.", 1, RED)
    screen.blit(tryAgain, (385, 550, 100, 100))
        
    #Third Challenge -----------------------------------------------------------
    TBDRect = Rect(725, 235, 100, 100)
    screen.blit(transformedTBD, TBDRect)
    
    return(STATE_GAME2_LOSE)    
def gameThreeScreen(mx, my, button, mouseRect):
    global playerScore
    global AIScore
    global roundNumber
    global playSound
    
    #BACKGROUND
    screen.blit(RPSBackground, (0, 0, 1000, 700))
    
    #round text on top
    roundNum = fontRound.render('Round ' + str(roundNumber), 1, BEIGE)
    screen.blit(roundNum, (400, 25, 200, 200))   
    #each player score
    playerScoreText = fontScore.render('Player\'s Score: ' + str(playerScore), 1, BLUE)
    AIScoreText = fontScore.render('AI\'s Score: ' + str(AIScore), 1, RED)
    screen.blit(playerScoreText, (75, 80, 100, 100))
    screen.blit(AIScoreText, (600, 80, 100, 100))
    
    #display question mark since they haven't clicked on anything yet
    screen.blit(TBDRPS, (90, 190))         #Player SIDE
    screen.blit(TBDRPS, (615, 190))         #AI SIDE
    
    #list of rects to click on 
    listRect = [Rect(45, 615, 125, 60), Rect(180, 615, 125, 60), Rect(315, 615, 125, 60)] 
    #list of choice rects
    RPSChoice_pos = [Rect(75, 625, 125, 60), Rect(200, 625, 125, 60), Rect(330, 625, 125, 60)]
    #list of choices
    RPSChoice = ['Rock', 'Paper', 'Scissor']
    
    if playerScore == 2:
        playSound = True
        #winning screen
        #print flashing you win in green and black
        for w in range(0, 6):
            draw.rect(screen, BLACK, (300, 275, 400, 150))
            win = fontWinLose.render("YOU WIN.", 1, WHITE)
            screen.blit(win, (335, 305, 400, 150))
            display.update()
            time.wait(250)
            win = fontWinLose.render("YOU WIN.", 1, BLUE)
            screen.blit(win, (335, 305, 400, 150))      
            draw.rect(screen, BLUE, (300, 275, 400, 150), 5)
            display.update()
            time.wait(250)         
        return(STATE_GAME3_WIN)
    elif AIScore == 2:
        playSound = True
        #losing screen
        for l in range(0, 6):
            draw.rect(screen, BLACK, (300, 275, 400, 150))
            lose = fontWinLose.render("YOU LOSE.", 1, WHITE)
            screen.blit(lose, (325, 305, 400, 150))
            display.update()
            time.wait(250)
            lose = fontWinLose.render("YOU LOSE.", 1, RED)
            screen.blit(lose, (325, 305, 400, 150))      
            draw.rect(screen, RED, (300, 275, 400, 150), 5)
            display.update()
            time.wait(250)                        
        return(STATE_GAME3_LOSE)    
    
    #check which mouse is hovering over
    choiceCollision = mouseRect.collidelist(listRect)
    
    if choiceCollision != -1:
        if button == 1:
            #get user choice and ai's choice
            userChoice = RPSChoice[choiceCollision]
            AIChoice = getAIChoice()
            
            RPSCountdown.play()
            for h in range(3, 0, -1):
                screen.fill(WHITE)
                screen.blit(RPSBackground, (0, 0, 1000, 700))
                screen.blit(playerScoreText, (75, 80, 100, 100))
                screen.blit(AIScoreText, (600, 80, 100, 100))                
                screen.blit(roundNum, (400, 25, 200, 200))  
                screen.blit(TBDRPS, (90, 190))         #Player SIDE
                screen.blit(TBDRPS, (615, 190))         #AI SIDE
                
                text = fontRound.render(str(h), 1, WHITE)
                screen.blit(text, (480, 500))
                display.update()
                time.wait(1000)
            
            screen.blit(RPSBackground, (0, 0, 1000, 700))
            #display users choice
            if userChoice == 'Rock':
                screen.blit(transformedRock, (85, 200))
                text = fontRound.render('Rock', 1, BLUE)
                screen.blit(text, (85, 600))
            elif userChoice == 'Paper':
                screen.blit(transformedPaper, (85, 200))
                text = fontRound.render('Paper', 1, BLUE)
                screen.blit(text, (85, 600))                
            else:
                screen.blit(transformedScissor, (85, 200))
                text = fontRound.render('Scissor', 1, BLUE)
                screen.blit(text, (85, 600))                  
            
            if AIChoice == 'Rock':
                screen.blit(transformedRock, (615, 200))
                text = fontRound.render('Rock', 1, RED)
                screen.blit(text, (615, 600))                  
            elif AIChoice == 'Paper':
                screen.blit(transformedPaper, (615, 200))
                text = fontRound.render('Paper', 1, RED)
                screen.blit(text, (615, 600))                  
            else:
                screen.blit(transformedScissor, (615, 200)) 
                text = fontRound.render('Scissor', 1, RED)
                screen.blit(text, (615, 600))                  

            display.update()
            time.wait(500)    
            
            playerScore, AIScore = findWinner(userChoice, AIChoice)
            roundNumber += 1
        
            display.update()
            time.wait(1000)    
            
        for l in range (0, 3):
            draw.rect(screen, WHITE, listRect[l])
            text = fontRPS.render(RPSChoice[l], 1, BLACK)
            screen.blit(text, RPSChoice_pos[l])                      
        text = fontRPS.render(RPSChoice[choiceCollision], 1, BLUE)
        screen.blit(text, RPSChoice_pos[choiceCollision])
        draw.rect(screen, BLUE, listRect[choiceCollision], 4)
    
    else:
        for l in range (0, 3):
            draw.rect(screen, WHITE, listRect[l])
            text = fontRPS.render(RPSChoice[l], 1, BLACK)
            screen.blit(text, RPSChoice_pos[l])            
        
    return(STATE_PLAY_GAME3)
def getAIChoice():
    choices = ['Rock', 'Paper', 'Scissor']
    return random.choice(choices)    
def findWinner(x, y):
    global playerScore
    global AIScore    
    
    #draw if both are the same
    if x == y:
        scoreText = fontScoreText.render('DRAW', 1, WHITE)
        screen.blit(scoreText, (425, 550, 100, 100))
        return(playerScore, AIScore)
    
    elif (x == 'Rock' and y == 'Scissor') or (x == 'Paper' and y == 'Rock') or (x == 'Scissor' and y == 'Paper'):
        for w in range(0,2):
            scoreText = fontScoreText.render('+1', 1, BLUE)
            screen.blit(scoreText, (350, 650, 100, 100))
            display.update()
            time.wait(250)
            scoreText = fontScoreText.render('+1', 1, GREEN)
            screen.blit(scoreText, (350, 650, 100, 100))
            display.update() 
            time.wait(250)
            
        return(playerScore + 1, AIScore)
    else:
        for w in range(0,2):
            scoreText = fontScoreText.render('+1', 1, RED)
            screen.blit(scoreText, (850, 650, 100, 100))
            display.update()
            time.wait(250)
            scoreText = fontScoreText.render('+1', 1, GREEN)
            screen.blit(scoreText, (850, 650, 100, 100))
            display.update() 
            time.wait(250)
        return(playerScore, AIScore + 1)
def gameThreeWelcome():
    screen.fill(BLACK)
    
    #fade in the text
    for textFadeIn in range (0, 255, 20):
        text1 = fontWelcomeScreen.render("Welcome to", 1, (textFadeIn, textFadeIn, textFadeIn))	
        text2 = fontWelcomeScreen.render("Rock Paper Scissors " + user_name , 1, (textFadeIn, textFadeIn, textFadeIn))
        screen.blit(text1, (10,280,400,100))
        screen.blit(text2, (10,325,400,100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (240, -1, -20):
        text1 = fontWelcomeScreen.render("Welcome to", 1, (textFadeOut, textFadeOut, textFadeOut))
        text2 = fontWelcomeScreen.render("Rock Paper Scissors " + user_name, 1, (textFadeOut, textFadeOut, textFadeOut))
        screen.blit(text1, (10,280,400,100))
        screen.blit(text2, (10,325,400,100))
        display.update()
        time.wait(100)
    screen.fill(BLACK) 
    
    #fade in the text
    for textFadeIn in range (0, 255, 20):
        text1 = fontWelcomeScreen.render("You have one chance to " , 1, (textFadeIn, textFadeIn, textFadeIn))
        text2 = fontWelcomeScreen.render("win a best of 3.", 1, (textFadeIn, textFadeIn, textFadeIn))
        screen.blit(text1, (10,280,400,100))
        screen.blit(text2, (10, 325, 400, 100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (240, -1, -20):
        text1 = fontWelcomeScreen.render("You have one chance to " , 1, (textFadeOut, textFadeOut, textFadeOut))
        text2 = fontWelcomeScreen.render("win a best of 3.", 1, (textFadeOut, textFadeOut, textFadeOut))
        screen.blit(text1, (10,280,400,100))
        screen.blit(text2, (10, 325, 400, 100))
        display.update()
        time.wait(100)
    
    screen.fill(BLACK)
    return(STATE_PLAY_GAME3) #intro finished, enter game 3 state
def gameThreeWinScreen(mx, my, button):
    screen.fill(WHITE)
    
    #fade in the text
    for textFadeIn in range (240, -1, -20):
        text1 = fontWelcomeScreen.render("Congratulations" , 1, (textFadeIn, textFadeIn, textFadeIn))	
        text2 = fontWelcomeScreen.render("You have saved Earth." , 1, (textFadeIn, textFadeIn, textFadeIn))	
        screen.blit(text1, (200,280,400,100))
        screen.blit(text2, (200,350,400,100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (0, 255, 20):
        text1 = fontWelcomeScreen.render("Congratulations", 1, (textFadeOut, textFadeOut, textFadeOut))	
        text2 = fontWelcomeScreen.render("You have saved Earth." , 1, (textFadeOut, textFadeOut, textFadeOut))	
        screen.blit(text1, (200,280,400,100))
        screen.blit(text2, (200,350,400,100))
        display.update()
        time.wait(100)
    screen.fill(WHITE)   
    
    #fade in the text
    for textFadeIn in range (240, -1, -20):
        text = fontWelcomeScreen.render("For now...." , 1, (textFadeIn, textFadeIn, textFadeIn))	
        screen.blit(text, (350,300,400,100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (0, 255, 20):
        text = fontWelcomeScreen.render("For now....", 1, (textFadeOut, textFadeOut, textFadeOut))	
        screen.blit(text, (350,300,400,100))
        display.update()
        time.wait(100)
    screen.fill(WHITE)       
    
    
    return(STATE_CREDIT_SCREEN)
def gameThreeLoseScreen(mx, my, button):
    screen.fill(BLACK)
    
    #fade in the text
    for textFadeIn in range (0, 255, 20):
        text = fontWelcomeScreen.render("You failed." , 1, (textFadeIn, textFadeIn, textFadeIn))		
        screen.blit(text, (350,280,400,100))
        display.update()
        time.wait(100)
    #fade out the text 
    for textFadeOut in range (240, -1, -20):
        text = fontWelcomeScreen.render("You failed.", 1, (textFadeOut, textFadeOut, textFadeOut))	
        screen.blit(text, (350,280,400,100))
        display.update()
        time.wait(100)    
    screen.fill(BLACK)
    
    return(STATE_MAIN)
def creditScreen(mx, my, button):
    global offsetY 
    
    screen.fill(BLACK)
    
    #SKIP BUTTON
    skip = fontWelcomeScreenSmall.render('SKIP', 1, WHITE)
    skipRect = Rect(10, 25, 100, 60)
    screen.blit(skip, skipRect)
    #collision check
    if skipRect.collidepoint(mx, my):
        if button == 1:
            return(STATE_MAIN)
        else:
            skip = fontWelcomeScreenSmall.render('SKIP', 1, RED)
            screen.blit(skip, skipRect)            
    
    #list of text of credits to display
    listCredits = [
        'Game Developer: Ayaan',
        'Storyline Editor: Ayaan',
        'Programming Language: Python'
        ]
    
    lineBreak = 0       #break between each line
    
    creditsHeader = fontWelcomeScreenTitle.render('Credits', 1, WHITE)
    screen.blit(creditsHeader ,(375, 550 - offsetY, 100, 100))
    
    for cred in listCredits:
        screen.blit((fontWelcomeScreenSmall.render(cred, 1, WHITE)), (85, (700 + lineBreak) - offsetY, 100, 100)) 
        lineBreak += 60
        
    #THANK YOU FOR PLAYING!
    text = fontWelcomeScreenTitle.render('Thank you for Playing', 1, WHITE)
    screen.blit(text, (50, 1050 - offsetY, 100, 100))
    
    
    if 1050 - offsetY <= -200:
        return(STATE_MAIN)
    offsetY += 2
    return(STATE_CREDIT_SCREEN)
#---------------------------------------------------------------------

#version of game
version = 'V1.1 BETA'

running = True
myClock = time.Clock()
state = STATE_MAIN    #initialize state to main screen
mx, my = 0, 0
mouseRect = Rect(0, 0, 2, 2)

playSound = True
offsetY = 0
playAgain1 = True
playAgain2 = True
playAgain3 = True  
#---------------------------------------------------------------------
while running:
    button = 0      #reset button
    
    #Events Loop
    for e in event.get():
        if e.type == QUIT:
            running = False
            
       
        if e.type == MOUSEMOTION:
            mx, my = e.pos
            mouseRect = Rect(mx, my, 2, 2)
       
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos
            button = e.button
            mouseRect = Rect(mx, my, 2, 2)
            
        if e.type == KEYDOWN:
            if state == STATE_WELCOME:
                if e.key == K_BACKSPACE:
                    user_name = user_name[:-1]
                elif e.key == K_RETURN:
                    nameGiven = True
                else:
                    user_name += e.unicode
                       
    #MAIN STATE -------------------------------------------------------------------
    if state == STATE_MAIN:
        #menu music
        if playSound:
            menuMusic.play()
            playSound = False
        
        #re initialize every game state 
        playAgain1 = True
        playAgain2 = True
        playAgain3 = True        
        
        state = mainScreen(mx, my, button, backgroundX)
        backgroundX -= 1.5
        if backgroundX < -1*width:
            backgroundX = 0        
        display.update()
    
    #WELCOME SCREEN STATE -------------------------------------------------------------------
    elif state == STATE_WELCOME:
        screen.fill(BLACK)
        if nameGiven == False:
            #get users name
            text = fontWelcomeScreen.render("Please enter your name: " , 1, WHITE)	
            screen.blit(text, (160,215,200,100))    
            draw.rect(screen, WHITE, (185, 300, 600, 125))
            
            display_name = fontWelcomeScreen.render(user_name, 1, BLACK)
            screen.blit(display_name, (185, 300, 600, 125))
            display.update()
                
        
        if nameGiven == True:
            user_name = user_name.capitalize()
            welcomeScreen(mx, my, button, user_name)
            state = STATE_PLAY_SCREEN
        display.update()
        backgroundX = 0
    
    #PLAY SCREEN STATE -------------------------------------------------------------------
    elif state == STATE_PLAY_SCREEN:
        #enter the play screen
        state = playScreen(mx, my, button, backgroundX)  
        backgroundX -= 1.5
        if backgroundX < -1*width:
            backgroundX = 0         
        display.update()
    
    #GAME ONE STATE -------------------------------------------------------------------
    elif state == STATE_PLAY_GAME1:
        #cut off music 
        menuMusic.stop()
        #play music
        if playSound:
            gameOneMusic.play()
            playSound = False
        
        
        if playAgain1 == True:
            gameOneLives = 3
            gameOneWin = False
            gameOneLose = False
            playAgain1 = False
        
        state = gameOneScreen(mx, my, button)
        display.update()
    
    #GAME ONE WIN SCREEN -------------------------------------------------------------------
    elif state == STATE_GAME1_WIN:
        #cut off music
        gameOneMusic.stop()
        if playSound:
            menuMusic.play()
            playSound = False
        
        state = gameOneWinScreen(mx, my, button, backgroundX)
        backgroundX -= 1.5
        if backgroundX < -1*width:
            backgroundX = 0         
        display.update()
    
    #GAME ONE LOSE SCREEN -------------------------------------------------------------------
    elif state == STATE_GAME1_LOSE:
        #cut off music
        gameOneMusic.stop() 
        if playSound:
            menuMusic.play()
            playSound = False
        
        state = gameOneLoseScreen(mx, my, button, backgroundX)
        #re initialize game one variable as they failed
        gameOneLives = 3
        gameOneWin = False
        gameOneLose = False
        
        backgroundX -= 1.5
        if backgroundX < -1*width:
            backgroundX = 0           
        display.update()
    
    #GAME TWO STATE -------------------------------------------------------------------
    elif state == STATE_PLAY_GAME2:
        #cut off music
        menuMusic.fadeout(1500)
        if playSound:
            gameTwoMusic.play()
            playSound = False
        
        keys = key.get_pressed()  
        if keys[K_RIGHT]:
            if recyclingBinX <= 720:
                recyclingBinX += 8
        if keys[K_LEFT]:
            if recyclingBinX >= -30:
                recyclingBinX -= 8
            
        if playAgain2 == True:
            #re-initialzing every variable 
            numberOfRectangles = 4
            recyclingBinX = 500
            rectList = []
            garbageList = []
            score = 0
            arrowY = 185
            stageTwo = True
            stageThree = True
            #making the list of rectangles
            for rectCreate in range(0,numberOfRectangles):
                rectList.append(initRect())
            for garbageCreate in range (0, numberOfRectangles):
                garbageList.append(garbageInit())
            speedList = speed(numberOfRectangles)
            playAgain2 = False
    
        for r in range (0, numberOfRectangles):
            rectList[r][1] += speedList[r]
    
        for n in range(0, len(rectList)):
            if rectList[n][1] >= 600:
                gameTwoMusic.fadeout(1000)
                youLose.play()
                playSound = True
                #print flashing you lose in red and black
                for l in range(0, 6):
                    draw.rect(screen, BLACK, (300, 275, 400, 150))
                    lose = fontWinLose.render("YOU LOSE.", 1, WHITE)
                    screen.blit(lose, (325, 305, 400, 150))
                    display.update()
                    time.wait(250)
                    lose = fontWinLose.render("YOU LOSE.", 1, RED)
                    screen.blit(lose, (325, 305, 400, 150))      
                    draw.rect(screen, RED, (300, 275, 400, 150), 5)
                    display.update()
                    time.wait(250)                
                state = STATE_GAME2_LOSE
                
        gameTwoScreen(mx, my, button, rectList)
        display.update()    
        
        #game 2 event handling
        collisionCheck = recyclingBinRect.collidelist(rectList)
        if collisionCheck != -1:
            garbage.play()
            rectList[collisionCheck] = initRect()
            garbageList[collisionCheck] = garbageInit()
            score += 1
            arrowY += 12
            if score <= 6:
                speedList[collisionCheck] = random.uniform(0.5, 1.2)
            elif score <= 15 and score >= 7:
                speedList[collisionCheck] = (random.uniform(1.8, 2.5))
                if stageTwo == True:
                    stage.play()
                    for s2 in range (0,6):
                        stageTwoText = fontStage.render("Stage II", 1, BLACK)
                        screen.blit(stageTwoText, (275, 325, 100, 100))
                        display.update()
                        time.wait(250)
                        stageTwoText = fontStage.render("Stage II", 1, RED)
                        screen.blit(stageTwoText, (275, 325, 100, 100))
                        display.update()
                        time.wait(250)
                        
                    stageTwo = False
            elif score <= 26 and score >= 16:
                speedList[collisionCheck] = (random.uniform(2.8, 3.5))  
                if stageThree == True:
                    stage.play()
                    for s3 in range(0, 6):
                        stageThreeText = fontStage.render("Stage III", 1, RED)
                        screen.blit(stageThreeText, (275, 325, 100, 100))
                        display.update()
                        time.wait(250)
                        stageThreeText = fontStage.render("Stage III", 1, BLACK)
                        screen.blit(stageThreeText, (275, 325, 100, 100))
                        display.update()
                        time.wait(250)                        
                        
                    stageThree = False
        
        elif score >= 25:
            gameTwoMusic.fadeout(1000)
            youWin.play()
            playSound = True
            #print flashing you win in green and black
            for w in range(0, 6):
                draw.rect(screen, BLACK, (300, 275, 400, 150))
                win = fontWinLose.render("YOU WIN.", 1, WHITE)
                screen.blit(win, (335, 305, 400, 150))
                display.update()
                time.wait(250)
                win = fontWinLose.render("YOU WIN.", 1, GREEN)
                screen.blit(win, (335, 305, 400, 150))      
                draw.rect(screen, GREEN, (300, 275, 400, 150), 5)
                display.update()
                time.wait(250)  
                state = STATE_GAME2_WIN
        elif score <= 15 and score >= 7:
            speedList = speed(numberOfRectangles)
        elif score <= 26 and score >= 16:
            speedList = speed(numberOfRectangles)
    #GAME TWO WIN SCREEN -------------------------------------------------------------------
    elif state == STATE_GAME2_WIN:
        #play music
        if playSound:
            menuMusic.play()
            playSound = False
        
        state = gameTwoWinScreen(mx, my, button, backgroundX)
        backgroundX -= 1.5
        if backgroundX < -1*width:
            backgroundX = 0         
        display.update()
        
    #GAME TWO LOSE SCREEN -------------------------------------------------------------------
    elif state == STATE_GAME2_LOSE:
        #play music
        if playSound:
            menuMusic.play()
            playSound = False        
        
        state = gameTwoLoseScreen(mx, my, button, backgroundX)
        backgroundX -= 1.5
        if backgroundX < -1*width:
            backgroundX = 0         
        display.update()
    
    #GAME THREE WELCOME STATE -------------------------------------------------------------------
    elif state == STATE_GAME3_WELCOME:
        state = gameThreeWelcome()
        display.update()
     
    #GAME THREE STATE -------------------------------------------------------------------
    elif state == STATE_PLAY_GAME3:
        menuMusic.fadeout(1000)
        
        if playAgain3 == True:
            roundNumber = 1
            playerScore = 0
            AIScore = 0
            offsetY = 0
            playAgain3 = False
        
        state = gameThreeScreen(mx, my, button, mouseRect)
        display.update()
    
    #GAME THREE WIN STATE -------------------------------------------------------------------
    elif state == STATE_GAME3_WIN:
        if playSound:
            youWin.play()
        state = gameThreeWinScreen(mx, my, button)
        display.update() 
        
    #GAME THREE LOSE STATE -------------------------------------------------------------------
    elif state == STATE_GAME3_LOSE:
        if playSound:
            youLose.play()
        state = gameThreeLoseScreen(mx, my, button)
        display.update()
        
    #CREDIT SCREEN STATE -------------------------------------------------------------------
    elif state == STATE_CREDIT_SCREEN:
        state = creditScreen(mx, my, button)
        display.update()
    
    #INSTRUCTIONS / HELP STATE -------------------------------------------------------------------
    elif state == STATE_INSTRUCTIONS:
        state = instructionScreen(mx, my, button, backgroundX)   
        backgroundX -= 1.5
        if backgroundX < -1*width:
            backgroundX = 0           
        display.update()
    
    #QUIT STATE -------------------------------------------------------------------
    elif state == STATE_QUIT:
        running = False
        quit()
    
    myClock.tick(60)
quit()