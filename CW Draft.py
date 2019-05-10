#Software Development Coursework 2: To-Do List. Created by Steven Pacitti (3726429) and Matt Goody (3729256)

#The program starts by importing relevant libraries for use
import tkinter as root          #this line importants tkinter and defines it as 'root', to prevent the need to define tkinter later.
from tkinter import *           #this imports the main features of tkinter. Tkinter is used to create GUIs within python.
from tkinter import messagebox  #this imports messagebox from tkinter, allowing the use of pop-up windows.
import datetime                 #this imports datetime, meaning the program can use the computer to find the current date.

#First, an object class is defined. This is what To-Do tasks will be saved as when going to the .csv file, and when coming into the program from the .csv. It standardizes the layout of task variables.
class ToDoTask:
    def __init__(self, TaskName, TaskDesc, Status, Priority, StartD, StartM, StartY, EndD, EndM, EndY):  #This initializes 'self' first, which refers to the instance of the object. The remaining words are the different attributes of a task, which will all be entered by users of the program.
        self.TaskName = TaskName    #This means that whenever an object is referenced with the extension of .TaskName, it will refer to the 'TaskName' part of the ToDoTask object. This same principle applies to the rest of the code in this class.
        self.TaskDesc = TaskDesc
        self.Status = Status
        self.Priority = Priority
        self.StartD = StartD
        self.StartM = StartM
        self.StartY = StartY
        self.EndD = EndD
        self.EndM = EndM
        self.EndY = EndY
        
#This next class holds the entire program. It is defined as the menu.
class Menu(root.Tk):    #(root.Tk) is from when tkinter was imported as root. This simply allows the class to access all of the tkinter module.
    def __init__(self): #This initializes self, which refers to the program itself in this case.
        root.Tk.__init__(self)  #root.Tk is initialized to mean self, so root is not used again.

        self.title("To-Do Manager") #This names the window of the program
        sizex = 440 #Defines the width of the window
        sizey = 238 #Defines the length of the window
        posx = 360 #Defines the x position of where on the screen the window will appear
        posy = 50 #Defines the y position of where on the screen the window will appear
        self.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy)) #This uses the defined dimensions and applies it to the menu window
        self.resizable(False, False) #This prevents the menu window from being resized.

        lblTitle = Label(self, text="Welcome To Your To-Do List", font='Ariel 13 bold') #lblTitle is a Label that will be placed onto self (menu window), using a non-standard font. lblTitle shows off the naming convention for variables that will carry through this program. It's a label, so gets the prefix 'lbl' and it's the title of the window, so gets the relevant name 'Title'
        lblTitle.place(x=110, y=28) #This places the label on the window in an exact location

        btnAddNewTask = Button(self, text="Add New Task", command=self.AddNewTask, cursor='hand2', width=15, font='Ariel 10') #This defines a button for the main menu that will send the code to the 'AddNewTask' module once clicked on. The button is also given a standard size, and will change the users cursor when they hover over it. 
        btnListTasks = Button(self, text="View Tasks", command=self.ListTasks, cursor='hand2', width=15, font='Ariel 10') #This defines a button for the main menu that will send the code to the 'ListTasks' module once clicked on. The button is also given a standard size, and will change the users cursor when they hover over it.
        btnReminder = Button(self, text="Reminder", command=self.Reminder) #This defines a button for the main menu that will send the code to the 'Reminder' module once clicked on. The button will alsochange the users cursor when they hover over it.
        btnQuit = Button(self, text="Quit", command=self.destroy, cursor='hand2', font='Ariel 10') #This defines a button for the main menu that will cause the window to close once clicked on. The button will also change the users cursor when they hover over it.

        btnAddNewTask.place(x=160, y=75)    #This line, and the three below, place the buttons defined above onto the menu window    
        btnListTasks.place(x=160, y=120)
        btnReminder.place(x=10, y=10)
        btnQuit.place(x=390, y=200)

        self.Reminder() #This runs the Reminder function immediately upon opening the program

    def Reminder(self): #This defines 'Reminder' as a function, and passes the value 'self' to the function. This function is used to remind users if they have a task due in for the day of accessing the program.
        try: #This starts a try/except statement for this whole function.
            today = datetime.date.today().strftime("%B %d, %Y")#This checks the current date and saves it as a variable named 'today'
            
            FullTaskList = [] #This makes a new, empty list.
            with open("ToDoList.csv", "r") as f:    #The .csv containing saved tasks is opened to be readable.
                for line in f: #The code iterates through each line of the file and runs the below code during each line.
                    details = line.split(",") #This defines 'details' as a way to place a comma between parts of a line. 
                    SavedTask = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9]) #This defines SavedTask as an instance of the ToDoTask class, with 10 line splits, each one corrolating to one of the attributes of the task in the file. 
                    FullTaskList.append(SavedTask) #The defined SavedTask object is added to the FullTaskList list.
            for SavedTask in FullTaskList: #This code iterates through each task saved to the FullTaskList in the process explained above.
                if (str(SavedTask.EndM) + ' ' + SavedTask.EndD + ', ' + SavedTask.EndY) == today and SavedTask.Status != "Completed": #If the current date (today variable) matches the date of a SavedTask's date, and if the SavedTask has not been marked as complete, the below code will run.
                    messagebox.showinfo("Task Due Today", "The %s task is due to be completed today." % SavedTask.TaskName) #Using the Messagebox library, a pop-up box will appear to warn the user that the relevant SavedTask is due to be completed today.
        except FileNotFoundError: #This is the except part of the statement from the start of the function. If the 'ToDoList.csv' file wasn't found during the function, this prevents the code from breaking by running a pass function instead.
            pass

                
    def AddNewTask(self):#This defines 'AddNewTask' as a function, and passes the value 'self' to the function. This function is used to add a new task to the .csv file.
        self.NewTaskWin = Toplevel(self) #'NewTaskWin' is defined as a higher level window as the self (menu) window. This means that a second window will open, with all code in the function referring to this new window
        self.NewTaskWin.title("Add New Task") #The NewTaskWin is given a title.
        sizex = 440 #Defines the width of the window
        sizey = 250 #Defines the length of the window
        posx = 800 #Defines the x position of where on the screen the window will appear
        posy = 50 #Defines the y position of where on the screen the window will appear
        self.NewTaskWin.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy)) #This uses the defined dimensions and applies it to the AddNewTask window
        self.NewTaskWin.resizable(False, False) #This prevents the new task window from being resized
        
        self.NewTaskWin.entTaskName = StringVar() #This section of code creates variables for each attribute that a user can set for a task, and defines them as either a string or integer variable.
        self.NewTaskWin.entTaskDesc = StringVar()
        self.NewTaskWin.status = StringVar()
        self.NewTaskWin.priority = IntVar()
        self.NewTaskWin.StartDay = StringVar()
        self.NewTaskWin.StartMonth = StringVar()
        self.NewTaskWin.MonthList = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") #This creates a list of each month. It will be used later as the options for an option box
        self.NewTaskWin.StartYear = IntVar()
        self.NewTaskWin.EndDay = StringVar()
        self.NewTaskWin.EndMonth = StringVar()
        self.NewTaskWin.EndYear = IntVar()
        
        lblTitle = Label(self.NewTaskWin, text="Please Add a New To-Do Task",font='Ariel 10 bold') #This makes a title label for the Add New Task window, and gives it a non-standard font.
        lblTitle.place(x=140, y=3) #This places the title label on the window
        
        self.NewTaskWin.grid_rowconfigure(0, minsize=35) #This gives row 0 some substance. This is so row 1 is below lblTitle. lblTitle used .place not .grid or it wouldn't be centered

        #The below section creates an entry box for the user to enter the task name, and makes a relevant label for users to understand the field. The widgets are then placed in the window.
        lblTaskName = Label(self.NewTaskWin, text="Task Name:") 
        entTaskName = Entry(self.NewTaskWin, textvariable=self.NewTaskWin.entTaskName)
        lblTaskName.grid(row=1, column=0)
        entTaskName.grid(row=1, column=1)
        
        #The below section creates an entry box for the user to enter the task description, and makes a relevant label for users to understand the field. The widgets are then placed in the window.
        entTaskDesc = Entry(self.NewTaskWin, textvariable=self.NewTaskWin.entTaskDesc)
        lblTaskDesc = Label(self.NewTaskWin, text="Task Description:")
        lblTaskDesc.grid(row=1, column=2)
        entTaskDesc.grid(row=1, column=3)

        self.NewTaskWin.status.set('Not Started') #This sets the value of the variable 'status' as Not Started.

        #The below section creates three radio buttons relating to the current completed status of the to-do task. Using the variable defined above, the button with the value Not Started will be automatically selected. These buttons and their relevant label are then placed on the window.
        lblStatus = Label(self.NewTaskWin, text="Current Status:", pady=10)
        rbStatus1 = Radiobutton(self.NewTaskWin, text="Not Started", variable=self.NewTaskWin.status, value='Not Started')
        rbStatus2 = Radiobutton(self.NewTaskWin, text="In Progress", variable=self.NewTaskWin.status, value='In Progress')
        rbStatus3 = Radiobutton(self.NewTaskWin, text="Completed", variable=self.NewTaskWin.status, value='Completed')
        lblStatus.grid(row=2, column=0)
        rbStatus1.grid(row=2, column=1)
        rbStatus2.grid(row=2, column=2)
        rbStatus3.grid(row=2, column=3)

        self.NewTaskWin.priority.set(3) #This sets the value of the varaible 'priority' as 3. 

        #The below section creates 5 radio buttons relating to the priority level of the to-do task. Using the priority variable defined above, the radio button with the value of 3 is automatically selected. The buttons and a relevant label are then all placed on the window
        lblPriority = Label(self.NewTaskWin, text="Priority Level:", pady=10)
        rbPriority1 = Radiobutton(self.NewTaskWin, variable=self.NewTaskWin.priority, value=1)
        rbPriority2 = Radiobutton(self.NewTaskWin, variable=self.NewTaskWin.priority, value=2)
        rbPriority3 = Radiobutton(self.NewTaskWin, variable=self.NewTaskWin.priority, value=3)
        rbPriority4 = Radiobutton(self.NewTaskWin, variable=self.NewTaskWin.priority, value=4)
        rbPriority5 = Radiobutton(self.NewTaskWin, variable=self.NewTaskWin.priority, value=5)
        lblPriority.grid(row=3, column=0)
        rbPriority1.place(x=90, y=98)
        rbPriority2.place(x=170, y=98)
        rbPriority3.place(x=250, y=98)
        rbPriority4.place(x=330, y=98)
        rbPriority5.place(x=410, y=98)

        #This section creates labels to go under each of the priority radio buttons, to make the value of each button clear. They are then placed on the window.
        lblPriority1 = Label(self.NewTaskWin, text="1")
        lblPriority2 = Label(self.NewTaskWin, text="2")
        lblPriority3 = Label(self.NewTaskWin, text="3")
        lblPriority4 = Label(self.NewTaskWin, text="4")
        lblPriority5 = Label(self.NewTaskWin, text="5")
        lblPriority1.place(x=95, y=115)
        lblPriority2.place(x=175, y=115)
        lblPriority3.place(x=255, y=115)
        lblPriority4.place(x=335, y=115)
        lblPriority5.place(x=415, y=115)

        #This sets the variables of StartDay, StartMonth and StartYear as 1, Janurary and 2019 respectibly. The StartMonth variable uses the MonthList variable defined earlier, and sets it's value as the first in the list.
        self.NewTaskWin.StartDay.set(1)
        self.NewTaskWin.StartMonth.set(self.NewTaskWin.MonthList[0])
        self.NewTaskWin.StartYear.set(2019)

        #This creates three option menus, each related to a different variable defined above. The menus are used to select the start date of the task. The menus and a relevant label are then placed in the windoow.
        lblStartDate = Label(self.NewTaskWin, text="Start Date:", pady=10)
        optnbxStartDay = OptionMenu(self.NewTaskWin, self.NewTaskWin.StartDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        optnbxStartMonth = OptionMenu(self.NewTaskWin, self.NewTaskWin.StartMonth, *self.NewTaskWin.MonthList)
        optnbxStartYear = OptionMenu(self.NewTaskWin, self.NewTaskWin.StartYear, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034)
        lblStartDate.grid(row=4, column=0)
        optnbxStartDay.grid(row=4, column=1)
        optnbxStartMonth.grid(row=4, column=2)
        optnbxStartYear.grid(row=4, column=3)

        #This sets the variables of EndDay, EndMonth and EndYear as 1, Janurary and 2019 respectibly. The EndMonth variable uses the MonthList variable defined earlier, and sets it's value as the first in the list.
        self.NewTaskWin.EndDay.set(1)
        self.NewTaskWin.EndMonth.set(self.NewTaskWin.MonthList[0])
        self.NewTaskWin.EndYear.set(2019)

        #This creates three option menus, each related to a different variable defined above. The menus are used to select the end date of the task. The menus and a relevant label are then placed in the windoow.
        lblEndDate = Label(self.NewTaskWin, text="End Date:", pady=10)
        optnbxEndDay = OptionMenu(self.NewTaskWin, self.NewTaskWin.EndDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        optnbxEndMonth = OptionMenu(self.NewTaskWin, self.NewTaskWin.EndMonth, *self.NewTaskWin.MonthList)
        optnbxEndYear = OptionMenu(self.NewTaskWin, self.NewTaskWin.EndYear, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038)
        lblEndDate.grid(row=5, column=0)
        optnbxEndDay.grid(row=5, column=1)
        optnbxEndMonth.grid(row=5, column=2)
        optnbxEndYear.grid(row=5, column=3)
        
        btnAddTask = Button(self.NewTaskWin, text="Add Task", command=self.WriteNewToFile, cursor='hand2', width=34) #A button is defined to access the function WriteToFile, which will write the user inputted task to the .csv file.
        btnMenu = Button(self.NewTaskWin, text="Return To Menu", command=self.NewTaskWin.destroy, cursor='hand2', width=13) #A button is defined to close the current window when pressed

        #The above buttons are placed on the window.
        btnAddTask.place(x=40, y=215)
        btnMenu.place(x=300, y=215)


    def ListTasks(self): #This defines the ListTasks function, accessed from the menu. This will list each task included in the .csv file for the user to view.
        try: #This is the start of a try/except function that runs for the whole section of code. It acts as a safeguard for if the .csv file doesn't exist, like with the Reminder function.
            class Edit(): #This defines a class that will be called within the function.
                def __init__(self, Task, menu): #The class initializes the Task sent to the function.
                    self.task = Task
                    self.menu = menu

                def __call__(self): #When the function is called, it will send the code to the 'EditTask' function, passing the defined Task.
                    self.menu.EditTask(self.task)

            class Delete(): #This defines a class that will be called within the function.
                def __init__(self, Task, menu):  #The class initializes the Task sent to the function.
                    self.task = Task
                    self.menu = menu

                def __call__(self): #When the function is called, it will send the code to the 'DeleteTask' function, passing the defined Task.
                    self.menu.DeleteTask(self.task)

            self.ListTasksWin = Toplevel(self) #'ListTasksWin' is defined as a higher level window as the self (menu) window. This means that a second window will open, with all code in the function referring to this new window
            self.ListTasksWin.title("List All Tasks") #ListTasksWin is given a title.
            sizex = 670 #Defines the width of the window
            sizey = 250 #Defines the length of the window
            posx = 130 #Defines the x position of where on the screen the window will appear
            posy = 320 #Defines the y position of where on the screen the window will appear
            self.ListTasksWin.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy)) #Uses the defined dimensions to set the size of the window.
            self.ListTasksWin.resizable(False, True) #This prevents the ListTasks window from being made wider, but can be made longer.

            lblTitle = Label(self.ListTasksWin, text="All To-Do Tasks",font='Ariel 10 bold') #A title label is made for the window using a non-standard font
            lblTitle.grid(row=0, column=3) #The title label is placed in the window

            #This creates and places a button to close the current window.
            btnReturn = Button(self.ListTasksWin, text="Return To Menu", command=self.ListTasksWin.destroy)
            btnReturn.place(x=560, y=5)

            #This creates 6 different columns and gives them a minimum size of 90 pixels. These columns are where values will be listed, and the minimum size helps to keep the window from looking too messy
            for i in range(0,6):
                self.ListTasksWin.grid_columnconfigure(i, minsize=90)

            #The below section creates and places labels that act as headings to describle the value held in that column.
            lblHeadingTaskName = Label(self.ListTasksWin, text="Task Name")
            lblHeadingTaskDesc = Label(self.ListTasksWin, text="Task Description")
            lblHeadingTaskSDate = Label(self.ListTasksWin, text="Start Date")
            lblHeadingTaskEDate = Label(self.ListTasksWin, text="End Date")
            lblHeadingTaskStatus = Label(self.ListTasksWin, text="Current Status")
            lblHeadingTaskPriority = Label(self.ListTasksWin, text="Priority")
            lblHeadingTaskName.grid(row=1, column=0)
            lblHeadingTaskDesc.grid(row=1, column=1)
            lblHeadingTaskSDate.grid(row=1, column=2)
            lblHeadingTaskEDate.grid(row=1, column=3)
            lblHeadingTaskStatus.grid(row=1, column=4)
            lblHeadingTaskPriority.grid(row=1, column=5)

            FullTaskList = [] #This creates an empty list
            TasksCount = 1 #This is used to count the number of tasks in the .csv file. It is used for formatting.
            with open("ToDoList.csv", "r") as f: #The csv is opened to be read.
                for line in f: #This iterates through each line of the file and defines them as objects of the ToDoTask class, then adds them to the empty list. The process has been explained in the Reminder function.
                    details = line.split(",")
                    Task = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9])
                    FullTaskList.append(Task)               
            for Task in FullTaskList: #This code runs once for each task in the FullTaskList
                TasksCount += 1 #The total value of TasksCount increases by 1
                #The below section creates and places labels that contain each attribute of the tasks listed in the csv file. The TasksCount variable is used to define the row for these labels to be placed on, so that each task appears on a different line in the window
                lblTaskName = Label(self.ListTasksWin, text=Task.TaskName)
                lblTaskDesc = Label(self.ListTasksWin, text=Task.TaskDesc)
                lblTaskSDate = Label(self.ListTasksWin, text=(Task.StartD + ' ' + Task.StartM + ' ' + Task.StartY)) #For clarity, the start day, month, and year are compiled into one field (it appears as DD MM YYYY)
                lblTaskEDate = Label(self.ListTasksWin, text=(Task.EndD + ' ' + Task.EndM + ' ' + Task.EndY)) #For clarity, the end day, month, and year are compiled into one field (it appears as DD MM YYYY)
                lblTaskStatus = Label(self.ListTasksWin, text=Task.Status)
                lblTaskPriority = Label(self.ListTasksWin, text=Task.Priority)
                btnEdit = Button(self.ListTasksWin, text="Edit", command=Edit(Task, self), cursor='hand2', padx=15) #A button is defined and placed with the command 'Edit', which will allow the user to edit the attributes given to the adjacent task. Clicking this button uses the code for the class 'Edit', as defined at the start of this function.
                btnDelete = Button(self.ListTasksWin, text="Delete", command=Delete(Task, self), cursor='hand2') #A button is defined and placed with the command 'Delete', which will allow the user to delete the adjacent task. Clicking this button uses the code for the class 'Delete', as defined at the start of this function.
                lblTaskName.grid(row=TasksCount, column=0)
                lblTaskDesc.grid(row=TasksCount, column=1)
                lblTaskSDate.grid(row=TasksCount, column=2)
                lblTaskEDate.grid(row=TasksCount, column=3)
                lblTaskStatus.grid(row=TasksCount, column=4)
                lblTaskPriority.grid(row=TasksCount, column=5)
                btnEdit.grid(row=TasksCount, column=6)
                btnDelete.grid(row=TasksCount, column=7)
                
        except FileNotFoundError: #This is the except part of the try/except function defined at the start of the function. This means that if the .csv doesn't exist, a messagebox will appear to tell the user to add tasks before trying to list them.
            self.ListTasksWin.destroy()
            messagebox.showinfo("No Tasks", "You have no to-do tasks saved. Please add some using the 'Add New Task' button.")
            


    def DeleteTask(self, Task): #This defines the function DeleteTask, which is used to delete a task from the .csv file. The values self and Task are passed to the function. Self is given so that the function can refer to itself, and Task is given so the code knows what to-do task is being specified by the button call.
        msgboxDelete = messagebox.askquestion ('Delete Task?','Are you sure you want to delete this task?',icon = 'warning') #This displays a pop-up window to confirm the user wants to delete the task. If 'no' is selected, nothing happens.
        if msgboxDelete == 'yes': #If 'yes' was selected from the message box, this code will run.
            with open('ToDoList.csv', 'r') as f: #This opens the csv file
                FullTaskList = [] #An empty list is created
                total = 0 #This creates a variable of 'total', with a value of 0. It will be used to check when the list has ended.
                num_lines = 0 #This creates a variable of 'num_lines' with a value of 0. It  will be used to check when the list has ended.  
                for line in f: #This will iterate through each line in the file, define them as 'SavedTask', an object of the class ToDoTask, then will add them to the empty file. This process has been documented in the Reminders fuunction.
                    details = line.split(",")
                    SavedTask = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9])
                    FullTaskList.append(SavedTask)
                    num_lines += 1 #For every line in the database, the value of num_lines increases by one. This counts the total number of lines (and by extension, tasks) in the database.

                for SavedTask in FullTaskList: #This will iterate through each task in the FullTaskList
                    if SavedTask.TaskName == Task.TaskName and SavedTask.TaskDesc == Task.TaskDesc and SavedTask.Status == Task.Status and SavedTask.Priority == Task.Priority and SavedTask.StartD == Task.StartD and SavedTask.StartM == Task.StartM and SavedTask.StartY == Task.StartY and SavedTask.EndD == Task.EndD and SavedTask.EndM == Task.EndM and SavedTask.EndY == Task.EndY: #If the selected task has each attribute identical to the values of the passed tasks attributes, the below code will run.
                        FullTaskList.remove(SavedTask) #The selected task will be removed from the list of tasks.

                #Once each task has been iterated through to remove the selected task, the full list is written to the .csv file. This will delete anything in the file prior.
                with open('ToDoList.csv', 'w') as file:
                    for SavedTask in FullTaskList:
                        file.write(SavedTask.TaskName + ',' + SavedTask.TaskDesc + ',' + SavedTask.Status + ',' + str(SavedTask.Priority) + ',' + str(SavedTask.StartD) + ',' + str(SavedTask.StartM) + ',' + str(SavedTask.StartY) + ',' + str(SavedTask.EndD) + ',' + str(SavedTask.EndM) + ',' + str(SavedTask.EndY) + ', \n')

            #This will close and reopen the ListTasks window, effectively refreshing it after the task has been deleted.
            self.ListTasksWin.withdraw()
            self.ListTasks()


    def EditTask(self, Task): #This defines the function EditTask, which is used to edit a chosen task. The values self and Task are passed to the function. Self is given so that the function can refer to itself. The task is passed so the window can receive it's values from the chosen task.

        class Rewrite(): #This defines a class that will be called within the function.
            def __init__(self, Task, menu): #The class initializes the Task sent to the function.
                self.task = Task
                self.menu = menu

            def __call__(self):
                self.menu.RewriteToFile(self.task) #When the function is called, it will send the code to the 'RewriteToFile' function, passing the defined Task.
        
        self.EditTaskWin = Toplevel(self) #'EditTaskWin' is defined as a higher level window as the self (menu) window. This means that a new window will open, with all code in the function referring to this new window
        self.EditTaskWin.title("Edit Task") #The edit task window is given a title
        sizex = 440 #Defines the width of the window
        sizey = 250 #Defines the length of the window
        posx = 800 #Defines the x position of where on the screen the window will appear
        posy = 300 #Defines the y position of where on the screen the window will appear
        self.EditTaskWin.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy)) #Uses the defined dimensions to set the size of the window
        self.EditTaskWin.resizable(False, False) #This prevents the window from being resized.

        #The code below is identical to the main code of the 'AddTask' function, as they have the same interface. The only difference is that this function refers to the 'EditTaskWin'. For details of this code, see the AddTask function.
        self.EditTaskWin.entTaskName = StringVar()
        self.EditTaskWin.entTaskName.set(Task.TaskName)

        lblTaskName = Label(self.EditTaskWin, text="Task Name:")
        lblTaskName.grid(row=1, column=0)
        entTaskName = Entry(self.EditTaskWin, textvariable=self.EditTaskWin.entTaskName)
        entTaskName.grid(row=1, column=1)
            
        self.EditTaskWin.entTaskName = StringVar()
        self.EditTaskWin.entTaskDesc = StringVar()
        self.EditTaskWin.status = StringVar()
        self.EditTaskWin.priority = IntVar()
        self.EditTaskWin.StartDay = StringVar()
        self.EditTaskWin.StartMonth = StringVar()
        self.EditTaskWin.MonthList = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        self.EditTaskWin.StartYear = IntVar()
        self.EditTaskWin.EndDay = StringVar()
        self.EditTaskWin.EndMonth = StringVar()
        self.EditTaskWin.EndYear = IntVar()

        self.EditTaskWin.entTaskName.set(Task.TaskName)
        self.EditTaskWin.entTaskDesc.set(Task.TaskDesc)
        self.EditTaskWin.status.set(Task.Status)
        self.EditTaskWin.priority.set(Task.Priority)
        self.EditTaskWin.StartDay.set(Task.StartD)
        self.EditTaskWin.StartMonth.set(Task.StartM)
        self.EditTaskWin.StartYear.set(Task.StartY)
        self.EditTaskWin.EndDay.set(Task.EndD)
        self.EditTaskWin.EndMonth.set(Task.EndM)
        self.EditTaskWin.EndYear.set(Task.EndY)
        
        lblTitle = Label(self.EditTaskWin, text="Please Edit The To-Do Task",font='Ariel 10 bold')
        lblTitle.place(x=140, y=3)
        
        self.EditTaskWin.grid_rowconfigure(0, minsize=35) #This gives row 0 some substance. This is so row 1 is below lblTitle. lblTitle used .place not .grid or it wouldn't be centered
        
        lblTaskName = Label(self.EditTaskWin, text="Task Name:")
        lblTaskName.grid(row=1, column=0)
        entTaskName = Entry(self.EditTaskWin, textvariable=self.EditTaskWin.entTaskName)
        entTaskName.grid(row=1, column=1)
        
        entTaskDesc = Entry(self.EditTaskWin, textvariable=self.EditTaskWin.entTaskDesc)
        lblTaskDesc = Label(self.EditTaskWin, text="Task Description:")
        lblTaskDesc.grid(row=1, column=2)
        entTaskDesc.grid(row=1, column=3)

        lblStatus = Label(self.EditTaskWin, text="Current Status:", pady=10)
        rbStatus1 = Radiobutton(self.EditTaskWin, text="Not Started", variable=self.EditTaskWin.status, value='Not Started')
        rbStatus2 = Radiobutton(self.EditTaskWin, text="In Progress", variable=self.EditTaskWin.status, value='In Progress')
        rbStatus3 = Radiobutton(self.EditTaskWin, text="Completed", variable=self.EditTaskWin.status, value='Completed')
        lblStatus.grid(row=2, column=0)
        rbStatus1.grid(row=2, column=1)
        rbStatus2.grid(row=2, column=2)
        rbStatus3.grid(row=2, column=3)

        lblPriority = Label(self.EditTaskWin, text="Priority Level:", pady=10)
        rbPriority1 = Radiobutton(self.EditTaskWin, variable=self.EditTaskWin.priority, value=1)
        rbPriority2 = Radiobutton(self.EditTaskWin, variable=self.EditTaskWin.priority, value=2)
        rbPriority3 = Radiobutton(self.EditTaskWin, variable=self.EditTaskWin.priority, value=3)
        rbPriority4 = Radiobutton(self.EditTaskWin, variable=self.EditTaskWin.priority, value=4)
        rbPriority5 = Radiobutton(self.EditTaskWin, variable=self.EditTaskWin.priority, value=5)
        lblPriority.grid(row=3, column=0)
        rbPriority1.place(x=90, y=98)
        rbPriority2.place(x=170, y=98)
        rbPriority3.place(x=250, y=98)
        rbPriority4.place(x=330, y=98)
        rbPriority5.place(x=410, y=98)

        lblPriority1 = Label(self.EditTaskWin, text="1")
        lblPriority2 = Label(self.EditTaskWin, text="2")
        lblPriority3 = Label(self.EditTaskWin, text="3")
        lblPriority4 = Label(self.EditTaskWin, text="4")
        lblPriority5 = Label(self.EditTaskWin, text="5")
        lblPriority1.place(x=95, y=115)
        lblPriority2.place(x=175, y=115)
        lblPriority3.place(x=255, y=115)
        lblPriority4.place(x=335, y=115)
        lblPriority5.place(x=415, y=115)
        
        lblStartDate = Label(self.EditTaskWin, text="Start Date:", pady=10)

        optnbxStartDay = OptionMenu(self.EditTaskWin, self.EditTaskWin.StartDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        optnbxStartMonth = OptionMenu(self.EditTaskWin, self.EditTaskWin.StartMonth, *self.EditTaskWin.MonthList)
        optnbxStartYear = OptionMenu(self.EditTaskWin, self.EditTaskWin.StartYear, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034)

        lblStartDate.grid(row=4, column=0)
        optnbxStartDay.grid(row=4, column=1)
        optnbxStartMonth.grid(row=4, column=2)
        optnbxStartYear.grid(row=4, column=3)
        
        lblEndDate = Label(self.EditTaskWin, text="End Date:", pady=10)

        optnbxEndDay = OptionMenu(self.EditTaskWin, self.EditTaskWin.EndDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        optnbxEndMonth = OptionMenu(self.EditTaskWin, self.EditTaskWin.EndMonth, *self.EditTaskWin.MonthList)
        optnbxEndYear = OptionMenu(self.EditTaskWin, self.EditTaskWin.EndYear, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038)

        lblEndDate.grid(row=5, column=0)
        optnbxEndDay.grid(row=5, column=1)
        optnbxEndMonth.grid(row=5, column=2)
        optnbxEndYear.grid(row=5, column=3)
        
        btnAddTask = Button(self.EditTaskWin, text="Save Changes", command=Rewrite(Task, self), cursor='hand2', width=34) #A button is defined and placed with the command 'Rewrite', which will rewrite the selected task with the new inputs. Clicking this button uses the code for the class 'Rewrite', as defined at the start of the function.
        btnMenu = Button(self.EditTaskWin, text="Cancel", command=self.EditTaskWin.destroy, cursor='hand2', width=13)
        
        btnAddTask.place(x=40, y=215)
        btnMenu.place(x=300, y=215)
        

    def WriteNewToFile(self): #This defines the 'WriteNewToFile' function. When this is called, it gets all of the user inputs and writes it to the .csv file to save as a task.
        #This section collects all of the user inputs from the New Task window and defines appropriate variables with their values
        TaskName = self.NewTaskWin.entTaskName.get()
        TaskDesc = self.NewTaskWin.entTaskDesc.get()
        Status = self.NewTaskWin.status.get()
        Priority = self.NewTaskWin.priority.get()
        StartD = self.NewTaskWin.StartDay.get()
        StartM = self.NewTaskWin.StartMonth.get()
        StartY = self.NewTaskWin.StartYear.get()
        EndD = self.NewTaskWin.EndDay.get()
        EndM = self.NewTaskWin.EndMonth.get()
        EndY = self.NewTaskWin.EndYear.get()

        #This section is basic validation of the inputs
        if TaskName == '' or TaskDesc == '': #If the task name or description fields are empty, an error will show to say the user needs to enter values.
            messagebox.showerror("Error", "All fields must have values in order to save this task.")            
        elif StartY > EndY: #If the start year is after the end year, this is impossible, so an error will show to say the user needs to enter valid dates.
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif (StartM == "April" or StartM == "June" or StartM == "September" or StartM == "November") and (int(StartD) >=30): #If a start month with 30 days has the 31st selected, an error will appear to say the user needs to enter valid dates.
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif StartM == "February" and int(StartD) >=28: #If any start day over 28 has been entered with the month of February selected, an error will appear to say the user needs to enter valid dates.
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif (EndM == "April" or EndM == "June" or EndM == "September" or EndM == "November") and (int(EndD) >=30): #If an end month with 30 days has the 31st selected, an error will appear to say the user needs to enter valid dates.
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif EndM == "February" and int(EndD) >=28: #If any end day over 28 has been entered with the month of February selected, an error will appear to say the user needs to enter valid dates.
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")        
        else: #If none of the above errors have been hit, this code will run.
            self.NewTaskWin.destroy() #The add new task window will close
            messagebox.showinfo("Success", "Task Added Successfully") #A message will appear to say the task was saved correctly
            NewTask = ToDoTask(TaskName, TaskDesc, Status, Priority, StartD, StartM, StartY, EndD, EndM, EndY) #The user inputs are placed into a 'NewTask' object, which uses the ToDoTask class.
            with open('ToDoList.csv', 'a') as f: #With the .csv open, the attributes of the NewTask will be added to the file, and a new line will be started.
                f.write(NewTask.TaskName + ',' + NewTask.TaskDesc + ',' + NewTask.Status + ',' + str(NewTask.Priority) + ',' + str(NewTask.StartD) + ',' + str(NewTask.StartM) + ',' + str(NewTask.StartY) + ',' + str(NewTask.EndD) + ',' + str(NewTask.EndM) + ',' + str(NewTask.EndY) + ', \n')
                self.AddNewTask() #The add new task window reopens.

            #this section checks if the list tasks window is open. If so, it will close and reopen, so as to refresh the list and display the newly added task.
            try:
                if 'normal' == self.ListTasksWin.state():
                    self.ListTasksWin.destroy()
                    self.ListTasks()
            except: 
                pass


    def RewriteToFile(self, Task): #This defines the 'RewriteToFile' function. When this is called, it gets all of the user inputs and writes it to the .csv file to replace a task.
        #This section collects all of the user inputs from the Edit Task window and defines appropriate variables with their values
        NewTaskName = self.EditTaskWin.entTaskName.get()
        NewTaskDesc = self.EditTaskWin.entTaskDesc.get()
        NewStatus = self.EditTaskWin.status.get()
        NewPriority = self.EditTaskWin.priority.get()
        NewStartD = self.EditTaskWin.StartDay.get()
        NewStartM = self.EditTaskWin.StartMonth.get()
        NewStartY = self.EditTaskWin.StartYear.get()
        NewEndD = self.EditTaskWin.EndDay.get()
        NewEndM = self.EditTaskWin.EndMonth.get()
        NewEndY = self.EditTaskWin.EndYear.get()

        NewTask = ToDoTask(NewTaskName, NewTaskDesc, NewStatus, NewPriority, NewStartD, NewStartM, NewStartY, NewEndD, NewEndM, NewEndY) #The user inputs are placed into a 'NewTask' object, which uses the ToDoTask class.

        #This section uses the same validation as is shown in the WriteNewToFile function. For details, check that function.
        if NewTaskName == '' or NewTaskDesc == '':
            messagebox.showerror("Error", "All fields must have values in order to save this task.")            
        elif NewStartY > NewEndY:
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif (NewStartM == "April" or NewStartM == "June" or NewStartM == "September" or NewStartM == "November") and (int(NewStartD) >=30):
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif NewStartM == "February" and int(NewStartD) >=28:
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif (NewEndM == "April" or NewEndM == "June" or NewEndM == "September" or NewEndM == "November") and (int(NewEndD) >=30):
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif NewEndM == "February" and int(NewEndD) >=28:
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")        
        else: #If none of the above errors are hit, this code will run
            with open('ToDoList.csv', 'r') as f: #This section of code will open the .csv, make a new list, and run through each line to import the saved tasks to the list. This process was detailed in the Reminder function.
                FullTaskList = []
                total = 0 #This creates a variable of 'total', with a value of 0. It will be used to check when the list has ended. 
                for line in f: 
                    details = line.split(",")
                    SavedTask = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9])
                    FullTaskList.append(SavedTask)

            for SavedTask in FullTaskList: #This will run the below code once for each saved task in the FullTaskList
                if SavedTask.TaskName == Task.TaskName and SavedTask.TaskDesc == Task.TaskDesc and SavedTask.Status == Task.Status and SavedTask.Priority == Task.Priority and SavedTask.StartD == Task.StartD and SavedTask.StartM == Task.StartM and SavedTask.StartY == Task.StartY and SavedTask.EndD == Task.EndD and SavedTask.EndM == Task.EndM and SavedTask.EndY == Task.EndY: #If the saved task has attributes equal to the task originally passed to the function, the below code will run
                    FullTaskList.remove(SavedTask) #The saved task will be removed from the list
                    FullTaskList.append(NewTask) #The new task will be added to the list
                    with open('ToDoList.csv', 'w') as f: #With the .csv open, each task in the FullTaskList will be written to the file. This will delete any data previously there.
                        for SavedTask in FullTaskList:
                            f.write(SavedTask.TaskName + ',' + SavedTask.TaskDesc + ',' + SavedTask.Status + ',' + str(SavedTask.Priority) + ',' + str(SavedTask.StartD) + ',' + str(SavedTask.StartM) + ',' + str(SavedTask.StartY) + ',' + str(SavedTask.EndD) + ',' + str(SavedTask.EndM) + ',' + str(SavedTask.EndY) + ', \n')

            self.EditTaskWin.destroy() #This will close the edit task window
            #This section will close and reopen the list tasks window, effectively refreshing it
            self.ListTasksWin.destroy() 
            self.ListTasks()

#This section defines 'app' as the Menu class, then runs it as the mainloop
app = Menu()
app.mainloop()
