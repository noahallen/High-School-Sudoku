from Tkinter import *
import Tkinter as tk
import random

#Defines all of the global variables
global randomized_board
randomized_board = [5, 3, 4, 6, 7, 8, 9, 1, 2, 6, 7, 2, 1, 9, 5, 3, 4, 8, 1, 9, 8, 3, 4, 2, 5, 6, 7, 8, 5, 9, 7, 6, 1, 4, 2, 3, 4, 2, 6, 8, 5, 3, 7, 9, 1, 7, 1, 3, 9, 2, 4, 8, 5, 6, 9, 6, 1, 5, 3, 7, 2, 8, 4, 2, 8, 7, 4, 1, 9, 6, 3, 5, 3, 4, 5, 2, 8, 6, 1, 7, 9]
global myButtonList 
myButtonList= []
global player_board
player_board= []

#This causes random spots on our board to be replaced with "_", hiding the answers
yes = random.randint(30,50)
player_board = randomized_board
randomized_board = [5, 3, 4, 6, 7, 8, 9, 1, 2, 6, 7, 2, 1, 9, 5, 3, 4, 8, 1, 9, 8, 3, 4, 2, 5, 6, 7, 8, 5, 9, 7, 6, 1, 4, 2, 3, 4, 2, 6, 8, 5, 3, 7, 9, 1, 7, 1, 3, 9, 2, 4, 8, 5, 6, 9, 6, 1, 5, 3, 7, 2, 8, 4, 2, 8, 7, 4, 1, 9, 6, 3, 5, 3, 4, 5, 2, 8, 6, 1, 7, 9]
for x in range(yes):
    spot = random.randint(0,80)
    player_board[spot] = '_'

#This function is what is called when a button is pressed
def callback(event):
    
    #Calls the global variable player_board
    global player_board
    
    #Sets button to start at 0 instead of 1 for the for loop.
    button = 0
    
    #Creates a for loop to check each button name against a list of the button names to return the position value of the pressed button
    for button in range(81):
        
        #Creates the variable myWidgetName to set it equal to the button name
        myWidgetName = event.widget._name
        
        #Checks the button pressed name against the list of button names to return the position of the button on the grid
        if myButtonList[button].count(myWidgetName) > 0:
            print("Button Number:" + str(button)) 
            
            #Sets the variable answer to the position of the button on the grid
            answer = button 
              
            #Takes input from the user to check their answer
    entryVal = input("Enter Number Here: ")
    
    #If the entered value is equal to the list position's value, then display good job 
    if entryVal == randomized_board[answer]:
        player_board[answer] = randomized_board[answer]
        print("")
        print("Good Job")
        
        #Causes the display to update the value if guessed correctly
        event.widget.config(text=entryVal)
        
        #If the entire board is filled out, you win
        if player_board == randomized_board:
            print("")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            print("YOU WON CONGRATULATIONS")
            #Closes the finished board
            root.destroy()
            
    #If incorrect, display incorrect and try again
    else:
        print("")
        print("Incorrect")
        print("Try Again")

#Creates the class gameboard
class GameBoard(tk.Frame):
    
    #Defines the init function which creates the grid structure
    def __init__(self, parent, rows=9, columns=9, size=64, color="white"):
        #Defines variables to be used while creating the grid
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color = color

        #Sets the length and width of the window depending on the size of the boxes and how large the grid is
        canvas_width = columns * size
        canvas_height = rows * size

        #Initializes the window size, thickness, and background color 
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, highlightthickness=0, width=canvas_width, height=canvas_height, background="#00ffff")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        #Initializes the board size 
        xsize = int(self.size)
        ysize = int(self.size)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color
        
        #Defines global variables to be used for creating the board
        global player_board
        global myButtonList 
        global randomized_board
        
        #randomized_board = [5, 3, 4, 6, 7, 8, 9, 1, 2, 6, 7, 2, 1, 9, 5, 3, 4, 8, 1, 9, 8, 3, 4, 2, 5, 6, 7, 8, 5, 9, 7, 6, 1, 4, 2, 3, 4, 2, 6, 8, 5, 3, 7, 9, 1, 7, 1, 3, 9, 2, 4, 8, 5, 6, 9, 6, 1, 5, 3, 7, 2, 8, 4, 2, 8, 7, 4, 1, 9, 6, 3, 5, 3, 4, 5, 2, 8, 6, 1, 7, 9]
        #Creates nested for loops to create a grid of squares and then placing buttons inside of each square
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                gridPosition = ((row*9) + col)
                
                #Creates the grid of squares
                m = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                
                #Creates the grid of buttons and adds the text to each button
                myButton = Button(self.canvas, text = player_board[gridPosition], font = ("Arial", 12, "bold"), padx = (self.size*.25), pady = (self.size*.19))
                
                #Binds the button to the command callback
                myButton.bind('<Button-1>', callback)
                
                #Adds each button value to a list for comparison
                myButtonList.append([myButton._name])
                
                #Places each button
                myButton.place(x = x1+.08*self.size, y = y1+.08*self.size)
                
        #Creates the bold lines every three rows and columns in the previous grid to separate the grid into 3 by 3 blocks     
        for row in range(self.rows):
            for col in range(self.columns):       
                if col % 3 == 0 and row % 3 == 0:
                    x1 = (col * self.size)
                    y1 = (row * self.size) 
                    #Places each bold gridline
                    self.canvas.create_rectangle(x1+2, y1+2, x1 + 2 + 3*self.size, y1 + 2 + 3*self.size, outline="black", tags="square", width = 4)
                    

if __name__ == "__main__":
    root = tk.Tk()  
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()