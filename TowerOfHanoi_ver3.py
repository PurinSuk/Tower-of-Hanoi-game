### import all necessary module ###

#import deque from collections module (to use stack data structure)
from collections import deque
#import all modules of tkinter
from tkinter import *
#import a module for a messagebox
import tkinter.messagebox


### define all functions here ###

#define okFunction which is activated whenever an ok button is pressed
def okFunction():
    global numberOfMove
    global peg_1
    global peg_2
    global root
    fromStack = peg_1.get()
    toStack = peg_2.get()

    #if the player does not choose stacks to take/place disks from/on
    if fromStack == -1 or toStack == -1:
        tkinter.messagebox.showerror("Error",
                                     "Please choose from which stack to which stack you would like to move a disk")
    #if the player chooses to take and place a disk from and to the same stack
    elif fromStack == toStack:
        tkinter.messagebox.showerror("Error",
                                     "Not possible to move a disk from and to the same stack")
    #if the stack from which a disk is moved is not empty
    elif stack[fromStack-1]:
        #if the stack to which the disk is moved is empty, or the move is eligible
        if not(stack[toStack-1]) or stack[fromStack-1][-1].disk.rank < stack[toStack-1][-1].disk.rank:
            for elem in range(len(emptyLabelList)):
                emptyLabelList[elem].destroyLabel()
            movingDisk = stack[fromStack-1][-1]
            stack[fromStack-1].pop()
            stack[toStack-1].append(movingDisk)
            insertEmptyRow()
            stack[toStack-1][-1].disk.grid(row=6-len(stack[toStack-1]), column=toStack-1, padx=10)
            numberOfMove.set(numberOfMove.get()+1)
            NumberLabel = Label(bottomFrame, text="Number of moves: " + str(numberOfMove.get()))
            NumberLabel.grid(row=2, column=1, pady=5)
            """
            for elem in range(len(stack[fromStack-1])):
                print(stack[fromStack-1][elem].disk.rank)
            """

        #if the move is not eligible (larger on smaller disks)
        elif stack[fromStack-1][-1].disk.rank > stack[toStack-1][-1].disk.rank:
            tkinter.messagebox.showerror("Error", "Moving a larger disk onto a smaller one is not allowed")
    #if the stack from which a disk is moved is empty
    else:
        tkinter.messagebox.showerror("Error",
                                     "Your chosen stack contains no disks")
    #check whether the game has ended or not, if yes then close the game
    if len(stack[-1])==5:
        tkinter.messagebox.showinfo("Congratulations", "You win the game with " + str(numberOfMove.get()) + " moves")
        root.quit()

### create all Graphical User Interface ###

#create the main window
root = Tk(className="Tower of Hanoi")
root.geometry("500x350")

#create three different frames: one for a game title, one for disks, and one for game tools
topFrame = Frame(root)
topFrame.pack(side=TOP)
middleFrame = Frame(root)
middleFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


#create a label for the game title
gameTitle = Label(topFrame, text="Tower Of Hanoi", font=15, fg="blue")
gameTitle.grid(row=0, column=0)
emptySpace = Label(topFrame, text="")
emptySpace.grid(row=1, column=0)

#create a label of each stack
firstStackLabel = Label(middleFrame, text="<--------1st stack-------->")
firstStackLabel.grid(row=6, column=0)
secondStackLabel = Label(middleFrame, text="<--------2nd stack-------->")
secondStackLabel.grid(row=6, column=1)
thirdStackLabel = Label(middleFrame, text="<--------3rd stack-------->")
thirdStackLabel.grid(row=6, column=2)


#create a label for the text "Move from"
moveLabel = Label(bottomFrame, text="Move from")
moveLabel.grid(row=0, column=0, sticky=E, pady=5)

#create an integer variable to store the value telling which stack the player wants to move the disk from
peg_1 = IntVar(bottomFrame)
peg_1.set(-1)
#create a drop down menu for the player to choose the stack
optionMenu_1 = OptionMenu(bottomFrame, peg_1, "1", "2", "3")
optionMenu_1.grid(row=0, column=1, pady=5)

#create a label for the text "to"
toLabel = Label(bottomFrame, text="to")
toLabel.grid(row=0, column=2, pady=5)

#create an integer variable to store the value telling which stack the player wants to move the disk to
peg_2 = IntVar(bottomFrame)
peg_2.set(-1)
#create a drop down menu for the player to choose the stack
optionMenu_2 = OptionMenu(bottomFrame, peg_2, "1", "2", "3")
optionMenu_2.grid(row=0, column=3, pady=5)

#create the ok button
okButton = Button(bottomFrame, text="OK", command=okFunction, height=2, width=5)
okButton.grid(row=1, column=1, pady=3)

#create a variable to keep track of the number of moves & the label for a text "Number of moves: "
numberOfMove = IntVar(bottomFrame)
numberOfMove.set(0)
NumberLabel = Label(bottomFrame, text="Number of moves: " + str(numberOfMove.get()))
NumberLabel.grid(row=2, column=1, pady=5)

#create a class disk for each disk in the game
class disk():
    def __init__(self, widthInput):
        self.disk = Button(middleFrame, text = widthInput, height=1, width=3*widthInput+3)
        self.disk.rank = widthInput
        self.disk.grid(row=widthInput, column=0)


#create a list allDisks to store all disks
allDisks = []
for currentDisk in range(5, 0, -1):
    allDisks.append(disk(currentDisk))


#create three stacks
stack_1 = deque()
stack_2 = deque()
stack_3 = deque()

#put all disks into the first stack
for elem in range(len(allDisks)):
    stack_1.append(allDisks[elem])

#create a list of stacks to hold all three stacks
stack = []
stack.append(stack_1)
stack.append(stack_2)
stack.append(stack_3)

#create a class of an empty label (to be used as a replacement of a moved disk)
class emptyLabel():
    def __init__(self, inputrow):
        self.label = Label(middleFrame, text=" ")
        self.label.grid(row=inputrow+1, column=0)
    def destroyLabel(self):
        self.label.destroy()

#create an empty list to store empty labels
emptyLabelList = []

#define a function which will replace an empty row with empty labels when called
def insertEmptyRow():
    for elem in range(5 - len(stack_1)):
        emptyLabelList.append(emptyLabel(elem))


#call a function to maintain the main window
root.mainloop()
