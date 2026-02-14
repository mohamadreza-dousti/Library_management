import customtkinter as ctk

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('CREATED BY DOUSTI')
        self.geometry('350')

        self.tabview = ctk.CTkTabview(self, width=380, height=230,
                                corner_radius=15)
        self.tabview.pack(padx=10, pady=10, fill='both',
                    expand=True)

        self.tab1 = self.tabview.add('Books')