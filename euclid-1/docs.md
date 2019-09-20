euclid Functions
createPage
createPage(size, color, tracer)

Creates a  blank page on which pens will leave their marks. size is a two member tuple; it's default value is (640, 480). color is a RGB tuple; for instance (255, 255, 255) sets the screen to white. tracer is an integer - 0 or positive - that controls animation speed. If for instance the value of tracer is 3, only every third change made to the page will be rendered to the screen. This increases animation speed. (I borrow the name from Python's turtle module. It's clever. A tracer round is typically every fifth round discharged.)

loadPage
loadPage(name, tracer)

The second way to create the page on which pens will leave their marks. An image will be loaded from the file with the given name. See the discussion of tracer above in createPage.

setTracer
setTracer(n)

n must be an integer 0 or greater. 0 is the default. If the value of n is greater than 0, only every nth change made to the page will be rendered to the screen. This increases animation speed.

finish
finish()

If a tracer has been set, the script should end with a finish. This will make any last changes to the page appear on the screen.

getScreenSize
getScreenSize()

Returns the width and height  of the current page as a two member tuple.

clear
clear(color)

Wipes the page clear and gives it a (potentially new) color. If no color is given, the page will remain the color it was before the clear.

savePage
savePage(name)

Save the current contents of the page to a file of the given name. Include the file type, e.g. "fry.jpg".

wait
wait(n)

The last line of code (unless you want euclid's window to close when your script is complete). If no value is given, euclid's window remains open until the user closes it. A value passed to n results in a pause of n seconds before the script continues execution.

Pen Methods
I chose logos for my pen name.

distanceTo
logos.distanceTo(x, y)

Return the distance from logos' current position to the point with coordinates (x, y).

getX
logos.getX()

Return the x-coordinates of logos' current position.

getY
logos.getY()

Return the y-coordinate of logos' current position.

getDir
logos.getDir()

Return logos' current direction in degrees. 0 points right, 90 up, 180 left and 270 down.

getColor
logos.getColor()

Return logos' current color as a RGB triple.

isDown
logos.isDown()

Return a Boolean that answers the question, "Is logos currently down?" If down, logos will leave marks with a goto or a foward.

goto
logos.goto(x, y)

Send logos to the position (x, y). If logos is down, a mark  will be left.

forward
logos.forward(d)

Move logos forward a distance d in logos' current direction. A negative distance results in motion backwards. If logos is down, a mark will be left.

setDir
logos.setDir(d)

Set logos' direction to d given in degrees. 0 points right, 90 up, 180 left and 270 down.

turn
logos.turn(d)

Turn logos by d degrees. Positive is counterclockwise, negative is clockwise.

setColor
logos.setColor(color)

Set the color of the mark that logos makes. The color should be given as a RGB triple.

up
logos.up()

Pick logos up from the page.  If up, logos will not leave a mark if told to goto or to go forward.

down
logos.down()

Put logos down on the page. If down, logos will leave a mark if told to goto or to go forward.

setDelay
logos.setDelay(d)

Set the delay between marks made by logos. 0 is no delay.

point
logos.point()

Drop a point of logos' current color at logos' current position. A point is a single pixel.

beginRegion, endRegion
logos.beginRegion(color), logos.endRegion()

A region is a filled polygonal shape. Place the first before a block of code that draws a polygon by use of some combination of goto's and forward's. Place the second after the polygon is complete and the polygon will be filled with logos' current color.

If no color value is sent to beginRegion, the fill color will be logos' current color; if a color  is sent, that will become the fill color and the boundary color will be logos' current color.

circle
logos.circle(r)

Draw a circle of radius r. logos' current position is the center.

disc
logos.disc(r, color)

Draw a disc of radius r. (A disc is a filled circle.) logos' current position is the center.

If a color value is sent to disc, that will become the fill color and the boundary color will be logos' current color; if no color value is sent, the boundary and interior will both be logos' current color.

write
logos.write(text, fontName, fontSize)

Write the given text in the given font at the given size. The font name should be passed as a string, e.g. "Times New Roman". The default font is Arial and the default font size is 30.


ALL CREDITS FOR EUCLID GO TO DR. FRANKLIN MASON.