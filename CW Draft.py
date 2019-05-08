import tkinter as root
from tkinter import *
from tkinter import messagebox
import datetime


class ToDoTask:
    def __init__(self, TaskName, TaskDesc, Status, Priority, StartD, StartM, StartY, EndD, EndM, EndY):
        self.TaskName = TaskName
        self.TaskDesc = TaskDesc
        self.Status = Status
        self.Priority = Priority
        self.StartD = StartD
        self.StartM = StartM
        self.StartY = StartY
        self.EndD = EndD
        self.EndM = EndM
        self.EndY = EndY
        

class Menu(root.Tk):
    def __init__(self):
        root.Tk.__init__(self)
        self.title("To-Do Manager")
        sizex = 440
        sizey = 238
        posx = 360 #Sets the x position of where on the screen the window will appear
        posy = 50 #Sets the y position of where on the screen the window will appear
        self.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy))
        self.resizable(False, False)

        lblTitle = Label(self, text="Welcome To Your To-Do List", font='Ariel 13 bold')
        lblTitle.place(x=110, y=28)

        btnAddNewTask = Button(self, text="Add New Task", command=self.AddNewTask, cursor='hand2', width=15, font='Ariel 10')
        btnListTasks = Button(self, text="View Tasks", command=self.ListTasks, cursor='hand2', width=15, font='Ariel 10')
        btnReminder = Button(self, text="Reminder", command=self.Reminder)
        btnQuit = Button(self, text="Quit", command=self.destroy, cursor='hand2', font='Ariel 10')

        btnAddNewTask.place(x=160, y=75)
        btnListTasks.place(x=160, y=120)
        btnReminder.place(x=10, y=10)
        btnQuit.place(x=390, y=200)

        self.Reminder()

    def Reminder(self):
        today = datetime.date.today().strftime("%B %d, %Y")
        
        FullTaskList = []
        with open("test.csv", "r") as f:
            for line in f:
                details = line.split(",")
                Task = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9])
                FullTaskList.append(Task)
        for Task in FullTaskList:
            if (str(Task.EndM) + ' ' + Task.EndD + ', ' + Task.EndY) == today and Task.Status != "Completed":
                messagebox.showinfo("Task Due Today", "The %s task is due to be completed today." % Task.TaskName)            

                
    def AddNewTask(self):
        self.NewTaskWin = Toplevel(self)
        self.NewTaskWin.title("Add New Task")
        sizex = 440
        sizey = 250
        posx = 800 #Sets the x position of where on the screen the window will appear
        posy = 200 #Sets the y position of where on the screen the window will appear
        self.NewTaskWin.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy))
        self.NewTaskWin.resizable(False, False)
        
        self.NewTaskWin.entTaskName = StringVar()
        self.NewTaskWin.entTaskDesc = StringVar()
        self.NewTaskWin.status = StringVar()
        self.NewTaskWin.priority = IntVar()
        self.NewTaskWin.StartDay = StringVar()
        self.NewTaskWin.StartMonth = StringVar()
        self.NewTaskWin.MonthList = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        self.NewTaskWin.StartYear = IntVar()
        self.NewTaskWin.EndDay = StringVar()
        self.NewTaskWin.EndMonth = StringVar()
        self.NewTaskWin.EndYear = IntVar()
        
        lblTitle = Label(self.NewTaskWin, text="Please Add a New To-Do Task",font='Ariel 10 bold')
        lblTitle.place(x=140, y=3)
        
        self.NewTaskWin.grid_rowconfigure(0, minsize=35) #This gives row 0 some substance. This is so row 1 is below lblTitle. lblTitle used .place not .grid or it wouldn't be centered
        
        lblTaskName = Label(self.NewTaskWin, text="Task Name:")
        lblTaskName.grid(row=1, column=0)
        entTaskName = Entry(self.NewTaskWin, textvariable=self.NewTaskWin.entTaskName)
        entTaskName.grid(row=1, column=1)
        
        entTaskDesc = Entry(self.NewTaskWin, textvariable=self.NewTaskWin.entTaskDesc)
        lblTaskDesc = Label(self.NewTaskWin, text="Task Description:")
        lblTaskDesc.grid(row=1, column=2)
        entTaskDesc.grid(row=1, column=3)

        self.NewTaskWin.status.set('Not Started')

        lblStatus = Label(self.NewTaskWin, text="Current Status:", pady=10)
        rbStatus1 = Radiobutton(self.NewTaskWin, text="Not Started", variable=self.NewTaskWin.status, value='Not Started')
        rbStatus2 = Radiobutton(self.NewTaskWin, text="In Progress", variable=self.NewTaskWin.status, value='In Progress')
        rbStatus3 = Radiobutton(self.NewTaskWin, text="Completed", variable=self.NewTaskWin.status, value='Completed')
        lblStatus.grid(row=2, column=0)
        rbStatus1.grid(row=2, column=1)
        rbStatus2.grid(row=2, column=2)
        rbStatus3.grid(row=2, column=3)

        self.NewTaskWin.priority.set(3)

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

        self.NewTaskWin.StartDay.set(1)
        self.NewTaskWin.StartMonth.set(self.NewTaskWin.MonthList[0])
        self.NewTaskWin.StartYear.set(2019)
        
        lblStartDate = Label(self.NewTaskWin, text="Start Date:", pady=10)

        cmbxStartDay = OptionMenu(self.NewTaskWin, self.NewTaskWin.StartDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        cmbxStartMonth = OptionMenu(self.NewTaskWin, self.NewTaskWin.StartMonth, *self.NewTaskWin.MonthList)
        cmbxStartYear = OptionMenu(self.NewTaskWin, self.NewTaskWin.StartYear, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034)

        lblStartDate.grid(row=4, column=0)
        cmbxStartDay.grid(row=4, column=1)
        cmbxStartMonth.grid(row=4, column=2)
        cmbxStartYear.grid(row=4, column=3)
        
        self.NewTaskWin.EndDay.set(1)
        self.NewTaskWin.EndMonth.set(self.NewTaskWin.MonthList[0])
        self.NewTaskWin.EndYear.set(2019)
        
        lblEndDate = Label(self.NewTaskWin, text="End Date:", pady=10)

        cmbxEndDay = OptionMenu(self.NewTaskWin, self.NewTaskWin.EndDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        cmbxEndMonth = OptionMenu(self.NewTaskWin, self.NewTaskWin.EndMonth, *self.NewTaskWin.MonthList)
        cmbxEndYear = OptionMenu(self.NewTaskWin, self.NewTaskWin.EndYear, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038)

        lblEndDate.grid(row=5, column=0)
        cmbxEndDay.grid(row=5, column=1)
        cmbxEndMonth.grid(row=5, column=2)
        cmbxEndYear.grid(row=5, column=3)
        
        btnAddTask = Button(self.NewTaskWin, text="Add Task", command=self.WriteNewToFile, cursor='hand2', width=34)
        btnMenu = Button(self.NewTaskWin, text="Return To Menu", command=self.NewTaskWin.destroy, cursor='hand2', width=13)
        
        btnAddTask.place(x=40, y=215)
        btnMenu.place(x=300, y=215)


    def ListTasks(self):
        class Edit():
            def __init__(self, Task, menu):
                self.task = Task
                self.menu = menu

            def __call__(self):
                self.menu.EditTask(self.task)

        class Delete():
            def __init__(self, Task, menu):
                self.task = Task
                self.menu = menu

            def __call__(self):
                self.menu.DeleteTask(self.task)

        self.ListTasksWin = Toplevel(self)
        self.ListTasksWin.title("List All Tasks")
        sizex = 670
        sizey = 250
        posx = 130 #Sets the x position of where on the screen the window will appear
        posy = 320 #Sets the y position of where on the screen the window will appear
        self.ListTasksWin.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy))
        self.ListTasksWin.resizable(False, True)

        lblTitle = Label(self.ListTasksWin, text="All To-Do Tasks",font='Ariel 10 bold')
        lblTitle.grid(row=0, column=3)

        btnReturn = Button(self.ListTasksWin, text="Return To Menu", command=self.ListTasksWin.destroy)
        btnReturn.place(x=560, y=5)

        for i in range(0,6):
            self.ListTasksWin.grid_columnconfigure(i, minsize=90)

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

        FullTaskList = []
        TasksCount = 1
        with open("test.csv", "r") as f:
            for line in f:
                details = line.split(",")
                Task = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9])
                FullTaskList.append(Task)               
        for Task in FullTaskList:
            TasksCount += 1
            lblTaskName = Label(self.ListTasksWin, text=Task.TaskName)
            lblTaskDesc = Label(self.ListTasksWin, text=Task.TaskDesc)
            lblTaskSDate = Label(self.ListTasksWin, text=(Task.StartD + ' ' + Task.StartM + ' ' + Task.StartY))
            lblTaskEDate = Label(self.ListTasksWin, text=(Task.EndD + ' ' + Task.EndM + ' ' + Task.EndY))
            lblTaskStatus = Label(self.ListTasksWin, text=Task.Status)
            lblTaskPriority = Label(self.ListTasksWin, text=Task.Priority)
            btnEdit = Button(self.ListTasksWin, text="Edit", command=Edit(Task, self), cursor='hand2', padx=15)
            btnDelete = Button(self.ListTasksWin, text="Delete", command=Delete(Task, self), cursor='hand2')

            lblTaskName.grid(row=TasksCount, column=0)
            lblTaskDesc.grid(row=TasksCount, column=1)
            lblTaskSDate.grid(row=TasksCount, column=2)
            lblTaskEDate.grid(row=TasksCount, column=3)
            lblTaskStatus.grid(row=TasksCount, column=4)
            lblTaskPriority.grid(row=TasksCount, column=5)
            btnEdit.grid(row=TasksCount, column=6)
            btnDelete.grid(row=TasksCount, column=7)


    def DeleteTask(self, Task):
        msgboxDelete = messagebox.askquestion ('Delete Task?','Are you sure you want to delete this task',icon = 'warning')
        if msgboxDelete == 'yes':
            with open('test.csv', 'r') as f:
                FullTaskList = []
                total = 0 #This creates a variable of 'total', with a value of 0. It will be used to check when the list has ended.
                num_lines = 0 #This creates a variable of 'num_lines' with a value of 0. It  will be used to check when the list has ended.  
                for line in f:
                    details = line.split(",")
                    SavedTask = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9])
                    FullTaskList.append(SavedTask)
                    num_lines += 1 #For every line in the database, the value of num_lines increases by one. This counts the total number of lines (and by extension, tasks) in the database.

            for SavedTask in FullTaskList:
                if SavedTask.TaskName == Task.TaskName and SavedTask.TaskDesc == Task.TaskDesc and SavedTask.Status == Task.Status and SavedTask.Priority == Task.Priority and SavedTask.StartD == Task.StartD and SavedTask.StartM == Task.StartM and SavedTask.StartY == Task.StartY and SavedTask.EndD == Task.EndD and SavedTask.EndM == Task.EndM and SavedTask.EndY == Task.EndY:
                    FullTaskList.remove(SavedTask)
                    with open('test.csv', 'w') as f:
                        for task in FullTaskList:
                            f.write(SavedTask.TaskName + ',' + SavedTask.TaskDesc + ',' + SavedTask.Status + ',' + str(SavedTask.Priority) + ',' + str(SavedTask.StartD) + ',' + str(SavedTask.StartM) + ',' + str(SavedTask.StartY) + ',' + str(SavedTask.EndD) + ',' + str(SavedTask.EndM) + ',' + str(SavedTask.EndY) + ', \n')
           
            self.ListTasksWin.withdraw()
            self.ListTasks()


    def EditTask(self, Task):

        class Rewrite():
            def __init__(self, Task, menu):
                self.task = Task
                self.menu = menu

            def __call__(self):
                self.menu.RewriteToFile(self.task)
        
        self.EditTaskWin = Toplevel(self)
        self.EditTaskWin.title("Edit Task")
        sizex = 440
        sizey = 250
        posx = 800 #Sets the x position of where on the screen the window will appear
        posy = 450 #Sets the y position of where on the screen the window will appear
        self.EditTaskWin.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy))
        self.EditTaskWin.resizable(False, False)


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

        cmbxStartDay = OptionMenu(self.EditTaskWin, self.EditTaskWin.StartDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        cmbxStartMonth = OptionMenu(self.EditTaskWin, self.EditTaskWin.StartMonth, *self.EditTaskWin.MonthList)
        cmbxStartYear = OptionMenu(self.EditTaskWin, self.EditTaskWin.StartYear, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034)

        lblStartDate.grid(row=4, column=0)
        cmbxStartDay.grid(row=4, column=1)
        cmbxStartMonth.grid(row=4, column=2)
        cmbxStartYear.grid(row=4, column=3)
        
        lblEndDate = Label(self.EditTaskWin, text="End Date:", pady=10)

        cmbxEndDay = OptionMenu(self.EditTaskWin, self.EditTaskWin.EndDay, '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        cmbxEndMonth = OptionMenu(self.EditTaskWin, self.EditTaskWin.EndMonth, *self.EditTaskWin.MonthList)
        cmbxEndYear = OptionMenu(self.EditTaskWin, self.EditTaskWin.EndYear, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038)

        lblEndDate.grid(row=5, column=0)
        cmbxEndDay.grid(row=5, column=1)
        cmbxEndMonth.grid(row=5, column=2)
        cmbxEndYear.grid(row=5, column=3)
        
        btnAddTask = Button(self.EditTaskWin, text="Save Changes", command=Rewrite(Task, self), cursor='hand2', width=34)
        btnMenu = Button(self.EditTaskWin, text="Cancel", command=self.EditTaskWin.destroy, cursor='hand2', width=13)
        
        btnAddTask.place(x=40, y=215)
        btnMenu.place(x=300, y=215)
        

    def WriteNewToFile(self): 
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

        if TaskName == '' or TaskDesc == '':
            messagebox.showerror("Error", "All fields must have values in order to save this task.")            
        elif StartY > EndY:
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif (StartM == "April" or StartM == "June" or StartM == "September" or StartM == "November") and (int(StartD) >=30):
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif StartM == "February" and int(StartD) >=28:
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif (EndM == "April" or EndM == "June" or EndM == "September" or EndM == "November") and (int(EndD) >=30):
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")
        elif EndM == "February" and int(EndD) >=28:
            messagebox.showerror("Error", "Please ensure valid dates have been entered.")        
        else:
            self.NewTaskWin.destroy()
            messagebox.showinfo("Success", "Task Added Successfully")
            NewTask = ToDoTask(TaskName, TaskDesc, Status, Priority, StartD, StartM, StartY, EndD, EndM, EndY)
            with open('test.csv', 'a') as f:
                f.write(NewTask.TaskName + ',' + NewTask.TaskDesc + ',' + NewTask.Status + ',' + str(NewTask.Priority) + ',' + str(NewTask.StartD) + ',' + str(NewTask.StartM) + ',' + str(NewTask.StartY) + ',' + str(NewTask.EndD) + ',' + str(NewTask.EndM) + ',' + str(NewTask.EndY) + ', \n')
                self.AddNewTask()
                
            try:
                if 'normal' == self.ListTasksWin.state():
                    self.ListTasksWin.destroy()
                    self.ListTasks()
            except: 
                pass


    def RewriteToFile(self, Task):
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

        NewTask = ToDoTask(NewTaskName, NewTaskDesc, NewStatus, NewPriority, NewStartD, NewStartM, NewStartY, NewEndD, NewEndM, NewEndY)

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
        else:
            with open('test.csv', 'r') as f:
                FullTaskList = []
                total = 0 #This creates a variable of 'total', with a value of 0. It will be used to check when the list has ended.
                num_lines = 0 #This creates a variable of 'num_lines' with a value of 0. It  will be used to check when the list has ended.  
                for line in f:
                    details = line.split(",")
                    SavedTask = ToDoTask(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7], details[8], details[9])
                    FullTaskList.append(SavedTask)
                    num_lines += 1 #For every line in the database, the value of num_lines increases by one. This counts the total number of lines (and by extension, tasks) in the database.

            for SavedTask in FullTaskList:
                if SavedTask.TaskName == Task.TaskName:# and SavedTask.TaskDesc == Task.TaskDesc and SavedTask.Status == Task.Status and SavedTask.Priority == Task.Priority and SavedTask.StartD == Task.StartD and SavedTask.StartM == Task.StartM and SavedTask.StartY == Task.StartY and SavedTask.EndD == Task.EndD and SavedTask.EndM == Task.EndM and SavedTask.EndY == Task.EndY:
                    FullTaskList.remove(SavedTask)
                    FullTaskList.append(NewTask)
                    with open('test.csv', 'w') as f:
                        for SavedTask in FullTaskList:
                            f.write(SavedTask.TaskName + ',' + SavedTask.TaskDesc + ',' + SavedTask.Status + ',' + str(SavedTask.Priority) + ',' + str(SavedTask.StartD) + ',' + str(SavedTask.StartM) + ',' + str(SavedTask.StartY) + ',' + str(SavedTask.EndD) + ',' + str(SavedTask.EndM) + ',' + str(SavedTask.EndY) + ', \n')

            self.EditTaskWin.destroy()
            self.ListTasksWin.destroy()
            self.ListTasks()


app = Menu()
app.mainloop()
