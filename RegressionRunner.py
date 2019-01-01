import tkinter as tk
from tkinter import *
import pandas as pd 
import statsmodels.api as sm

def setupGUI():
	root = tk.Tk()
	root.geometry("600x600")
	root.configure(background="white")
	frame = tk.Frame(root)
	frame.grid()
	#add label displaying app name
	nameLabel = Label(root, text="Welcome to RegressionRunner!",background="white", padx=200)
	nameLabel.grid(row=1, column=2)
	# add label to tell user to input path
	inputInstructions = Label(root, text="Input the path to your .csv file:")
	inputInstructions.grid(row=4, column=2)
	# add entry box to get path to csv
	pathEntryBox = Entry(root)
	pathEntryBox.grid(row=5, column=2)
	#add button to run regression
	runReg = tk.Button(root, text="Run Linear Regression", command=lambda: runRegression(pathEntryBox.get()), background="white",fg="black")
	runReg.grid(row=7, column=2)
	#add button to view dataframe
	viewDataButton = tk.Button(root, text="View Data", command=lambda: viewData(pathEntryBox.get()))
	viewDataButton.grid(row=8,column=2)
	#add instructions button
	instrButton = tk.Button(root, text="Click here for instructions", command=lambda: showInstructions())
	instrButton.grid(row=9,column=2)
	#add button to quit application
	quitButton = tk.Button(root, text="QUIT", fg="red", command=quit,bg="white")
	quitButton.grid(row=10, column=2)
	#execute
	root.mainloop()

def viewData(path):
	data = pd.read_csv(path)
	frame = tk.Tk()
	#title on frame
	title = Label(frame, text="Here is the first ten rows of the data:")
	title.grid(row=1, column=1)
	#label to view data
	dataToShow = data.head(10)
	lbl = Label(frame, text=dataToShow)
	lbl.grid(row=2, column=1)
	# add button to quit application
	quitButton = tk.Button(frame, text="QUIT", fg="red", command=quit, bg="white")
	quitButton.grid(row=3, column=2)
	frame.mainloop()
	print("viewData")

def main():
	setupGUI()
	
def runRegression(path):
	print("Path to csv file: ", path)
	print("Running regression...")
	#code to run regression...
	#read data file
	data = pd.read_csv(path)
	#covert excel data to pandas dataframe (contains rows and columns)
	dataFrame = pd.DataFrame(data)
	#fetch specific columns to include in regression analysis
	x = dataFrame[dataFrame.columns[0:1]]
	y = dataFrame[dataFrame.columns[1:2]]
	#performs OLS Linear Regression
	results = sm.OLS(x, y).fit()
	summary = results.summary()
	print(summary)
	#show user results in frame
	root = tk.Tk()
	root.geometry("600x800")
	root.configure(background="white")
	frame = tk.Frame(root)
	frame.grid()
	resultsLabel = tk.Label(root, text=summary)
	resultsLabel.grid(row=1,column=1)
	#add button to explain regression results
	explainButton = Button(root, text="Click here for an explanation of these results", command=lambda: explainRegressionResults())
	explainButton.grid(row=2,column=1)
	#add button to exit application
	# add button to quit application
	quitButton = tk.Button(root, text="QUIT", fg="red", command=quit, bg="white")
	quitButton.grid(row=3, column=2)

def explainRegressionResults():
	root = tk.Tk()
	root.geometry("600x600")
	root.configure(background="white")
	frame = tk.Frame(root)
	frame.grid()
	#store text in strings
	intro = "There are several important things the regression results tells you."
	firstThing1 = "First, the r-squared tells you how much your independent variable explains your dependent variable.\n"
	firstThing2 = "This means if your r-squared if .4, your independent variable explains 40% of your dependent variable.\n"
	secondThing1 = "Second, the coefficient (which is called coef in the analysis) tells you how much a change in your independent variable affects your dependent variable.\n"
	secondThing2 = "For example, if the coefficient is -2, then an increase of 1 in your independent variable decreases the dependent variable by 2.\n"
	conclusion = "Those are the most important things in the analysis without becoming too technical. More information can be found online.\n"
	explanation = firstThing1 + firstThing2 + secondThing1 + secondThing2 + conclusion
	#add label to explain results
	explainLabel = Label(root, text=explanation)
	explainLabel.grid(row=1,column=1)
	# add button to quit application
	quitButton = tk.Button(root, text="QUIT", fg="red", command=quit, bg="white")
	quitButton.grid(row=2, column=2)

def showInstructions():
	root = tk.Tk()
	root.geometry("600x600")
	root.configure(background="white")
	frame = tk.Frame(root)
	frame.grid()
	instrLabel = Label(root, text="Open your .csv file in excel and make sure that your independent variable \n is in the first column and your dependent varialbe is in the second column. \nThen, place the path to that file into this application\nand click run regression to see the output.")
	instrLabel.grid(row=1, column=1)
	# add button to quit application
	quitButton = Button(root, text="QUIT", fg="red", command=quit, bg="white")
	quitButton.grid(row=2, column=1)
	frame.mainloop()
#call main method to run app
main()