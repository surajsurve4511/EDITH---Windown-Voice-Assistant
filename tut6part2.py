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

            self.btn_snapshot = tkinter.Button(bthn_frame,text="Snapshot", width=20, bg="black", fg="white")
            self.btn_snapshot.pack(side="left,padx=10,pady=10)

         def snapshot(self):
             ret, frame = self.vid.get_frame()
             if ret:
                 cv2.imwrite ("My Caputre
        







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
                 return
                 
