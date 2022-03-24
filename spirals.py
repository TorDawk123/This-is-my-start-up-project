#torian dawkins
#spirograph

#import  the turle library for
#drawing the requried curve
import turtle as tt

tt.bgcolor("black")
tt.pensize(2)
tt.speed(10)

#iterate and colors
for i in range(6):

    #choose my color combinations
    for color in ("green","blue","white","maroon","yellow","gray"):
        tt.color(color)

        #draw the spiral circle size
        tt.circle(100)

        #move the markings ot the left to draw another circle
        tt.left(10)

    #hide the cursor that draws the circle
    tt.hideturtle()
    
