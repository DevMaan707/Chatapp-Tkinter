import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import customtkinter as ttkk
import socket
import json
import threading

from PIL import Image,ImageTk


class first_window:


    def submit(self,instance_second_window,client_socket):

        info=(self.name_entry.get(),self.rollnumber_entry.get())
        print(type(self.name_entry.get()),type(self.rollnumber_entry.get()))
        print(info)
        jsonified_data=json.dumps(info)
        client_socket.send(jsonified_data.encode('utf-8'))
        instance_second_window.main(info,client_socket)
        #self.window.destroy()
        


    def __init__(self,instan,client_socket):
        #creating the main window
        self.window=ttk.Window()
        self.window.title('ZenTalk')
        self.window.geometry("1000x800")

        self.window.configure(bg="#E7ECF2")

        #to update the dimensions of the window
        self.window.update_idletasks()



        ttkk.set_default_color_theme("dark-blue")
        #creating blue frame

        blue_frame= ttkk.CTkFrame(master=self.window ,
                                  width=self.window.winfo_width(),
                                  fg_color="#71AFE2",
                                  bg_color="#71AFE2")
        blue_frame.place(relx=0,
                         rely=0,
                         relwidth=1,
                         relheight=0.3)

        #creating the main frame 
        frame=ttkk.CTkFrame(master=self.window,
                            width=self.window.winfo_width()*0.8,
                            height=self.window.winfo_height()*0.9,
                            fg_color="white")
        
        
        #placing the frame 
        frame.place(relx=0.15,
                    rely=0.15,
                    relwidth=0.7,
                    relheight=0.7)

        #creating the welcome label
        welcome=ttkk.CTkLabel(master=frame,
                            text="Welcome!",
                            font=('Arial',34,"bold"),
                            )

        #welcome.configure('Arial',34,'bold')

        #placing label
        welcome.place(relx=0.13,
                    rely=0.13)

        #creating the get started label
        get_started=ttkk.CTkLabel(master=frame,text="Fill out your details to get started",
                                  font=('Arial',14),
                                  text_color="grey",
                                  fg_color="transparent")
        
        get_started.place(relx=0.34,rely=0.26)


        #creating the name label
        name=ttkk.CTkLabel(master=frame,
                        text='Name',
                        font=('Arial',18))


        #placing label
        name.place(relx=0.2,
                rely=0.4)

        #name entry field
        self.name_entry=ttkk.CTkEntry(master=frame ,
                                placeholder_text='Enter your Name')

        #placing entryfield
        self.name_entry.place(relx=0.4,
                        rely=0.4)

        #creating the rollnumber label
        rollnumber=ttkk.CTkLabel(master=frame,
                                text="Roll Number",
                                font=('Arial',18))


        #placing label
        rollnumber.place(relx=0.2,
                        rely=0.49)

        #rollNumber entry field
        self.rollnumber_entry=ttkk.CTkEntry(master=frame,
                                    placeholder_text='Enter your RollNumber')


        #placing entryfield
        self.rollnumber_entry.place(relx=0.4,
                            rely=0.49)


        #creating the join button
        join=ttkk.CTkButton(master=frame,text="Join Now",command=lambda:self.submit(instan,client_socket))

        #placing button
        join.place(relx=0.4,
                rely=0.61)
        
        disc=ttkk.CTkLabel(master=frame,text="This is beta version made in 2 days please keep that in mind before commenting on the UI.",
                                  font=('Arial',14),
                                  text_color="grey",
                                  fg_color="transparent")
        
        disc.place(relx=0.09,rely=0.86)

        self.window.mainloop()

class second_window:
    frames_counter=0
    frames_dict={}

    def main_frames(self,name_of_chat,client_socket):
        self.default_button.configure(fg_color="#00aaff",
                                        text_color="white",
                                        hover_color="#00aaff")
        if name_of_chat in second_window.frames_dict:
            pass
        else:
            self.new_frame(name_of_chat,client_socket)


    def senddata(self,name_,text,client_socket):
        #print("yo")
        client_socket.send(json.dumps((name_,text)).encode('utf-8'))

        text_frame=ttkk.CTkFrame(master=self.real_chatbox,
                            fg_color="#a8a8b0")

        text_frame.pack(fill='x')


        bubbly_frame=ttkk.CTkFrame(master=text_frame,
                                   fg_color='blue'
                                   )
        bubbly_frame.pack(side='left')
        text_label = ttkk.CTkLabel(master=bubbly_frame,text=text)

        text_label.pack(padx=15,pady=5)


    def addtext(self,recv_data):
        text_frame=ttkk.CTkFrame(master=self.real_chatbox,
                                 width=self.new_frame_.winfo_width(),
                                 fg_color="#bdbdc6")
        
        print(f"RECEIVED DATA IS {recv_data}")
        
        text_frame.pack(fill='x')
        recv_data=json.loads(recv_data)
        x=recv_data[1]
        print(f"X is {x}")

        bubbly_frame=ttkk.CTkFrame(master=text_frame
                                   )
        bubbly_frame.pack()
        text=ttkk.CTkLabel(master=bubbly_frame,
                           text=x)
        text.pack(padx=15,pady=5)

        

    def main(self,info,client_socket):
        

        self.window=ttk.Window()
        self.window.title('ZenTalk')
        self.window.geometry("1000x800")

        #to update the dimensions of the window
        self.window.update_idletasks()


        #creating two frames
        frame_contacts=ttkk.CTkFrame(master=self.window,
                                    width=self.window.winfo_width()*0.35,
                                    height=self.window.winfo_height(),
                                    fg_color="transparent")

        #placing the frame
        frame_contacts.place(relwidth=0.35,
                            relheight=1)
        


        #creating profilebar
        frame_chatbox_bar=ttkk.CTkFrame(master=frame_contacts,
                                        width=frame_contacts.winfo_width(),
                                        height=frame_contacts.winfo_height()*0.3,
                                        fg_color="#11364b",
                                        corner_radius=0)

        
        #placing the bar
        frame_chatbox_bar.place(relwidth=1,
                                relheight=0.07)


        #seperator
        seperator=ttk.Separator(frame_contacts,
                                orient='horizontal')

        seperator.place(rely=0.069,
                        relwidth=1)


        #creating searchbox frame
        searchbox_frame=ttkk.CTkFrame(master=frame_contacts,
                                      fg_color="white")

        #placing the searchbox frame
        searchbox_frame.place(rely=0.09,
                            relwidth=1,
                            relheight=0.1,
                            )

        #seaechbox label
#        searchbox_label=ttkk.CTkLabel(master=searchbox_frame,
#                                    text="Search",
#                                    font=('Arial',16),
#                                    fg_color="transparent")

        #placing the label
#        searchbox_label.place(relx=0)

        #search entry
        searchbox=ttkk.CTkEntry(master=searchbox_frame,
                                placeholder_text='Search',
                                corner_radius=10
                                )

        #search entry place
        searchbox.place(relx=0.04,
                        relwidth=0.9
                        )
        
        all_chat_label=ttkk.CTkLabel(master=searchbox_frame ,
                                     text='All chats',
                                     font=('Arial',13,"bold"),
                                     text_color="blue",
                                     fg_color="transparent")
        
        all_chat_label.place(relx=0.41,
                             rely=0.58)
        seperator_indicator=ttk.Separator(master=searchbox_frame,
                                          orient='horizontal',
                                          )
        seperator_indicator.place(relx=0.39,
                                  rely=0.95,
                                  relwidth=0.18)
        #search button
#        searchbutton=ttkk.CTkButton(master=searchbox_frame)

        #search button place
#        searchbutton.place()


        #seperator
#        seperator=ttk.Separator(frame_contacts,
#                                orient='horizontal')

#        seperator.place(rely=0.1,
#                        relwidth=1)

        #group chat frame
        default_frame=ttkk.CTkFrame(master=frame_contacts,
                                    fg_color="white"
                                    )


        #placement of groupchat frame
        default_frame.place(rely=0.201,
                            relwidth=1,
                            relheight=0.8)

        #groupchat button
        self.default_button=ttkk.CTkButton(master=default_frame,
                                    corner_radius=4,
                                    fg_color='transparent',
                                    hover_color='#F0F2F5',
                                    text='Group Chat',
                                    anchor='w',
                                    text_color='black',
                                    width=default_frame.winfo_width(),
                                    height=80,
                                    font=('Arial',18),
                                    command=lambda:self.main_frames(self.default_button.cget("text"),client_socket))

        #placement of button
        self.default_button.pack(fill='x')


        #creating chatbox frame
        #frame_chatbox=ttkk.CTkFrame(master=self.window)

        self.window.mainloop()



    #defining the functions
    def new_frame(self,name_,client_socket):

        #image_=Image.open('chat_bck.png')
        #background_image = ImageTk.PhotoImage(image_)




        self.new_frame_ = ttkk.CTkFrame(master=self.window)
        self.new_frame_.place(relx=0.35,
                        relwidth=1,
                        relheight=1)

        self.chat_bar=ttkk.CTkFrame(master=self.new_frame_,
                                    fg_color="white")

        self.chat_bar.place(relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=0.07)
        
        self.real_chatbox=ttkk.CTkFrame(master=self.new_frame_
                                        )


        self.real_chatbox.place(rely=0.07,
                                relx=0,
                                relwidth=1,
                                relheight=1)
        
        #self.pic_label=ttkk.CTkLabel(master=self.real_chatbox,
        #                             image=background_image)
        
        #self.pic_label.place(relwidth=1,
        #                     relheight=1,
        #                     relx=0,
        #                     rely=0)

                                
        text_entry=ttkk.CTkEntry(master=self.real_chatbox,
                                )

        text_entry.place(relx=0.04,
                        rely=0.87,
                        relwidth=0.54,
                        relheight=0.04)
        

        send_btn=ttkk.CTkButton(master=self.real_chatbox,
                                text='Send',
                                command=lambda: self.senddata(name_,text_entry.get(),client_socket))
        send_btn.place(relx=0.59,
                    rely=0.87,
                    relwidth=0.04,
                    relheight=0.04)
    

def handle_messages(self,client_socket):
    while True:
        res=client_socket.recv(1024).decode('utf-8')
        print(f"RES RECEIVED IS {res}")
        self.addtext(res)

def main():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_address=('127.0.0.1',3001)
    client_socket.connect(server_address)
    sec=second_window()


    receiver=threading.Thread(target=handle_messages,args=(sec,client_socket,))
    receiver.start()
    
    run=first_window(sec,client_socket)

if __name__=="__main__":
    main()