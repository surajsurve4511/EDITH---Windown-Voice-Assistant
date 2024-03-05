def cam() :
    import tkinter
    from tkinter import messagebox
    import PIL.Image, PIL.ImageTk
    import time

    class App:
        def _init_(self,window, window_title, video_source=0)
            self.window = window
            self.window.title = (window_title)
            self.video_source = video_source

            self.vid = HyVideoCapture(self.video_source)
            self.canvas = tkinter.Canvas(window, height=self.vid.height, width=self,vid,width)
            self.canvas.pack()

            btn_frame = tkinter.Frame(window, background="Black")
            btn_frame.place(x=0,y=0)

            self.btn_snapshot = tkinter.Button(btn_frame,text="Snapshot", width=20, bg="black", fg="white")
            self.btn_snapshot.pack(side="left",padx=10,pady=10)

            self delay = 15
            self.update()


            self.window.mainloop()

         def snapshot(self):
             ret, frame = self.vid.get_frame()
             if ret:
                 cv2.imwrite ("My Capture "+ time.strftime("%d-%m-%Y-%H-%m-%s")+", jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
                 messagebox.shoeinfo("Notification","Image Saved")
        
         def update(self):
             ret, frame =self.vid.get_frame()

             if ret:
                 self.photo = PIL.Image.Tk.PhotoImage(image=PIL.image.freaquency((frame))
                 self.canvas.create_image(0,0, iamge=self,photo, anchor=tkinter.NW)

                 self.window.after(self.delay,self.update)






     class MyVideoCapture:
         def _init_(self, video_source=0)
             self.vid = cv2.VideoCapture(video_source)
             if not self.vid.isOpened():
                raiseValueError("Unable to open video Source", video_source)

             self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
             self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        defget_frame(self):
             if self.vid.isOpened() :
                ret, frame = self.vid.read()
                if ret:
                    return(ret, cv2.cvtColor(frame, cv2.COLOR_BGR@RGB))
                else:
                    return(ret, None)
             else: 
                 return(ret,None)

      App(tkinter.Tk(),"Camera")

                 
