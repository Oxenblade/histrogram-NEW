from tkinter import *

class HistrogramApp:

    def __init__(self):
        self.root= Tk()

    def setup_window(self):
        
        self.root.title("Traffic data on Histogram")
        self.root.iconbitmap("C:/Users/hp/Downloads/traffic data/statistic_9684905.ico")
        self.root.geometry("1350x700")
        self.canvas= Canvas(self.root, width=1300, height=600, bg= "#F4F8D3")
        self.canvas.grid(row = 5, column = 1,padx =20, pady = 20)
        
    def draw_histogram(self):
        
        self.label = Label(self.root, text = " **Histogram of Vechicle Frequency per Hour(15/06/2024)**")
        self.label.config(font = ("Helvetica", 12, "bold"),anchor= W)
        self.label.grid(row = 4, column =1, pady=10,)

        #create line
        #my_canvas.create_line(x1, y1,x2,y2, fill="color")
        self.canvas.create_line(0,550,1210,550, fill="black")
        self.canvas.create_line(10,100,10,550, fill="black")
        self.canvas.create_text( 585, 580 , text = "00:00 to 24:00 Hours", fill="black")

        #create text ( x axis = numbers hours)

        self.canvas.create_text( 35, 560 , text = "00", fill="black")
        self.canvas.create_text( 85, 560 , text = "01", fill="black")
        self.canvas.create_text( 135, 560 , text = "02", fill="black")
        self.canvas.create_text( 185, 560 , text = "03", fill="black")
        self.canvas.create_text( 235, 560 , text = "04", fill="black")
        self.canvas.create_text( 285, 560 , text = "05", fill="black")
        self.canvas.create_text( 335, 560 , text = "06", fill="black")
        self.canvas.create_text( 385, 560 , text = "07", fill="black")
        self.canvas.create_text( 435, 560 , text = "08", fill="black")
        self.canvas.create_text( 485, 560 , text = "09", fill="black")
        self.canvas.create_text( 535, 560 , text = "10", fill="black")
        self.canvas.create_text( 585, 560 , text = "11", fill="black")
        self.canvas.create_text( 635, 560 , text = "12", fill="black")
        self.canvas.create_text( 685, 560 , text = "13", fill="black")
        self.canvas.create_text( 735, 560 , text = "14", fill="black")
        self.canvas.create_text( 785, 560 , text = "15", fill="black")
        self.canvas.create_text( 835, 560 , text = "16", fill="black")
        self.canvas.create_text( 885, 560 , text = "17", fill="black")
        self.canvas.create_text( 935, 560 , text = "18", fill="black")
        self.canvas.create_text( 985, 560 , text = "19", fill="black")
        self.canvas.create_text( 1035, 560 , text = "20", fill="black")
        self.canvas.create_text( 1085, 560 , text = "21", fill="black")
        self.canvas.create_text( 1135, 560 , text = "22", fill="black")
        self.canvas.create_text( 1185, 560 , text = "23", fill="black")


        #my_canvas.create_rectangle(x1,y1,x2,y2, fil="color")
        
        #self.canvas.create_rectangle(15,550,35,300, fill="red")
        self.canvas.create_rectangle(35,550,55,525, fill="green")
        #self.canvas.create_rectangle(65,550,85,150, fill="red")
        self.canvas.create_rectangle(85,550,105,225, fill="green")
        #self.canvas.create_rectangle(115,550,135,175, fill="red")
        self.canvas.create_rectangle(135,550,155,450, fill="green")
        
        #self.canvas.create_rectangle(165,550,185,300, fill="red")
        self.canvas.create_rectangle(185,550,205,525, fill="green")
        #self.canvas.create_rectangle(215,550,235,300, fill="red")
        self.canvas.create_rectangle(235,550,255,375, fill="green")

        #self.canvas.create_rectangle(265,550,285,300, fill="red")
        self.canvas.create_rectangle(285,550,305,525, fill="green")
        #self.canvas.create_rectangle(315,550,335,300, fill="red")
        self.canvas.create_rectangle(335,550,355,525, fill="green")
        #self.canvas.create_rectangle(365,550,385,300, fill="red")

        self.canvas.create_rectangle(385,550,405,505, fill="green")
        #self.canvas.create_rectangle(415,550,435,300, fill="red")
        self.canvas.create_rectangle(435,550,455,100, fill="green")
        #self.canvas.create_rectangle(465,550,485,300, fill="red")
        self.canvas.create_rectangle(485,550,505,200, fill="green")

        #self.canvas.create_rectangle(515,550,535,300, fill="red")
        self.canvas.create_rectangle(535,550,555,200, fill="green")
        #self.canvas.create_rectangle(565,550,585,300, fill="red")
        self.canvas.create_rectangle(585,550,605,300, fill="green")
        #self.canvas.create_rectangle(615,550,635,300, fill="red")
        
        self.canvas.create_rectangle(635,550,655,202, fill="green")
        self.canvas.create_rectangle(665,550,685,300, fill="red")
        self.canvas.create_rectangle(685,550,705,202, fill="green")
        self.canvas.create_rectangle(715,550,735,300, fill="red")
        self.canvas.create_rectangle(735,550,755,203, fill="green")
        
        self.canvas.create_rectangle(765,550,785,300, fill="red")
        self.canvas.create_rectangle(785,550,805,201, fill="green")
        self.canvas.create_rectangle(815,550,835,300, fill="red")
        self.canvas.create_rectangle(835,550,855,202, fill="green")

        self.canvas.create_rectangle(865,550,885,300, fill="red")
        self.canvas.create_rectangle(885,550,905,202, fill="green")
        self.canvas.create_rectangle(915,550,935,300, fill="red")
        self.canvas.create_rectangle(935,550,955,203, fill="green")
        self.canvas.create_rectangle(965,550,985,300, fill="red")

        self.canvas.create_rectangle(985,550,1005,202, fill="green")
        self.canvas.create_rectangle(1015,550,1035,300, fill="red")
        self.canvas.create_rectangle(1035,550,1055,203, fill="green")
        self.canvas.create_rectangle(1065,550,1085,300, fill="red")
        self.canvas.create_rectangle(1085,550,1105,202, fill="green")

        self.canvas.create_rectangle(1115,550,1135,300, fill="red")
        self.canvas.create_rectangle(1135,550,1155,201, fill="green")
        self.canvas.create_rectangle(1165,550,1185,300, fill="red")
        self.canvas.create_rectangle(1185,550,1205,203, fill="green")

    def add_legend(self):
         #my_canvas.create_rectangle(x1,y1,x2,y2, fil="color")
        self.canvas.create_rectangle(150,50,200,15, fill="red")
        self.canvas.create_rectangle(150,90,200,55, fill="green")
        self.canvas.create_text( 300, 30 , text = "Elm Avenue/Rabbit Road ", fill="black", font=('Helvetica 10 bold'))
        self.canvas.create_text( 300, 70 , text = "Hanley Highway/Westway ", fill="black", font=('Helvetica 10 bold'))
        
    def run(self):
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        self.root.mainloop()

if __name__ == "__main__" :
    app = HistrogramApp()
    
    app.run()

