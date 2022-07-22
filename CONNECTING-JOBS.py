from tkinter import * 
root = Tk()
import random
from PIL import ImageTk, Image
root.title("CONNECTING-JOBS")
root.geometry("900x500")
picture = ImageTk.PhotoImage(Image.open("Image6.png"))

Image=Label(root)
Image["image"]=picture
Image.place(relx=0.8,rely=0.5, anchor= CENTER)
#-----------------------HEading-------
heading = Label(root, text = "Assigning Jobs", font = ("Comic Sans MS", 15))
heading.place(relx = 0.1, rely = 0.06, anchor = CENTER)
#-------textbox-----------------------
entry_doctor = Entry(root)
entry_doctor.place(relx=0.3, rely=0.2,anchor=CENTER)
#-------doctor label-------------
doctor_heading_label = Label(root, text = "Doctor:")
doctor_heading_label.place(relx = 0.04, rely = 0.2, anchor = CENTER)
#-------------Display------------
doctor_label = Label(root, font = ("Comic Sans MS", 8), fg = "darkgreen")
doctor_label.place(relx=0.11,rely=0.3, anchor= CENTER)
#-----------End of Doctor-------------
#-------------softwareEngineer label------------
softwareEngineer_heading_label = Label(root, text = "SoftwareEngineer:")
softwareEngineer_heading_label.place(relx = 0.07, rely = 0.35, anchor = CENTER)
#-------------softwareEngineer textbox--------
entry_softwareEngineer = Entry(root)
entry_softwareEngineer.place(relx=0.3, rely=0.35,anchor=CENTER)
#----------------DisplayLabel-----------------
softwareEngineer_label = Label(root, font = ("Comic Sans MS", 8), fg = "darkgreen")
softwareEngineer_label.place(relx=0.11,rely=0.45, anchor= CENTER)
#-----------End of softwareEngineer-----------
#------------chemicalEngineer label-----------
chemicalEngineer_heading_label = Label(root, text = "ChemicalEngineer:")
chemicalEngineer_heading_label.place(relx = 0.07, rely = 0.5, anchor = CENTER)
#------------chemicalEngineer texbox------------
entry_chemicalEngineer = Entry(root)
entry_chemicalEngineer.place(relx=0.3, rely=0.5,anchor=CENTER)
#------------DisplayLabel-----------------------
chemicalEngineer_label = Label(root, font = ("Comic Sans MS", 8), fg = "darkgreen")
chemicalEngineer_label.place(relx=0.11,rely=0.6, anchor= CENTER)



def doctor():
    hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
    random_hospital = random.randint(0,3)
    doctor_name = entry_doctor.get()
    doctor_label["text"] = doctor_name + " has been alloted to " + hospital_list[random_hospital]
    
def softwareEngineer():
    companies_list = ["Microsoft", "Oracle", "SAP", "Adobe"]
    random_companies = random.randint(0,3)
    softwareEngineer_name = entry_softwareEngineer.get()
    softwareEngineer_label["text"] =  softwareEngineer_name + " has been alloted to " + companies_list[random_companies]
    
def chemicalEngineer():
    companies_list = ["BASF", "DowDuPont", "SABIC", "Formosa Plastics"]
    random_companies = random.randint(0,3)
    chemicalEngineer_name = entry_chemicalEngineer.get()
    chemicalEngineer_label["text"] =  chemicalEngineer_name + " has been alloted to " + companies_list[random_companies]
    
    
    
btn_doctor = Button(root, text="Show the hospital alloted", command= doctor, fg = "White", bg = "blue", relief = FLAT)
btn_doctor.place(relx=0.09, rely=0.25,anchor=CENTER)

btn_softwareEngineer = Button(root, text="Show the company alloted", command= softwareEngineer, fg = "White", bg = "blue", relief = FLAT)
btn_softwareEngineer.place(relx=0.097, rely=0.4,anchor=CENTER)

btn_chemicalEngineer = Button(root, text="Show the company alloted", command= chemicalEngineer, fg = "White", bg = "blue", relief = FLAT)
btn_chemicalEngineer.place(relx=0.09, rely=0.55,anchor=CENTER)

root.mainloop()
                