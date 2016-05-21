import turtle

def drawSnake( rad , angle , len , neckrad ) :
    for i in range(len) :
        turtle.circle( rad , angle )
        turtle.circle( -rad ,angle )

    turtle.circle(rad , angle/2 )
    turtle.fa( rad )
    turtle.circle(neckrad+1 , 180 )
    turtle.fd( rad*2/3 )


def main( ) :
    s = type(4.6)
    print s

    turtle.setup( 900 , 700 , 100 , 100 )
    turtle.pensize( 30 )
    turtle.pencolor( "blue" )
    turtle.seth( -90 )
    drawSnake( 100 , 80 , 5 , 15 )
    while 1 :
        pass


main( )
