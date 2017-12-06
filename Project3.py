# Project3CS177
# Kairui Deng
# CS177 Project3
# This program creates a program that would run the animation of the game Clay Target
# It will create a main function, which will give you a control panel for the user to create a new game
# This program will also create different animations based on the different choices offered to the users
from random import randint
from graphics import*
from time import*
import math


def f1():
    win = GraphWin("Control Panel",400,400)
    gamepanel = Rectangle(Point(10,30),Point(390,180))
    gamepanel.draw(win)
    targetpanel = Rectangle(Point(10,210),Point(390,360))
    targetpanel.draw(win)
    gamepanelmsg = Text(Point(200,15),"GAME PANEL")
    targetpanelmsg = Text(Point(200,195),"TARGET PANEL")
    gamepanelmsg.draw(win)
    targetpanelmsg.draw(win)
    
    newgame = Rectangle(Point(20,40),Point(120,90))
    newgame.setFill("grey")
    newgamemsg = Text(Point(70,65),"NEW GAME")
    newgame.draw(win)
    newgamemsg.draw(win)
    
    highscore = Rectangle(Point(150,40),Point(250,90))
    highscore.setFill("blue")
    highscoremsg = Text(Point(200,65),"HIGH SCORE")
    highscore.draw(win)
    highscoremsg.draw(win)
    
    quitit = Rectangle(Point(280,40),Point(380,90))
    quitit.setFill("red")
    quititmsg = Text(Point(330,65),"QUIT")
    quitit.draw(win)
    quititmsg.draw(win)
    
    player = Entry(Point(70,145),8)
    playerbox = Rectangle(Point(20,120),Point(120,170))
    playerbox.draw(win)
    playermsg = Text(Point(70,107),"Player")
    player.draw(win)
    playermsg.draw(win)
    
    roundbox = Rectangle(Point(170,120),Point(230,170))
    roundbox.draw(win)
    roundmsg = Text(Point(200,107),"Round")
    roundmsg.draw(win)
    roundnum = Text(Point(200,145),"0")
    roundnum.draw(win)
    
    scorebox = Rectangle(Point(300,120),Point(360,170))
    scorebox.draw(win)
    scoremsg = Text(Point(330,107),"Score")
    scoremsg.draw(win)
    scorenumber = Text(Point(330,145),"0")
    scorenumber.draw(win)

    anglebox = Rectangle(Point(40,250),Point(100,300))
    anglebox.draw(win)
    angle = Entry(Point(70,275),5)
    angle.setText("45")
    angle.draw(win)
    anglemsg = Text(Point(70,230),"Angle")
    anglemsg.draw(win)
    angleup = Circle(Point(130,260),10)
    angleup.setFill("light grey")
    angleup.draw(win)
    angleuparrow = Line(Point(130,250),Point(130,270))
    angleuparrow.setArrow("first")
    angleuparrow.draw(win)
    angledown = Circle(Point(130,290),10)
    angledown.setFill("light grey")
    angledown.draw(win)
    angledownarrow = Line(Point(130,280),Point(130,300))
    angledownarrow.setArrow("last")
    angledownarrow.draw(win)
    
    
    powerbox = Rectangle(Point(170,250),Point(230,300))
    powerbox.draw(win)
    power = Entry(Point(200,275),5)
    power.setText("10")
    power.draw(win)
    powermsg = Text(Point(200,230),"Power")
    powermsg.draw(win)
    powerup = Circle(Point(260,260),10)
    powerup.setFill("light grey")
    powerup.draw(win)
    poweruparrow = Line(Point(260,250),Point(260,270))
    poweruparrow.setArrow("first")
    poweruparrow.draw(win)
    powerdown = Circle(Point(260,290),10)
    powerdown.setFill("light grey")
    powerdown.draw(win)
    powerdownarrow = Line(Point(260,280),Point(260,300))
    powerdownarrow.setArrow("last")
    powerdownarrow.draw(win)
    
    gravitybox = Rectangle(Point(300,250),Point(360,300))
    gravitybox.draw(win)
    gravity = Entry(Point(330,275),5)
    gravity.setText("5")
    gravity.draw(win)
    gravitymsg = Text(Point(330,230),"Gravity")
    gravitymsg.draw(win)
    gravityup = Circle(Point(380,260),10)
    gravityup.setFill("light grey")
    gravityup.draw(win)
    gravityuparrow = Line(Point(380,250),Point(380,270))
    gravityuparrow.setArrow("first")
    gravityuparrow.draw(win)
    gravitydown = Circle(Point(380,290),10)
    gravitydown.setFill("light grey")
    gravitydown.draw(win)
    gravitydownarrow = Line(Point(380,280),Point(380,300))
    gravitydownarrow.setArrow("last")
    gravitydownarrow.draw(win)
    
    pullbox = Rectangle(Point(135,310),Point(265,350))
    pullbox.setFill("pink")
    pullmsg = Text(Point(200,330),"PULL")
    pullmsg.setSize(12)
    pullbox.draw(win)
    pullmsg.draw(win)

    return win,newgame,player,angle,power,gravity,pullbox,gravityup,gravitydown,powerdown,powerup,angledown,angleup,roundnum,scorenumber

def main():
    gamewindow = game()
    win,newgame,playername,angle,power,gravity,pull,gravityup,gravitydown,powerdown,powerup,angledown,angleup,roundnum,scorenumber = f1()
    x = 0
    newround = 0
    newscore = 0
    try:
        filename = open("top_scores.txt","r")
        filename.close()
    except:
        filename = open("top_scores.txt","w")
        filename.write("Top 10 scores")
        filename.write("==============")
        filename.write("Big Mac /t 5")
        filename.close() 
    while x < 10000000:
        x += 1
        clickpoint = win.getMouse()
        player = playername.getText()
        if clickpoint:
            clickx = clickpoint.getX()
            clicky = clickpoint.getY()

            if 370 < clickx <390 and 250 < clicky < 270:
                gravityup.setFill("red")
                gravitydown.setFill("light grey")
                g = gravity.getText()
                gravity.setText(int(g)+1)
                if int(g) > 24:
                    gravity.setText("25")                    
            if 370 < clickx < 390 and 280 < clicky < 300:
                gravitydown.setFill("red")
                gravityup.setFill("light grey")
                g = gravity.getText()
                gravity.setText(int(g)-1)
                if int(g) < 4:
                    gravity.setText("3")

            if 250 < clickx < 270 and 250 < clicky < 270:
                powerup.setFill("red")
                powerdown.setFill("light grey")
                p = power.getText()
                power.setText(int(p)+1)
                if int(p) > 49:
                    power.setText("50")
            if 250 < clickx < 270 and 280 < clicky < 300:
                powerdown.setFill("red")
                powerup.setFill("light grey")
                p = power.getText()
                power.setText(int(p)-1)
                if int(p) < 6:
                    power.setText("5")

            if 120 < clickx < 140 and 250 < clicky < 270:
                angleup.setFill("red")
                angledown.setFill("light grey")
                a = angle.getText()
                angle.setText(int(a)+1)
                if int(a) > 59:
                    angle.setText("60")
            if 120 < clickx < 140 and 280 < clicky < 300:
                angledown.setFill("red")
                angleup.setFill("light grey")
                a = angle.getText()
                angle.setText(int(a)-1)
                if int(a) < 31:
                    angle.setText("30")
                    
            if 20 < clickx < 120 and 40 < clicky < 90 and len(player) > 0:
                roundnum.setText("0")
                scorenumber.setText("0")
                gravity.setText("5")
                power.setText("10")
                angle.setText("45")
                angleup.setFill("light grey")
                angledown.setFill("light grey")
                powerup.setFill("light grey")
                powerdown.setFill("light grey")
                gravityup.setFill("light grey")
                gravitydown.setFill("light grey")
                newround = 0
                newscore = 0


            if 280 < clickx < 380 and 40 < clicky < 90 :
                win.close()
                gamewindow.close()

            if 135 < clickx < 265 and 310 < clicky < 350:
                newround += 1               
                if len(player) > 0 and 3 <= int(gravity.getText()) <= 25 and 5 <= int(power.getText()) <= 50 and 30 <= int(angle.getText()) <= 60:
                    pull.setFill("yellow")
                    newgame.setFill("grey")
                    sleep(2)
                    newerscore = animate(angle.getText(),power.getText(),gravity.getText(),gamewindow)
                    sleep(0.1)
                    newgame.setFill("green")
                    pull.setFill("pink")
                    newscore += newerscore
                    scorenumber.setText(newscore)
                    roundnum.setText(newround)
                if newround == 5:
                    finalscore = newerscore
                if newround > 5:
                    roundnum.setText("5")
                    scorenumber.setText(finalscore)

        if len(player) > 0:
            newgame.setFill("green")

        if power.getText() != "" and angle.getText() != "" and gravity.getText() != "":
            p = int(power.getText())
            g = int(gravity.getText())
            a = int(angle.getText())
            newround = 0
            newscore = 0
            if p > 49:
                power.setText("50")
            if p < 6:
                power.setText("5")
            if g > 24:
                gravity.setText("25")
            if g < 4:
                gravity.setText("3")
            if a > 59:
                angle.setText("60")
            if a < 31:
                angle.setText("30")
        

        

def game():
    win = GraphWin("Game On",600,600)
    sky = Rectangle(Point(0,0),Point(600,450))
    sky.setFill("light blue")
    ground = Rectangle(Point(0,450),Point(600,600))
    ground.setFill("light green")
    ground.draw(win)
    sky.draw(win)
    return win

def animate(angle,power,gravity,win):
    yleft = randint(350,450)
    yright = randint(350,450)
    circleleft = Circle(Point(0,yleft),8)
    circleright = Circle(Point(600,yright),8)
    circleleft.setFill("dark grey")
    circleright.setFill("dark grey")
    circleleft.draw(win)
    circleright.draw(win)
    dx = int(power)*(math.cos(int(angle)))
    dy = int(power)*(math.sin(int(angle)))
    i = True
    score = 0
    r = 0
    while i == True:
        centerpointleft = circleleft.getCenter()
        centerpointleftx = centerpointleft.getX()
        centerpointlefty = centerpointleft.getY()
        centerpointright = circleright.getCenter()
        centerpointrightx = centerpointright.getX()
        centerpointrighty = centerpointright.getY()
        if r >= 2:
            print("here")
            i = False
        if centerpointleftx > 596:
            circleleft.undraw()
            if centerpointrightx < 4:
                circleright.undraw()
                i = False
            if centerpointrighty > 450:
                circleright.undraw()
                i = False
        if centerpointlefty > 450:
            circleleft.undraw()
            if centerpointrightx < 4:
                circleright.undraw()
                i = False
            if centerpointrighty > 450:
                circleright.undraw()
                i = False
        if centerpointrightx < 4:
            circleright.undraw()
            if centerpointleftx > 596:
                circleleft.undraw()
                i = False
            if centerpointlefty > 450:
                circleleft.undraw()
                i = False
        if centerpointrighty > 450:
            circleright.undraw()
            if centerpointleftx > 596:
                circleleft.undraw()
                i = False
            if centerpointlefty > 450:
                circleleft.undraw()
                i = False
        else:
            circleleft.move(dx,-dy+(0.5*(i**2)*int(gravity)/500))
            circleright.move(-dx,-dy+(0.5*(i**2)*int(gravity)/500))
            clickpoint = win.checkMouse()
            if clickpoint:
                clickx = clickpoint.getX()
                clicky = clickpoint.getY()
                xright = clickx - centerpointrightx
                yright = clicky - centerpointrighty
                xleft = clickx - centerpointleftx
                yleft = clicky - centerpointlefty
                if -10 < xright < 10 and -10 < yright < 10:
                    circleright.undraw()
                    score += round(((int(gravity)+int(power))/10),2)
                    r += 1
                if -10 < xleft < 10 and -10 < yleft < 10:
                    circleleft.undraw()
                    score += round(((int(gravity)+int(power))/10),2)
                    r += 1
                
        sleep(0.1)
    
    return score
    
    




    
            
        

        
    
    

    
    
    
    
    


    
    

main()
    
    
    
