One of your friends wonders out loud how probable it would to hit a colored section of the painting if they were to close their eyes and throw a dart at random at the canvas. You tell your friend that this is a very bad idea, but because you are in an Introduction to Computer Programming class you know that you can use your newly acquired Python skills to solve this problem!

For this program you will be writing some code that will simulate the throwing of a random dart at this modern art painting. To do this you can repeatedly generate a random coordinate within the painting area and test to see which shape (if any) the dart falls into. Note that the playing field is 800 units wide and 500 units high, so you will be generating random coordinates within this range as part of your simulation.

When you are finished you should calculate the % chance of a dart hitting a particular shape. Refer to the schematic below for the exact measurements of the painting. Hint: Start off by simulating just one dart toss and use the coordinate plane to determine if the dart has fallen into one of the colored regions. Start off with the red rectangle since it will be the simplest shape to work with -- how can you write a statement to determine if a point falls within a rectangle? From there, expand this logic and apply it to the other shapes. Hint: you may need the distance formula again to determine if a point falls within a circular region! Once you are confident that you have designed an effective algorithm you can scale up and place your code inside a loop.

Some hints:

You can ask Python to generate the current time by calling the time.time() function. You will need to import the time module in order to call this function.
A Monte Carlo simulation approximates a solution to a problem. Because of this you will see different numbers when you run your program. The percentages that get generates should roughly match the percentages shown here.
The more "throws" you compute the closer you will get to the actual solution.
You can generate a random floating point number within a given range by using the random.uniform() function. This function takes two arguments - a low boundary and a high boundary - and generates a floating point number within this range (edges inclusive)
The coordinate system shown here is one that is standard in the world of computer graphics -- notice that the origin point is at the top left side of the screen, and that the y axis only contains positive values.
You will need to format your output to match the sample output above (i.e. all of your values should line up)
Your "execution time" value will likely be different than the ones given here in the sample output. This is due to the fact that every computer will run at a slightly different rate based on processor speed, available memory, etc.
