from tkinter import *
from tkinter import messagebox

label_color = "#25265E"
small_font_style = ("Arial", 16)
digit_font=("Arial",25,"bold")
symbol_font=("Arial",22)
large_font_style = ("Arial", 35, "bold")


# create frame
class calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x650")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.total_expression = " "
        self.current_expression = " "
        self.display_frame = self.create_display_frame()
        self.total_display_label,self.expression_label = self.create_display_labels()
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            '.':(4,1),0:(4,2)
        }
        self.operator={
            "/":"/","*":"*","-":"-","+":"+"
        }
        self.button_frame = self.create_button_frame()
        # rows and columns are  expanded in the empty spaces
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x, weight=1)

        self.create_digit_button()
        self.create_operator_symbols()
        self.create_special_buttions()

    def create_special_buttions(self):
        self.create_clear()
        self.create_equal()

    def create_display_labels(self):
        total_display_label = Label(self.display_frame, text=self.total_expression, anchor=E, bg="gray", fg=label_color,
                                    padx=24,
                                    font=small_font_style)
        total_display_label.pack(expand=True, fill="both")

        expression_label = Label(self.display_frame, text=self.current_expression, anchor=E, bg="gray", fg=label_color,
        padx=24, font=large_font_style)
        expression_label.pack(expand=True, fill="both")
        return total_display_label, expression_label

    def create_display_frame(self):
        frame = Frame(self.window, height=100, bg="gray")
        frame.pack(fill='both', expand=True)
        return frame

    def add_to_expression_label(self, value):
        self.current_expression += str(value)
        self.update_expression_label()



    def create_digit_button(self):
        for digit,grid_value in self.digits.items():
            button=Button(self.button_frame,text=str(digit),bg="#ffffff",fg="pink",font= digit_font,borderwidth=0,command=lambda x=digit:self.add_to_expression_label(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=NSEW)

    def append_operators(self,operator):
        self.current_expression += operator
        self.total_expression +=self.current_expression
        self.current_expression=" "
        self.update_expression_label()
        self.update_total_display_label()



    def create_operator_symbols(self):
        i=0
        for operator,symbols in self.operator.items():
            button=Button(self.button_frame,text=symbols,bg="#ffffff",fg="pink",font=symbol_font,borderwidth=0, command=lambda x=operator:self.append_operators(x))
            button.grid(row=i,column=4,sticky=NSEW)
            i+=1

    def clear(self):
        self.current_expression=" "
        self.total_expression=" "
        self.update_total_display_label()
        self.update_expression_label()
    def create_clear(self):
        button = Button(self.button_frame, text="C", bg="#ffffff", fg="pink", font=symbol_font, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1,columnspan=3,sticky=NSEW)

    def evaluation(self):
        self.total_expression+=self.current_expression
        self.update_total_display_label()
        self.current_expression=str(eval(self.total_expression))
        self.total_expression = ""
        self.update_expression_label()


    def create_equal(self):

        button = Button(self.button_frame, text="=", bg="green", fg="pink", font=symbol_font, borderwidth=0,command=self.evaluation)
        button.grid(row=4, column=3,columnspan=2,sticky=NSEW)



    def create_button_frame(self):
        frame = Frame(self.window)
        frame.pack(fill='both', expand=True)
        return frame
    def update_total_display_label(self):
        self.total_display_label.config(text=self.total_expression)
    def update_expression_label(self):
        self.expression_label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    obj = calculator()
    obj.run()
