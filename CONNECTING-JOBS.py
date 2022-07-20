from tkinter import * 
root = Tk()
import random
root.title("CONNECTING-JOBS")
root.geometry("900x500")

doctor_label = Label(root)
doctor_label.place(relx=0.2,rely=0.3, anchor= CENTER)

softwareEngineer_label = Label(root)
softwareEngineer_label.place(relx=0.2,rely=0.5, anchor= CENTER)

chemicalEngineer_label = Label(root)
chemicalEngineer_label.place(relx=0.2,rely=0.7, anchor= CENTER)

def doctor():
    hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
    random_hospital = random.randint(0,3)
    doctor_list = ["Bob","Michel","Shivvesh", "Hashil"]
    random_doctor = random.randint(0,3)
    doctor_label["text"] = doctor_list[random_doctor] + " has been alloted to " + hospital_list[random_hospital]
    
def softwareEngineer():
    companies_list = ["Microsoft", "Oracle", "SAP", "Adobe"]
    random_companies = random.randint(0,3)
    softwareEngineer_list = ["Bob","Michel","Manna", "Hashil"]
    random_softwareEngineer = random.randint(0,3)
    softwareEngineer_label["text"] = softwareEngineer_list[random_softwareEngineer] + " has been alloted to " + companies_list[random_companies]
    
def chemicalEngineer():
    companies_list = ["BASF", "DowDuPont", "SABIC", "Formosa Plastics"]
    random_companies = random.randint(0,3)
    chemicalEngineer_list = ["Bob","Shivvesh","Manna", "Hashil"]
    random_chemicalEngineer = random.randint(0,3)
    chemicalEngineer_label["text"] = chemicalEngineer_list[random_chemicalEngineer] + " has been alloted to " + companies_list[random_companies]
    
    
    
btn_doctor = Button(root, text="Show the hospital alloted", command= doctor)
btn_doctor.place(relx=0.2, rely=0.2,anchor=CENTER)

btn_softwareEngineer = Button(root, text="Show the company alloted", command= softwareEngineer)
btn_softwareEngineer.place(relx=0.2, rely=0.4,anchor=CENTER)

btn_chemicalEngineer = Button(root, text="Show the company alloted", command= chemicalEngineer)
btn_chemicalEngineer.place(relx=0.2, rely=0.6,anchor=CENTER)

root.mainloop()
                