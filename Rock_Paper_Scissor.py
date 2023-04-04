from tkinter import *
import random

#to create the window
root2=Tk()
root2.title("Rock Paper Scissor")
root2.geometry("615x500")
root2.configure(bg="yellow")

#label for title
label1=Label(root2,text="Rock Paper Scissor ",fg='navy blue',bg="yellow",font=('Arial',20))
label1.grid(row=0,column=0,padx=5,pady=15)

#label for user's turn
label3=Label(root2,text="Your turn: ",fg='black',bg="yellow",font=('Arial italic',12))
label3.grid(row=2,column=0,padx=5,pady=15)

#to store your choice
user=StringVar()

#creating text box to accept your choice
tbox1=Entry(root2,textvariable=user,fg='black',font=('Arial',12))
tbox1.grid(row=2,column=1)


list1=['Rock','Paper','Scissor']

#function for playing the game
def play():
    comp_pt=0
    user_pt=0
    comp=random.choice(list1)
    if user.get().capitalize()==comp:
     emptylabel3.config(text=f"Computer selected: {comp}")
     emptylabel1.config(text=f"Your score: {user_pt}")
     emptylabel2.config(text=f"Computer's score: {comp_pt}")
    else:
      if(user.get().capitalize()=='Rock' and comp=='Paper'):
           comp_pt=comp_pt+1
           emptylabel3.config(text=f"Computer selected: {comp}")
           emptylabel1.config(text=f"Your score: {user_pt}")
           emptylabel2.config(text=f"Computer's score: {comp_pt}")
      elif(user.get().capitalize()=='Rock' and comp=='Scissor'):
           user_pt=user_pt+1
           emptylabel3.config(text=f"Computer selected: {comp}")
           emptylabel1.config(text=f"Your score: {user_pt}")
           emptylabel2.config(text=f"Computer's score: {comp_pt}")
      elif(user.get().capitalize()=='Paper' and comp=='Rock'):
           user_pt=user_pt+1
           emptylabel3.config(text=f"Computer selected: {comp}")
           emptylabel1.config(text=f"Your score: {user_pt}")
           emptylabel2.config(text=f"Computer's score: {comp_pt}")
      elif(user.get().capitalize()=='Paper' and comp=='Scissor'):
           comp_pt=comp_pt+1
           emptylabel3.config(text=f"Computer selected: {comp}")
           emptylabel1.config(text=f"Your score: {user_pt}")
           emptylabel2.config(text=f"Computer's score: {comp_pt}")
      elif(user.get().capitalize()=='Paper' and comp=='Scissor'):
           comp_pt=comp_pt+1
           emptylabel3.config(text=f"Computer selected: {comp}")
           emptylabel1.config(text=f"Your score: {user_pt}")
           emptylabel2.config(text=f"Computer's score: {comp_pt}")
      elif(user.get().capitalize()=='Scissor' and comp=='Rock'):
           comp_pt=comp_pt+1
           emptylabel3.config(text=f"Computer selected: {comp}")
           emptylabel1.config(text=f"Your score: {user_pt}")
           emptylabel2.config(text=f"Computer's score: {comp_pt}")
      elif(user.get().capitalize()=='Scissor' and comp=='Paper'):
           user_pt=user_pt+1
           emptylabel3.config(text=f"Computer selected: {comp}")
           emptylabel1.config(text=f"Your score: {user_pt}")
           emptylabel2.config(text=f"Computer's score: {comp_pt}")
    if(user_pt>comp_pt):
        emptylabel4.config(text="Bravo!You won :)")
    elif(user_pt<comp_pt):
         emptylabel4.config(text="Computer won.Better luck next time")
    else:
        emptylabel4.config(text="It's a draw.Play again and become the winner :)")

#function to exit the game
def exit():
    root2.destroy()

#function to reset user's choice    
def reset():
    user.set("") 
    emptylabel3.config(text=" ")
    emptylabel1.config(text=" ")
    emptylabel2.config(text=" ")

#creating the play button
button1=Button(root2,command=play,text='Play',fg='white',bg='navy blue',font=('Arial bold',12))
button1.grid(row=3,column=1)

#creating the exit button
button1=Button(root2,command=exit,text='Exit',fg='white',bg='navy blue',font=('Arial bold',12))
button1.grid(row=0,column=3)

#creating the reset button
button1=Button(root2,command=reset,text='Reset',fg='white',bg='navy blue',font=('Arial bold',12))
button1.grid(row=0,column=5)


#creating an empty label to display user score
emptylabel1=Label(root2,fg='black',bg="yellow",font=('Arial italic',12))
emptylabel1.grid(row=5,column=0,pady=15)

#creating an empty label to display computer's score
emptylabel2=Label(root2,fg='black',bg="yellow",font=('Arial italic',12))
emptylabel2.grid(row=5,column=1,pady=15)


#creating an empty label to display computer's choice
emptylabel3=Label(root2,fg='black',bg="yellow",font=('Arial italic',12))
emptylabel3.grid(row=4,column=0,pady=15)


#creating an empty label to display result
emptylabel4=Label(root2,fg='red',bg="yellow",font=('Georgia bold',15))
emptylabel4.grid(row=6,column=0,pady=20,padx=100)



root2.mainloop()


