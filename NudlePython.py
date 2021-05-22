from tkinter import *
window = Tk()
window.title('GitHub Desktop')
window.geometry('600x500')
window.configure(background='Yellow')

lbl01 = Label(window, text='Sign Up', font = ('Gordita Black', 35),fg = 'Gray90', bg = 'Yellow')
lbl01.grid(column = 0,row = 0)

txt01 = Entry(window, width = 50)
txt01.grid(column = 0, row = 5)

lbl02 = Label(window, text = 'Username', font = ('Montserrat Medium', 10), fg = 'Black', bg = 'Yellow')
lbl02.grid(column = 2, row = 5)

txt02 = Entry(window, width = 50)
txt02.grid(column = 0, row = 10)

lbl03 = Label(window, text='Password', font = ('Montserrat Medium', 10),fg = 'Black', bg = 'Yellow')
lbl03.grid(column = 2,row = 10)

lbl0 = Label(window, text='.', font = ('Arial', 1), fg = 'Yellow', bg = 'Yellow')
lbl0.grid(column= 0, row = 110)

loginsave = txt01.get()
passwordsave = txt02.get()

def clicked2():
	loginsave = txt01.get()
	passwordsave = txt02.get()

	lbl01.configure(text='Sign In', font = ('Gordita Black', 35),fg = 'Gray90', bg = 'Yellow')
	lbl01.grid(column = 0,row = 0)

	txt01.configure(width = 50)
	txt01.grid(column = 0, row = 5)

	lbl02.configure(text = 'Username', font = ('Montserrat Medium', 10), fg = 'Black', bg = 'Yellow')
	lbl02.grid(column = 2, row = 5)

	txt02.configure(width = 50)
	txt02.grid(column = 0, row = 10)

	lbl03.configure(text='Password', font = ('Montserrat Medium', 10),fg = 'Black', bg = 'Yellow')
	lbl03.grid(column = 2,row = 10)


	def clicked():
		if txt01.get() == loginsave and txt02.get() == passwordsave:
			lbl0.configure(text=("Hello!", loginsave), font = ('Montserrat Medium', 20),fg = 'Black', bg = 'Yellow')
			lbl0.grid(column = 0, row = 40)  
		else:
			lbl0.configure(text='Login or password is not correct', font = ('Montserrat Medium', 12),fg = 'Red', bg = 'Yellow')
			lbl0.grid(column = 0, row = 80)

	btn01.configure(text = 'Sign In', font = ('Montserrat Medium',10), fg = 'Black', bg = 'Orange', command=clicked)
	btn01.grid(column = 0, row = 18)

btn02 = Button(window, text = 'Already have an account?', font = ('Montserrat Medium',10), fg = 'Black', bg = 'Orange',command = clicked2)
btn02.grid(column = 4, row = 80)

def clicked1():
	loginsave = txt01.get()
	passwordsave = txt02.get()

	lbl01.configure(text='Sign In', font = ('Gordita Black', 35),fg = 'Gray90', bg = 'Yellow')
	lbl01.grid(column = 0,row = 0)

	txt01.configure(width = 50)
	txt01.grid(column = 0, row = 5)

	lbl02.configure(text = 'Username', font = ('Montserrat Medium', 10), fg = 'Black', bg = 'Yellow')
	lbl02.grid(column = 2, row = 5)

	txt02.configure(width = 50)
	txt02.grid(column = 0, row = 10)

	lbl03.configure(text='Password', font = ('Montserrat Medium', 10),fg = 'Black', bg = 'Yellow')
	lbl03.grid(column = 2,row = 10)

	def clicked3():
		if txt01.get() == loginsave and txt02.get() == passwordsave:
			lbl0.configure(text=("Hello!", loginsave), font = ('Montserrat Medium', 20),fg = 'Black', bg = 'Yellow')
			lbl0.grid(column = 0, row = 40)  
		else:
			lbl0.configure(text='Login or password is not correct', font = ('Montserrat Medium', 12),fg = 'Red', bg = 'Yellow')
			lbl0.grid(column = 0, row = 80)

	btn01.configure(text = 'Sign In',fg = 'Black', bg = 'Orange', command=clicked3)
	btn01.grid(column = 0, row = 18)



btn01 = Button(window, text = 'Sign Up', font = ('Montserrat Medium',10), fg = 'Black', bg = 'Orange', command = clicked1)
btn01.grid(column = 0, row = 18)


window.mainloop()