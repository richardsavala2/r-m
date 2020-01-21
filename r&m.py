from tkinter import *
import os
import turtle
import time
import random


def delete2():

    screen2.destroy()
    screen3.destroy()
    broh_select()


def delete3():

    screen4.destroy()


def delete4():

    screen5.destroy()


def delete5a():

    screen6.destroy()
    rick()


def delete5b():

    screen6.destroy()
    morty()


def delete5c():

    screen6.destroy()
    summer()


def delete6a():

    screen7.destroy()
    morty1()
    morty1()


def delete6b():

    screen7.destroy()
    morty2()


def delete12a():

    screen13.destroy()
    morty4()


def delete12b():

    screen13.destroy()
    morty5()


def delete12c():

    screen13.destroy()
    morty6()
    morty6()
    morty6()
    morty6()


def delete13a():

    screen14.destroy()
    morty9()


def delete13b():

    screen14.destroy()
    morty5()
    morty5()
    morty5()
    morty5()
    morty5()
    morty5()
    morty5()
    morty5()


def delete14a():

    screen15.destroy()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()


def delete14b():

    screen15.destroy()
    morty12()


def delete15a():

    screen16.destroy()
    morty9()


def delete15b():

    screen16.destroy()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()


def delete16a():

    screen17.destroy()
    morty13()


def delete16b():

    screen17.destroy()
    morty14()


def delete16c():

    screen17.destroy()
    morty15()


def delete17():

    screen18.destroy()
    broh_select()


def delete18():

    screen19.destroy()
    broh_select()


def delete19a():

    screen20.destroy()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()
    morty10()


def delete19b():

    screen20.destroy()
    broh_select()


def delete20a():

    screen21.destroy()
    morty16()


def delete20b():

    screen21.destroy()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()
    morty11()


def delete21a():

    screen22.destroy()
    morty17()


def delete21b():

    screen22.destroy()
    morty18()


def delete21c():

    screen22.destroy()
    morty19()


def delete22a():

    screen23.destroy()
    broh_select()


def delete22b():

    screen23.destroy()
    screen.destroy()


def delete27a():

    screen28.destroy()
    morty7()


def delete27b():

    screen28.destroy()
    morty5()
    morty5()
    morty5()
    morty5()


def delete27c():

    screen28.destroy()
    morty8()


def delete29():

    screen30.destroy()
    broh_select()


def delete30():

    screen31.destroy()
    broh_select()


def delete31a():

    screen32.destroy()
    morty21()


def delete31b():

    screen32.destroy()
    morty22()


def delete31c():

    screen32.destroy()
    morty23()


def delete32():

    screen33.destroy()
    broh_select()


def delete33():

    screen34.destroy()
    broh_select()


def delete34():

    screen35.destroy()
    broh_select()


def delete39():

    screen40.destroy()
    broh_select()


def delete40():

    screen41.destroy()
    broh_select()


def delete41():

    screen42.destroy()
    broh_select()


def delete42():

    screen43.destroy()
    broh_select()


def delete43():
    screen44.destroy()
    broh_select()


def rick():

    global screen11
    delay = 0.1
    score = 0
    high_score = 0

    screen11 = turtle.Screen()
    screen11.title("snake fight ?")
    screen11.bgcolor('gray1')
    screen11.tracer(0)

    head = turtle.Turtle()
    head.speed(0)
    head.shape('square')
    head.color('steelblue1')
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('gray9')
    food.penup()
    food.goto(0, 100)

    segments = []

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("score: 0  high score: 0  ", align='center', font=('Courier', 24, 'normal'))

    def go_up():
        if head.direction != 'down':
            head.direction = 'up'

    def go_down():
        if head.direction != 'up':
            head.direction = 'down'

    def go_left():
        if head.direction != 'right':
            head.direction = 'left'

    def go_right():
        if head.direction != "left":
            head.direction = 'right'

    def move():
        if head.direction == 'up':
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == 'down':
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == 'left':
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == 'right':
            x = head.xcor()
            head.setx(x + 20)

    screen11.listen()
    screen11.onkeypress(go_up, 'w')
    screen11.onkeypress(go_down, 's')
    screen11.onkeypress(go_left, 'a')
    screen11.onkeypress(go_right, 'd')

    while True:
        screen11.update()

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write('score: {}  high score: {}'.format(score, high_score), align='center',
                      font=('Courier', 24, 'normal'))

        if head.distance(food) < 20:

            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color('lawngreen')
            new_segment.penup()
            segments.append(new_segment)

            delay -= 0.001

            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write('score: {}  high score: {}'.format(score, high_score), align='center',
                      font=('Courier', 24, 'normal'))

        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = 'stop'

                for segment in segments:
                    segment.goto(1000, 1000)

                score = 0

                delay = 0.1

                pen.clear()
                pen.write('score: {}  high score: {}'.format(score, high_score), align='center',
                          font=('Courier', 24, 'normal'))

        time.sleep(delay)


def morty24():

    global screen42
    screen42 = Toplevel(screen)
    screen42.title('not this again')
    screen42.geometry('400x400')
    Label(screen42, text='game over', width='400', bg='deeppink').pack()
    Label(screen42, text='').pack()
    Button(screen42, text='new game', command=delete41).pack()
    Label(screen42, text='').pack()


def morty23():

    global screen34

    screen34 = Toplevel(screen)
    screen34.title('"siri: nearest mortyMart.."')
    screen34.geometry('600x300')
    Label(screen34, text="you used 'SPECIAL', it didn\'t work!", height='2', width='600', bg='slateblue2').pack()
    Label(screen34, text="space snake used Sss, it was v effective", height='2', width='600', bg='red').pack()
    Label(screen34, text='DEFENSE: Sss  SPEED: Sss  SPECIAL: Sss', height='2', width='600', bg='slateblue2').pack()
    Label(screen34, text='').pack()
    Button(screen34, text='new game', command=delete33).pack()
    Label(screen34, text='').pack()
    Label(screen34, text='morticia:  HEALTH: 000  ATTACK: 137  DEFENSE: 000  SPECIAL: 000', bg='deeppink').pack()
    Label(screen34, text='').pack()


def morty22():

    global screen44

    screen44 = Toplevel(screen)
    screen44.title('Oo shit! way to buss him up morticia!')
    screen44.geometry('600x300')
    Label(screen44, text="you used 'kick', it was v effective", height='2', width='600', bg='slateblue2').pack()
    Label(screen44, text="space snake fainted", height='2', width='600', bg='lawngreen').pack()
    Label(screen44, text='oOOoEEe mission success').pack()
    Label(screen44, text='').pack()
    Button(screen44, text='new game', command=delete43).pack()
    Label(screen44, text='').pack()


def morty21():

    global screen33

    screen33 = Toplevel(screen)
    screen33.title('"for fucks sake its a snake stop punching it!"')
    screen33.geometry('400x400')
    Label(screen33, text="space snake used Sss, it was v effective", height='2', width='600', bg='red').pack()
    Label(screen33, text='').pack()
    Label(screen33, text='game over broh', width='400', bg='deeppink').pack()
    Label(screen33, text='').pack()
    Button(screen33, text='new game', command=delete32).pack()
    Label(screen33, text='').pack()
    Label(screen33, text='morticia:  HEALTH: 000  ATTACK: 072  DEFENSE: 000  SPECIAL: 003', bg='deeppink').pack()
    Label(screen33, text='').pack()


def morty20():

    global screen43

    screen43 = Toplevel(screen)
    screen43.title('Oo shit! way to buss him up morticia!')
    screen43.geometry('600x300')
    Label(screen43, text="you used 'kick', it was v effective", height='2', width='600', bg='slateblue2').pack()
    Label(screen43, text="space snake fainted", height='2', width='600', bg='lawngreen').pack()
    Label(screen43, text='oOOoEEe mission success').pack()
    Label(screen43, text='').pack()
    Button(screen43, text='new game', command=delete42).pack()
    Label(screen43, text='').pack()
    Label(screen43, text='morticia:  HEALTH: 097  ATTACK: 072  DEFENSE: 063  SPECIAL: 003', bg='deeppink').pack()
    Label(screen43, text='').pack()


def morty19():

    global screen35

    screen35 = Toplevel(screen)
    screen35.title('"Oof beth is not going to be happy.."')
    screen35.geometry('600x300')
    Label(screen35, text="you used 'SPECIAL', it didn\'t work!", height='2', width='600', bg='slateblue2').pack()
    Label(screen35, text="space snake used Sss, it was v effective", height='2', width='600', bg='red').pack()
    Label(screen35, text='DEFENSE: Sss  SPEED: Sss  SPECIAL: Sss', height='2', width='600', bg='slateblue2').pack()
    Label(screen35, text='').pack()
    Button(screen35, text='new game', command=delete34).pack()
    Label(screen35, text='').pack()
    Label(screen35, text='morticia:  HEALTH: 000  ATTACK: 137  DEFENSE: 000  SPECIAL: 000', bg='deeppink').pack()
    Label(screen35, text='').pack()


def morty18():

    global screen31

    screen31 = Toplevel(screen)
    screen31.title('Oo shit! way to buss him up morticia!')
    screen31.geometry('600x300')
    Label(screen31, text="you used 'kick', it was v effective", height='2', width='600', bg='slateblue2').pack()
    Label(screen31, text="space snake fainted", height='2', width='600', bg='lawngreen').pack()
    Label(screen31, text='oOOoEEe mission success').pack()
    Label(screen31, text='').pack()
    Button(screen31, text='new game', command=delete30).pack()
    Label(screen31, text='').pack()
    Label(screen31, text='morticia:  HEALTH: 097  ATTACK: 000  DEFENSE: 000  SPECIAL: 003', bg='deeppink').pack()
    Label(screen31, text='').pack()


def morty17():

    global screen32

    screen32 = Toplevel(screen)
    screen32.title('"float like a butterfly, sting like a bee!"')
    screen32.geometry('600x300')
    Label(screen32, text="you used 'punch', it was v ineffective", height='2', width='600', bg='slateblue2').pack()
    Label(screen32, text="space snake used Sss, it was v effective", height='2', width='600', bg='red').pack()
    Label(screen32, text='DEFENSE: Sss  SPEED: Sss  SPECIAL: Sss', height='2', width='600', bg='slateblue2').pack()
    Label(screen32, text='space snake ', height='2', width='300', bg='slateblue2').pack()
    Button(screen32, text='punch', command=delete31a).pack()
    Label(screen32, text='').pack()
    Button(screen32, text='kick', command=delete31b).pack()
    Label(screen32, text='').pack()
    Button(screen32, text='"the wheels on the bus go round & round"', command=delete31c).pack()
    Label(screen32, text='').pack()
    Label(screen32, text='morticia:  HEALTH: 097  ATTACK: 107  DEFENSE: 063  SPECIAL: 003', bg='deeppink').pack()
    Label(screen32, text='').pack()


def morty16():

    global screen22

    screen22 = Toplevel(screen)
    screen22.title('"morticia! concentrate on turning into a car!"')
    screen22.geometry('600x300')
    Label(screen22, text='space snake: TYPE1/POISON  ATTACK: Sss', height='2', width='400', bg='slateblue2').pack()
    Label(screen22, text='DEFENSE: Sss  SPEED: Sss  SPECIAL: Sss', height='2', width='400', bg='slateblue2').pack()
    Label(screen22, text='').pack()
    Button(screen22, text='punch', command=delete21a).pack()
    Label(screen22, text='').pack()
    Button(screen22, text='kick', command=delete21b).pack()
    Label(screen22, text='').pack()
    Button(screen22, text='"the wheels on the bus go round & round"', command=delete21c).pack()
    Label(screen22, text='').pack()
    Label(screen22, text='morticia:  HEALTH: 97  ATTACK: 137  DEFENSE: 063  SPECIAL: 003', bg='deeppink').pack()


def morty15():

    global screen41

    screen41 = Toplevel(screen)
    screen41.title('"you had weeks to up your SPECIAL!"')
    screen41.geometry('600x300')
    Label(screen41, text='game over', width='400', bg='slateblue2').pack()
    Label(screen41, text='').pack()
    Button(screen41, text='new game', command=delete40).pack()
    Label(screen41, text='').pack()
    Label(screen41, text='morty:  HEALTH: 000  ATTACK: 063  DEFENSE: 000  SPECIAL: 000', width='600', bg='yellow').pack()
    Label(screen41, text='').pack()


def morty14():

    global screen40

    screen40 = Toplevel(screen)
    screen40.title('"jesuss chr.. lll..piIick up your leg morty!"')
    screen40.geometry('600x300')
    Label(screen40, text='you used: KICK, it was v ineffective', width='400', bg='slateblue2').pack()
    Label(screen40, text='game over').pack()
    Label(screen40, text='').pack()
    Button(screen40, text='new game', command=delete39).pack()
    Label(screen40, text='').pack()
    Label(screen40, text='morty:  HEALTH: 000  ATTACK: 033  DEFENSE: 000  SPECIAL: 001', width='600', bg='yellow').pack()
    Label(screen40, text='').pack()


def morty13():

    global screen19

    screen19 = Toplevel(screen)
    screen19.title('"Oo geez mor-morty stop blocking his punches w your face!"')
    screen19.geometry('600x300')
    Label(screen19, text='you used: PUNCH, it was v ineffective', width='400', bg='slateblue2').pack()
    Label(screen19, text='game over', width='400', bg='slateblue2').pack()
    Label(screen19, text='').pack()
    Button(screen19, text='new game', command=delete18).pack()
    Label(screen19, text='').pack()
    Label(screen19, text='morty:  HEALTH: 000  ATTACK: 43  DEFENSE: 000  SPECIAL: 001', width='600', bg='yellow').pack()
    Label(screen19, text='').pack()


def morty12():

    global screen21

    screen21 = Toplevel(screen)
    screen21.title('"morticia watch out for that space snake!"')
    screen21.geometry('400x400')
    Label(screen21, text='a space snake has appeared', bg='slateblue2').pack()
    Label(screen21, text='').pack()
    Button(screen21, text='fight', command=delete20a).pack()
    Label(screen21, text='').pack()
    Button(screen21, text='run', command=delete20b).pack()
    Label(screen21, text='').pack()


def morty11():

    global screen20

    screen20 = Toplevel(screen)
    screen20.title('"son of a bi-iitch!"')
    screen20.geometry('200x700')
    Label(screen20, text='game over', height='2', width='200').pack()
    Label(screen20, text='').pack()
    Label(screen20, text=':0', height='2', width='700', bg='deeppink').pack()
    Button(screen20, text='OooEee', command=delete19a).pack()
    Label(screen20, text='').pack()
    Button(screen20, text='new game', command=delete19b).pack()
    Label(screen20, text='').pack()


def morty10():

    global screen30

    screen30 = Toplevel(screen)
    screen30.title('not this again')
    screen30.geometry('150x1000')
    Label(screen30, text='game over', width='1000', bg='deeppink').pack()
    Label(screen30, text='').pack()
    Button(screen30, text='new game', command=delete29).pack()
    Label(screen30, text='').pack()


def morty9():

    global screen23

    screen23 = Toplevel(screen)
    screen23.title('"wubba lubba dub dub!"')
    screen23.geometry('300x300')
    Label(screen23, text='mission success', width='300', bg='lawngreen').pack()
    Label(screen23, text='"time for blitz \'n chips!"', width='300', bg='lawngreen').pack()
    Label(screen23, text='').pack()
    Button(screen23, text='new game', command=delete22a).pack()
    Label(screen23, text='').pack()
    Button(screen23, text='logout', command=delete22b).pack()
    Label(screen23, text='').pack()


def morty8():

    global screen18

    screen18 = Toplevel(screen)
    screen18.title('"morty..?"')
    screen18.geometry('600x300')
    Label(screen18, text="skyler kicked morty/'s face off his head", height='2', width='400', bg='slateblue2').pack()
    Label(screen18, text='').pack()
    Label(screen18, text='game over :0').pack()
    Label(screen18, text='').pack()
    Button(screen18, text='new game', command=delete17).pack()
    Label(screen18, text='').pack()


def morty7():

    global screen17

    screen17 = Toplevel(screen)
    screen17.title('your morty is very weak, hes actually a kirkland morty')
    screen17.geometry('600x300')
    Label(screen17, text='skyler: TYPE1/PSYCHIC  ATTACK: 569', height='2', width='600', bg='slateblue2').pack()
    Label(screen17, text='DEFENSE: 234  SPEED: 299  SPECIAL: 420', height='2', width='600',bg='slateblue2').pack()
    Label(screen17, text='').pack()
    Button(screen17, text='punch', command=delete16a).pack()
    Label(screen17, text='').pack()
    Button(screen17, text='kick', command=delete16b).pack()
    Label(screen17, text='').pack()
    Button(screen17, text='transform into a car and drive away', command=delete16c).pack()
    Label(screen17, text='').pack()
    Label(screen17, text='morty:  HEALTH: 099  ATTACK: 063  DEFENSE: 137  SPECIAL: 001', width='600', bg='yellow').pack()
    Label(screen17, text='').pack()


def morty6():

    global screen15

    screen15 = Toplevel(screen)
    screen15.title('"a morticia! you\'re the last thing i need!"')
    screen15.geometry('1000x300')
    Label(screen15, text='get in the fucking car! im taking you home', height='2', width='400', bg='deeppink').pack()
    Label(screen15, text='').pack()
    Button(screen15, text='yes', command=delete14a).pack()
    Label(screen15, text='').pack()
    Button(screen15, text='no', command=delete14b).pack()
    Label(screen15, text='').pack()


def morty5():

    global screen16

    screen16 = Toplevel(screen)
    screen16.title('"god damn it morty you just ripped our time again!"')
    screen16.geometry('400x1000')
    Label(screen16, text='get back in the fucking car!', height='2', width='400', bg='slateblue2').pack()
    Label(screen16, text='').pack()
    Button(screen16, text='yes', command=delete15a).pack()
    Label(screen16, text='').pack()
    Button(screen16, text='no', command=delete15b).pack()
    Label(screen16, text='').pack()


def morty4():

    global screen14

    screen14 = Toplevel(screen)
    screen14.title('"good save morty!"')
    screen14.geometry('400x400')
    Label(screen14, text='"now get back in the fucking car!"', height='2', width='400', bg='slateblue2').pack()
    Label(screen14, text='').pack()
    Button(screen14, text='yes', command=delete13a).pack()
    Label(screen14, text='').pack()
    Button(screen14, text='no', command=delete13b).pack()
    Label(screen14, text='').pack()


def morty2():

    global screen28

    screen28 = Toplevel(screen)
    screen28.title('"i\'m changing the tire, get back in the car morty!"')
    screen28.geometry('400x400')
    Label(screen28, text='a wild skyler has appeared', height='2', width='400', bg='slateblue2').pack()
    Label(screen28, text='').pack()
    Button(screen28, text='fight', command=delete27a).pack()
    Label(screen28, text='').pack()
    Button(screen28, text='get back in the car', command=delete27b).pack()
    Label(screen28, text='').pack()
    Button(screen28, text='cry for rick', command=delete27c).pack()
    Label(screen28, text='').pack()


def morty1():

    global screen13

    screen13 = Toplevel(screen)
    screen13.title('/"you indecisive piece of shit!"')
    screen13.geometry('400x400')
    Label(screen13, text='"our time is all fuUUGHKd up!"', height='2', width='400', bg='slateblue2').pack()
    Label(screen13, text='').pack()
    Button(screen13, text='yes', command=delete12a).pack()
    Label(screen13, text='').pack()
    Button(screen13, text='no', command=delete12b).pack()
    Label(screen13, text='').pack()
    Button(screen13, text='wh-what ?', command=delete12c).pack()
    Label(screen13, text='').pack()


def morty():

    global screen7

    screen7 = Toplevel(screen)
    screen7.title('"space is a dangerous place broh"')
    screen7.geometry("400x400")
    Label(screen7, text='"Stay in the fucking car!"', width='400', height='2', bg='slateblue2').pack()
    Label(screen7, text='').pack()
    Button(screen7, text='yes', height='2', width='30', command=delete6a).pack()
    Label(screen7, text='').pack()
    Button(screen7, text='no', height='2', width='30', command=delete6b).pack()
    Label(screen7, text='').pack()


def summer():

    global screen10

    screen10 = turtle.Screen()
    screen10.title('"shitty ship.. SUM-summer take the OooEeheel (j)"')
    screen10.bgcolor('black')
    screen10.setup(width=500, height=800)
    screen10.tracer(0)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color('white')
    pen.goto(0, 250)
    pen.write('0', move=False, align='left', font=('Arial', 32, 'normal'))

    player = turtle.Turtle()
    player.speed(0)
    player.penup()
    player.color('grey')
    player.shape('triangle')
    player.goto(-200, 0)
    player.dx = 0
    player.dy = 1

    pipe1_top = turtle.Turtle()
    pipe1_top.speed(0)
    pipe1_top.penup()
    pipe1_top.color('lawngreen')
    pipe1_top.shape('square')
    pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
    pipe1_top.goto(300, 250)
    pipe1_top.dx = -2
    pipe1_top.dy = 0
    pipe1_top.value = 1

    pipe1_bottom = turtle.Turtle()
    pipe1_bottom.speed(0)
    pipe1_bottom.penup()
    pipe1_bottom.color('lawngreen')
    pipe1_bottom.shape('square')
    pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
    pipe1_bottom.goto(300, -250)
    pipe1_bottom.dx = -2
    pipe1_bottom.dy = 0

    pipe2_top = turtle.Turtle()
    pipe2_top.speed(0)
    pipe2_top.penup()
    pipe2_top.color('lawngreen')
    pipe2_top.shape('square')
    pipe2_top.shapesize(stretch_wid=25, stretch_len=3, outline=None)
    pipe2_top.goto(600, 100)
    pipe2_top.dx = -2
    pipe2_top.dy = 0
    pipe2_top.value = 1

    pipe2_bottom = turtle.Turtle()
    pipe2_bottom.speed(0)
    pipe2_bottom.penup()
    pipe2_bottom.color('lawngreen')
    pipe2_bottom.shape('square')
    pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
    pipe2_bottom.goto(600, -450)
    pipe2_bottom.dx = -2
    pipe2_bottom.dy = 0

    gravity = -0.4

    # define function / method
    def go_up():
        player.dy += 12

        if player.dy > 12:
            player.dy = 12

    # initialize game variables
    player.score = 0
    print('score: {}'.format(player.score))

    # keyboard binding
    screen10.listen()
    screen10.onkeypress(go_up, 'j')

    # main game loop
    while True:
        # pause
        time.sleep(0.02)

        # update screen
        screen10.update()

        # add gravity
        player.dy += gravity

        # move ship
        y = player.ycor()
        y += player.dy
        player.sety(y)

        # bottom border
        if player.ycor() < -390:
            player.dy = 0
            player.sety(-390)

        # move pipe1
        x = pipe1_top.xcor()
        x += pipe1_top.dx
        pipe1_top.setx(x)

        x = pipe1_bottom.xcor()
        x += pipe1_bottom.dx
        pipe1_bottom.setx(x)

        # return pipes to start
        if pipe1_top.xcor() < -350:
            pipe1_top.setx(350)
            pipe1_bottom.setx(350)
            pipe1_top.value = 1

        # move pipe 2
        x = pipe2_top.xcor()
        x += pipe2_top.dx
        pipe2_top.setx(x)

        x = pipe2_bottom.xcor()
        x += pipe2_bottom.dx
        pipe2_bottom.setx(x)

        # return pipes to start
        if pipe2_top.xcor() < -350:
            pipe2_top.setx(350)
            pipe2_bottom.setx(350)
            pipe2_top.value = 1

        # check for collisions with pipes
        # pipe1
        if (player.xcor() + 10 > pipe1_top.xcor() - 30) and (player.xcor() - 10 < pipe1_top.xcor() + 30):
            if (player.ycor() + 10 > pipe1_top.ycor() - 180) or (player.ycor() - 10 < pipe1_bottom.ycor() + 180):
                print('game over')
                screen10.update()
                time.sleep(3)
                # reset score
                player.score = 0
                # reset pipes
                pipe1_top.setx(300)
                pipe1_bottom.setx(300)
                pipe1_top.setx(600)
                pipe1_bottom.setx(600)
                # reset ship
                player.goto(-200, 0)
                player.dy = 0

        # check score
        if pipe1_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe1_top.value
            pipe1_top.value = 0
            pen.clear()
            pen.write(player.score, move=False, align='left', font=('Arial', 32, 'normal'))

        # check for collisions with pipes
        # pipe2
        if (player.xcor() + 10 > pipe2_top.xcor() - 30) and (player.xcor() - 10 < pipe2_top.xcor() + 30):
            if (player.ycor() + 10 > pipe2_top.ycor() - 200) or (player.ycor() - 10 < pipe2_bottom.ycor() + 200):
                print('game over')
                screen10.update()
                time.sleep(3)
                # reset score
                player.score = 0
                # reset pipes
                pipe2_top.setx(300)
                pipe2_bottom.setx(300)
                pipe2_top.setx(600)
                pipe2_bottom.setx(600)
                # reset ship
                player.goto(-200, 0)
                player.dy = 0

        # check score
        if pipe2_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe2_top.value
            pipe2_top.value = 0
            pen.clear()
            pen.write(player.score, move=False, align='left', font=('Arial', 32, 'normal'))


def broh_select():

    global screen6

    screen6 = Toplevel(screen)
    screen6.title('character select')
    screen6.geometry('300x300')
    Label(screen6, text='select character', height='2', width='400',  bg='lawngreen', font=('Calibri', '18')).pack()
    Label(screen6, text='').pack()
    Button(screen6, text="summer", height='2', width='10', command=delete5c).pack()
    Label(screen6, text='').pack()
    Button(screen6, text="rick", height='2', width='10', command=delete5a).pack()
    Label(screen6, text='').pack()
    Button(screen6, text="morty", height='2', width='10', command=delete5b).pack()
    Label(screen6, text='').pack()


def login_success():

    global screen3

    screen3 = Toplevel(screen)
    screen3.title('Success')
    screen3.geometry('150x100')
    Label(screen3, text='oOOoEEe Login Success').pack()
    Button(screen3, text='OK', command=delete2).pack()


def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen, bg='purple')
    screen4.title('Success')
    screen4.geometry('150x100')
    Label(screen4, text='incorrect broh!').pack()
    Button(screen4, text='OK', command=delete3).pack()


def user_not_found():

    global screen5

    screen5 = Toplevel(screen)
    screen5.title('Success')
    screen5.geometry('150x100')
    Label(screen5, text='broh not found!', bg='purple', font='calibri').pack()
    Button(screen5, text='OK', command=delete4).pack()


def register_user():

    print('working...')

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, 'w')
    file.write(username_info + '\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text='Registration Success', fg='green', font=('Calibri', '11')).pack()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()

    else:
        user_not_found()


def register():

    global screen1
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    screen1 = Toplevel(screen, bg='lawngreen')
    screen1.title('Register')
    screen1.geometry('300x250')
    Label(screen1, text='Please enter details below').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='Username * ').pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text='Password * ').pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text='').pack()
    Button(screen1, text='Register', width=10, height=1, command=register_user).pack()


def login():

    global screen2

    screen2 = Toplevel(screen)
    screen2.title('Login')
    screen2.geometry('300x250')
    Label(screen2, text='Please enter details below', bg='lawngreen').pack()
    Label(screen2, text='').pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text='Username * ').pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text='').pack()
    Label(screen2, text='Password * ').pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text='').pack()
    Button(screen2, text='Login', width=10, height=1, command=login_verify).pack()


def main_screen():

    global screen

    screen = Tk()
    screen.geometry("300x250")
    screen.title('Rick & Morty RPG')
    Label(screen, text='Rick & Morty RPG', bg='lawngreen', width='300', height='2', font=('Calibri', '13')).pack()
    Label(screen, text='').pack()
    Button(screen, text='Login', height='2', width='30', command=login).pack()
    Label(screen, text='').pack()
    Button(screen, text='Register', height="2", width='30', command=register).pack()

    screen.mainloop()


main_screen()
