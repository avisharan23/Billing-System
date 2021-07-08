from tkinter import*
import math,random
import os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Window",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)


        #=======Variables
        #=======Cos
        self.soap=IntVar()
        self.faceC=IntVar()
        self.faceW=IntVar()
        self.hairS=IntVar()
        self.hairG=IntVar()
        self.bodyL=IntVar()
        #=======Gro
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #========Dri
        self.limca=IntVar()
        self.mazza=IntVar()
        self.sprite=IntVar()
        self.coca=IntVar()
        self.thumb=IntVar()
        self.pepsi=IntVar()
        #==Total Tax
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drinks_tax=StringVar()

        #=========Customer
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        #============Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)    


        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10) 

        cbill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bil_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #======Cosmetics Frame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=185,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.faceC,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        faceW_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        faceW_txt=Entry(F2,width=10,textvariable=self.faceW,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        HairS_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        HairS_txt=Entry(F2,width=10,textvariable=self.hairS,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        HairG_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        HairG_txt=Entry(F2,width=10,textvariable=self.hairG,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        BodyL_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        BodyL_txt=Entry(F2,width=10,textvariable=self.bodyL,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #======GROCERY
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=185,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #======Cold Drink

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=185,width=325,height=380)

        c1_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Mazza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.mazza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Coca Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.coca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.thumb,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #====== Bill Area
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1005,y=185,width=330,height=380)
        bill_title=Label(F5,text="Bill",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #===== Button Frame

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=2,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=2,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Drinks Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=2,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=2,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=2,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Drinks Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=2,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=585,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=12,font='arial 12 bold').grid(row=0,column=0,padx=5,pady=5)
        gen_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=12,font='arial 12 bold').grid(row=0,column=1,padx=5,pady=5)
        clr_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font='arial 12 bold').grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font='arial 12 bold').grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.faceC.get()*120
        self.c_fw_p=self.faceW.get()*60
        self.c_hs_p=self.hairS.get()*180
        self.c_hg_p=self.hairG.get()*140
        self.c_bl_p=self.bodyL.get()*155
        self.total_cosmetic_price=float(

                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p                                  
                                    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*28
        self.g_o_p=self.oil.get()*150
        self.g_d_p=self.daal.get()*48
        self.g_w_p=self.wheat.get()*36
        self.g_s_p=self.sugar.get()*33
        self.g_t_p=self.tea.get()*64        

        self.total_grocery_price=float(

                                 self.g_r_p+
                                 self.g_o_p+
                                 self.g_d_p+
                                 self.g_w_p+
                                 self.g_s_p+
                                 self.g_t_p
                                  )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.03),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_l_p=self.limca.get()*25
        self.d_m_p=self.mazza.get()*25
        self.d_s_p=self.sprite.get()*25
        self.d_c_p=self.coca.get()*25
        self.d_t_p=self.thumb.get()*25
        self.d_p_p=self.pepsi.get()*25    
        
        self.total_drinks_price=float(
                                self.d_l_p+
                                self.d_m_p+
                                self.d_s_p+
                                self.d_c_p+
                                self.d_t_p+
                                self.d_p_p
                                 )
        self.cold_drinks_price.set("Rs. "+str(self.total_drinks_price))
        self.cd_tax=round((self.total_drinks_price*0.1),2)
        self.cold_drinks_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_drinks_price+
                                self.c_tax+
                                self.g_tax+
                                self.cd_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome Store")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n ==================================")
        self.txtarea.insert(END,f"\n Products\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n ==================================")

        
    def bill_area(self):
        if self.c_name.get=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Enter Customer Details")

        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Item Found")

        else:
            self.welcome_bill()
            #==========Cosmetics
            if self.soap.get() != 0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            
            if self.faceC.get() != 0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.faceC.get()}\t\t{self.c_fc_p}")

            if self.faceW.get() != 0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.faceW.get()}\t\t{self.c_fw_p}")

            if self.hairS.get() != 0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.hairS.get()}\t\t{self.c_hs_p}")

            if self.hairG.get() != 0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hairG.get()}\t\t{self.c_hg_p}")

            if self.bodyL.get() != 0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.bodyL.get()}\t\t{self.c_bl_p}")

            #==========grocery
            if self.rice.get() != 0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.oil.get() != 0:
                self.txtarea.insert(END,f"\n Oil\t\t{self.oil.get()}\t\t{self.g_o_p}")

            if self.daal.get() != 0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END,f"\n Wheat\t\t {self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get() != 0:
                self.txtarea.insert(END,f"\n Sugar\t\t {self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get() != 0:
                self.txtarea.insert(END,f"\n Tea\t\t {self.tea.get()}\t\t{self.g_t_p}")

            #==========Drinks
            if self.limca.get() != 0:
                self.txtarea.insert(END,f"\n Limca\t\t {self.soap.get()}\t\t{self.d_l_p}")

            if self.mazza.get() != 0:
                self.txtarea.insert(END,f"\n Mazza\t\t {self.faceC.get()}\t\t{self.d_m_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END,f"\n Sprite\t\t {self.faceW.get()}\t\t{self.d_s_p}")

            if self.coca.get() != 0:
                self.txtarea.insert(END,f"\n Coca Cola \t\t{self.hairS.get()}\t\t{self.d_c_p}")

            if self.thumb.get() != 0:
                self.txtarea.insert(END,f"\n Thumbs Up \t\t{self.hairG.get()}\t\t{self.d_t_p}")

            if self.pepsi.get() != 0:
                self.txtarea.insert(END,f"\n Pepsi \t\t{self.bodyL.get()}\t\t{self.d_p_p}")

            self.txtarea.insert(END,f"\n ---------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax \t\t\t {self.cosmetic_tax.get()}")

            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax \t\t\t {self.grocery_tax.get()}")

            if self.cold_drinks_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drink Tax \t\t\t {self.cold_drinks_tax.get()}")
        
            self.txtarea.insert(END,f"\n Total Bill: \t\t\t Rs.{self.Total_bill}")

            self.txtarea.insert(END,f"\n ---------------------------------")
            self.save_bill()

 
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want to Save the bill?")

        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open(r"C:\Users\shara\Desktop\AVi\Project\Billing system\Bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Bill saved")
        else:
            return

    def find_bill(self):
        present='no'
        for i in os.listdir(r"C:\Users\shara\Desktop\AVi\Project\Billing system\Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(r"C:\Users\shara\Desktop\AVi\Project\Billing system\Bills/"+i+".txt",'r')
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(EMD,d)
                f1.close()
                present='yes'
                
        if present=='no':
            messagebox.showerror("ERROR","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to Clear?")
        if op>0:
             
            self.soap.set(0)
            self.faceC.set(0)
            self.faceW.set(0)
            self.hairS.set(0)
            self.hairG.set(0)
            self.bodyL.set(0)
            #=======Gro
            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #========Dri
            self.limca.set(0)
            self.mazza.set(0)
            self.sprite.set(0)
            self.coca.set(0)
            self.thumb.set(0)
            self.pepsi.set(0)
            #==Total Tax
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            #=========Customer
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
        
            
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
        


        
root =Tk()
obj=Bill_App(root)
root.mainloop()
