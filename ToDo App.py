from tkinter import *
from tkinter import messagebox
import random

class ToDo:
	def __init__(self, master):
		self.master = master
		self.tasks = []

		self.screen()

	def updatecount(self):
		return self.labelcount.config(text = len(self.tasks))

	def updatelist(self):
		self.list.delete(0, END)
		for i in self.tasks:
			self.list.insert(END, i)

	def add(self, text):
		if text == "":
			self.label.config(text = "Please enter text")

		else:
			self.tasks.append(text)
			self.updatecount()
			self.entry.delete(0, END)
			self.label.config(text = "")
			self.updatelist()

	def done(self):
		if self.list.curselection():
			task = self.list.get(ANCHOR)
			if task in self.tasks:
				self.tasks.remove(task)

			self.updatecount()
			self.label.config(text = "")
			return self.list.delete(ANCHOR)

		else:
			return self.label.config(text = "Select a Task")

	def delete(self):
		deletemessage = messagebox.askyesno("ToDo App", "Are you sure to delete all tasks?")
		if deletemessage == True:
			self.tasks.clear()
			self.updatecount()
			self.list.delete(0, END)
			self.label.config(text = "")

	def sorta(self):
		if len(self.tasks) != 0: 
			self.tasks.sort()
			self.list.delete(0, END)
			for i in self.tasks:
				self.list.insert(END, i)

		else:
			return self.label.config(text = "No tasks")

	def sortb(self):
		if len(self.tasks) != 0:
			self.tasks.sort(reverse = True)
			self.list.delete(0, END)
			for i in self.tasks:
				self.list.insert(END, i)

		else:
			return self.label.config(text = "No tasks")

	def randomtask(self):
		try:
			task = random.choice(self.tasks)
			self.label.config(text = task)
		except:
			return self.label.config(text = "No tasks")

	def numbertasks(self):
		return self.label.config(text = len(self.tasks))

	def exit(self):
		closebox = messagebox.askyesno("ToDo App", "Are you sure you want to exit?")
		if closebox == True:
			return self.master.destroy()

	def load(self):
		loadmessage = messagebox.askyesno("ToDo App", "load last progress?")
		if loadmessage == True:
			self.tasks.clear()
			self.list.delete(0, END)
			with open("loads.txt", "r") as file:
				for i in file:
					self.tasks.append(i.replace("\n", ""))
					self.list.insert(END, i.replace("\n", ""))
				self.updatecount()

	def save(self):
		savemessage = messagebox.askyesno("ToDo App", "Save your progress?")
		if savemessage == True:
			with open("loads.txt", "w") as file:
				file.truncate(0)
				for i in self.tasks:
					file.write(f"{i}\n")

	def info(self):
		messagebox.showinfo("ToDo App", "This is ToDo App V.1.0\nCreated by Kazy22\nPython Project")


	def screen(self):
		# Label
		self.todo_label = Label(self.master, text = "ToDo App", bg = "black", fg = "white", font = ("Sans-Bold", 15))
		self.label = Label(self.master, text = "", bg = "black", fg = "white")
		self.labelcount = Label(self.master, text = len(self.tasks), fg = "white", bg = "black")

		self.todo_label.grid(row = 0, column = 0)
		self.label.grid(row = 0, column = 1, columnspan = 2, sticky = W + E)
		self.labelcount.grid(row = 0, column = 3, padx = 5)

		# Buttons
		self.add_b = Button(self.master, text = "Add ToDo", bg = "green", fg = "white", font = ("Sans-Bold", 15), bd = 0, width = 17, command = lambda: self.add(self.entry.get()))
		self.done_b = Button(self.master, text = "Done Task", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.done)
		self.delete_b = Button(self.master, text = "Delete All  ", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.delete)
		self.sorta_b = Button(self.master, text = "Sort (ASC)", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.sorta)
		self.sortb_b = Button(self.master, text = "Sort (DSC)", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.sortb)
		self.random_b = Button(self.master, text = "Random Task", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.randomtask)
		self.number_b = Button(self.master, text = "Number of Task", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.numbertasks)
		self.exit_b = Button(self.master, text = "Exit App", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.exit)
		self.load_b = Button(self.master, text = "Load LastToDo List", bg = "#676767", fg = "white", font =("Sans-Bold", 15), bd = 0, width = 17, command = self.load)
		self.save_b = Button(self.master, text = "Save ToDo List", bg = "#676767", fg = "white", font = ("Sans-Bold", 15), bd = 0, width = 17, command = self.save)
		self.info_b = Button(self. master, text = "Info", bg = "#676767", fg = "white", font = ("Sans-Bold", 15), bd = 0, width = 17, command = self.info)


		self.add_b.grid(row = 1, column = 0)
		self.done_b.grid(row = 2, column = 0)
		self.delete_b.grid(row = 3, column = 0)
		self.sorta_b.grid(row = 4, column = 0)
		self.sortb_b.grid(row = 5, column = 0)
		self.random_b.grid(row = 6, column = 0)
		self.number_b.grid(row = 7, column = 0)
		self.exit_b.grid(row = 8, column = 0)
		self.load_b.grid(row = 9, column = 0)
		self.save_b.grid(row = 9, column = 1, sticky = W, padx = (5, 0))
		self.info_b.grid(row = 9, column = 2, sticky = W)

		# Listbox
		self.entry = Entry(self.master, width = 26, font = ("Sans-Bold", 20), bd = 0, bg = "#404040", fg = "white")
		self.list = Listbox(self.master, width = 45, height = 12, bg = "#404040", fg = "white", font = ("Sans-Bold", 12))

		self.entry.grid(row = 1, column = 1, columnspan = 2, padx = (0, 18))
		self.list.grid(row = 2, column = 1, rowspan = 7, columnspan = 2, padx = (5, 25))



def main():
	root = Tk()
	root.title("ToDo Application")
	root.iconbitmap("icon/todo.ico")
	root.resizable(0, 0)
	root.config(bg = "black")

	ToDo(root)
	command = ToDo(root)

	root.protocol('WM_DELETE_WINDOW', command.exit)
	root.mainloop()

if __name__ == "__main__":
	main()