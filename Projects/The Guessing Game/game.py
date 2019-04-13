import random
from tkinter import *

#Max and Min Limit
MAX = 10
MIN = 1

class Application(Frame):
    #GUI

    def __init__(self, master):
        Frame.__init__(self, master)
        master.minsize(width=500, height=200)
        self.grid()

        self.create_widgets()

        self.number = random.randrange(MIN, MAX +1)

        self.tries = 0

    def create_widgets(self):
        Label(self,
              text="I'm thinking of a number between " + str(MIN) +
                   " and " + str(MAX)
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Try to guess the number"
              ).grid(row=1, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Number Of Tries: 0"
              ).grid(row=0, column=2, columnspan=1, sticky=W)

        Label(self,
              text="Guess"
              ).grid(row=2, column=0, sticky=W)

        # Entry
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        # Submit button
        Button(self,
               text="Enter",
               command=self.get_guess
               ).grid(row=2, column=2, columnspan=4, sticky=W)
        Button(self,
               text="Reset",
               command=self.reset
               ).grid(row=1, column=2, columnspan=1, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=3, column=0, columnspan=3)

    def get_guess(self):
        try:
            guess = int(self.guess_ent.get())
        except(ValueError):
            self.display_message("Invalid entry. Try again.")
        else:
            self.tries += 1
            Label(self,
                  text="Number Of Tries: " + str(self.tries)
                  ).grid(row=0, column=2, columnspan=1, sticky=W)
            self.check_guess(guess)

    def check_guess(self, guess):
        if guess < MIN or guess > MAX:
            self.display_message("Invalid Input, Guess Out Side Of Range.")
            self.tries -= 1  # This try doesn't count
            return

        # If guess equals the number, end current game.
        if guess == self.number:
            self.resetgame()
            return

        # Otherwise, see if guess is higher or lower than the chosen number.
        if guess < self.number:
            self.display_message("Guess Higher...")
            return
        elif guess > self.number:
            self.display_message("Guess Lower...")
            return

    def display_message(self, message):
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

    def reset(self):
        #Game Reset
        self.number = random.randrange(MIN, MAX + 1)
        self.display_message("Game Reset. Please enter another number to play again.")
        self.tries = 0
        Label(self,
              text="Number Of Tries: " + str(self.tries)
              ).grid(row=0, column=2, columnspan=1, sticky=W)

    def resetgame(self):
        self.display_message("Congrats! You guessed correctly. The number was " + \
                             str(self.number) + ". And it only took you " + \
                             str(self.tries) + " tries!" + " Click The Reset Button To Play Again")

def main():
    root = Tk()
    root.title("The Guessing Game")
    app = Application(root)
    root.mainloop()

# start Guess My Number
main()