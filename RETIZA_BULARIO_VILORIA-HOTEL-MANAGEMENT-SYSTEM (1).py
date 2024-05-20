import csv
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import font


class Hotel:
    def __init__(self, master):
        self.master = master
        master.title("Hotel Management System")

        self.customer_data = {}
        self.room_rent = 0
        self.food_purchased = 0
        self.total_cost = 0
        self.item_purchased = 0
        self.drink_purchased = 0
        self.total_cost = 0
        self.receipt_text = 0

        self.rt = 0
        self.ft = 0
        self.dt = 0
        self.it = 0
        

        self.notebook = ttk.Notebook(master)
        self.notebook.pack()

        self.main_menu_tab = ttk.Frame (self.notebook)
        self.notebook.add(self.main_menu_tab, text="MENU")

        self.customer_info_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_info_tab, text="CUSTOMER INFO")
        self.show_info_button = ttk.Button(self.customer_info_tab, text="SHOW INFO", command=self.show_info)
        self.show_info_button.pack()
        
        self.receipts_and_print = ttk.Frame(self.notebook)
        self.notebook.add(self.receipts_and_print, text = "RECEIPTS")
        
        self.save_receipt_button = tk.Button(self.receipts_and_print, text="SAVE RECEIPT", font=("Garamond Bold",25), bg="LightCyan", command=self.save_receipt)
        self.save_receipt_button.pack(side="left")
        
        self.advance_bookings = ttk.Frame(self.notebook)
        self.notebook.add(self.advance_bookings, text="SCHEDULE AND ADVANCE BOOKINGS")
        
        self.foods_and_rooms_items = ttk.Frame(self.notebook)
        self.notebook.add(self.foods_and_rooms_items, text = "LIST OF ITEMS")
        
        self.advance_booking_button = tk.Button(self.advance_bookings, text="SCHEDULES", font=("Garamond Bold",25), bg="DimGray", fg="white", command=self.show_schedules)
        self.advance_booking_button.pack()
        
        self.show_available_rooms_button = tk.Button(self.foods_and_rooms_items, text="AVAILABLE ROOMS",  font=("Garamond Bold",25), bg="Antique White", command=self.show_available_rooms)
        self.show_available_rooms_button.pack(side="top",expand="Yes", anchor="w", fill="x")
        
        self.show_available_foods_button = tk.Button(self.foods_and_rooms_items, text="FOODS",  font=("Garamond Bold",25), bg="Linen", command=self.show_available_foods)
        self.show_available_foods_button.pack(side="top",expand="Yes", anchor="w", fill="x")
        
        self.show_available_drinks_button = tk.Button(self.foods_and_rooms_items, text="DRINKS",  font=("Garamond Bold",25), bg="HoneyDew", command=self.show_available_drinks)
        self.show_available_drinks_button.pack(side="top",expand="Yes", anchor="w", fill="x")
        
        self.show_available_hygiene_items_button = tk.Button(self.foods_and_rooms_items, text="ITEMS",  font=("Garamond Bold",25), bg="Bisque", fg="black", command=self.show_available_hygiene_items)
        self.show_available_hygiene_items_button.pack(side="top",expand="Yes", anchor="w", fill="x")
        
        self.receipt_button = tk.Button(self.receipts_and_print, text="SHOW RECEIPT",  font=("Garamond Bold",25), bg="BurlyWood", fg="black", command=self.show_receipt)
        
        self.receipt_button.pack(side="left")

        
        
        self.welcome_label = tk.Label(self.main_menu_tab, text="MANAGING SYSTEM")
        self.welcome_label.pack()
        
        self.enter_data_button = tk.Button(self.main_menu_tab, text="CUSTOMER DATA", font=("Garamond Bold",25), bg="AntiqueWhite", command=self.enter_customer_data)
        self.enter_data_button.pack(side="top",expand="Yes", anchor="w", fill="x")

        self.calculate_rent_button = tk.Button(self.main_menu_tab, text="ROOM SELECTION", font=("Garamond Bold",25), bg="Linen", command=self.calculate_room_rent)
        self.calculate_rent_button.pack(side="top",expand="Yes", anchor="w", fill="x")

        self.calculate_food_button = tk.Button(self.main_menu_tab, text="ORDER A FOOD", font=("Garamond Bold",25), bg="HoneyDew", command=self.calculate_food_purchased)
        self.calculate_food_button.pack(side="top",expand="Yes", anchor="w", fill="x")
        
        self.calculate_drink_purchased_button = tk.Button(self.main_menu_tab, text= "ORDER A DRINK", font=("Garamond Bold",25), bg="Bisque", command = self.calculate_drink_purchased)
        self.calculate_drink_purchased_button.pack(side="top",expand="Yes", anchor="w", fill="x")
        
        self.calculate_item_purchased_button = tk.Button(self.main_menu_tab, text= "ORDER AN ITEM", font=("Garamond Bold",25), bg="Light Cyan", command = self.calculate_hygiene_item_purchased)
        self.calculate_item_purchased_button.pack(side="top",expand="Yes", anchor="w", fill="x")
        
        self.show_total_cost_button = tk.Button(self.main_menu_tab, text="TOTAL COST", font=("Garamond Bold",25), bg="AliceBlue", command=self.show_total_cost)
        self.show_total_cost_button.pack(side="top",expand="Yes", anchor="w", fill="x")

    def enter_customer_data(self):
        self.customer_data['name'] = simpledialog.askstring("Name", "Please enter your name:\t\t\t")
        self.customer_data['address'] = simpledialog.askstring("Address", "Please enter your address:\t\t\t")
        self.customer_data['contact'] = simpledialog.askstring("Contact", "Please enter your contact number:\t\t\t")
        checkin = simpledialog.askstring("Check-in Date", "Please enter your check-in date (mm/dd/yyyy):")
        checkout = simpledialog.askstring("Check-out Date", "Please enter your check-out date (mm/dd/yyyy):")
        try:
            checkin_date = datetime.datetime.strptime(checkin, '%m/%d/%Y')
            checkout_date = datetime.datetime.strptime(checkout, '%m/%d/%Y')
            if checkin_date > checkout_date:
                messagebox.showerror("Error", "Invalid date range")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid date format, use mm/dd/yyyy")
            
        
        self.customer_data['checkin'] = checkin
        self.customer_data['checkout'] = checkout
        messagebox.showinfo("Info", "Customer data entered successfully")

    def calculate_room_rent(self):
        room_type = simpledialog.askstring("Room Type", "Please enter the room type\n Single = PHP999\n Double Deluxe = PHP1999\n Premium Suite = PHP3499")
        days_stayed = simpledialog.askinteger("Days Stayed", "Please enter the number of days stayed:")
        self.rt = room_type
        if room_type == "Single":
            self.room_rent = days_stayed * 999
        elif room_type == "Double Deluxe":
            self.room_rent = days_stayed * 1999
        elif room_type == "Premium Suite":
            self.room_rent = days_stayed * 3499
        else:
            messagebox.showerror("Error", "Invalid room type entered")
            messagebox.showinfo("Info", "Room rent calculated successfully")

       

    def calculate_food_purchased(self):
        food_type = simpledialog.askstring("Food type", "Please choose the food that you will eat.\n Meal 1 = PHP175\n Meal 2 = PHP200\n Meal 3 = PHP185\n Meal 4 = PHP190\n Meal 5 = PHP220")
        food_quantity = simpledialog.askinteger("Food quantity", "Please enter the quantity of food")
        if food_type == "Meal 1":
            self.food_purchased = food_quantity*175
        elif food_type == "Meal 2":
            self.food_purchased = food_quantity*200
        elif food_type == "Meal 3":
            self.food_purchased = food_quantity*185
        elif food_type == "Meal 4":
            self.food_purchased = food_quantity*190
        elif food_type == "Meal 5":
            self.food_purchased = food_quantity*220
        else:
            messagebox.showinfo("Info", "Food cost calculated successfully")
        self.ft = food_type

    def calculate_drink_purchased(self):
        drink_type = simpledialog.askstring("Beverage type", "Please choose the drinks you want to take.\n Water = PHP20\n Juice = PHP30\n Wine = PHP1000\n Beer = PHP190\n Whiskey = PHP1200 " )
        drink_quantity = simpledialog.askinteger("Beverage quantity", "Please enter the quantity of drinks")
        if drink_type == "Water":
            self.drink_purchased = drink_quantity*20
        elif drink_type == "Juice":
            self.drink_purchased = drink_quantity*30
        elif drink_type == "Wine": 
            self.drink_purchased = drink_quantity*1000
        elif drink_type == "Beer":
            self.drink_purchased = drink_quantity*190
        elif drink_type == "Whiskey":
            self.drink_purchased = drink_quantity*1200
        else:
            messagebox.showinfo("Info", "drink cost calculated successfully")
        self.dt = drink_type
    def calculate_hygiene_item_purchased(self):
        item_type = simpledialog.askstring("item type", " Package 1 = PHP250\n Package 2 = PHP200\n Package 3 = PHP150\n Package 4 = PHP120\n Package 5 = PHP100\n Package 6 = PHP120")
        item_quantity = simpledialog.askinteger("item quantity", "Please enter the total quantity of items:")
        if item_type == "Package 1":
            self.item_purchased = item_quantity*250
        elif item_type == "Package 2":
            self.item_purchased = item_quantity*200
        elif item_type == "Package 3":
            self.item_purchased = item_quantity*150
        elif item_type == "Package 4":
            self.item_purchased = item_quantity*120
        elif item_type == "Package 5":
            self.item_purchased = item_quantity*100
        elif item_type == "Package 6":
            self.item_purchased = item_quantity*120 
        else:
            messagebox.showinfo("Info", "Item cost calculated successfully")
        self.it = item_type

    def show_total_cost(self):
        self.total_cost = self.room_rent + self.food_purchased + self.drink_purchased + self.item_purchased
        messagebox.showinfo("Info", "Total cost: PHP" + str(self.total_cost))

    def show_info(self):
        self.notebook.select(self.customer_info_tab)
        self.customer_info_label = tk.Label(self.customer_info_tab, text="Customer Name: " + self.customer_data.get('name', '') + "\n"
                                                                    "Customer Address: " + self.customer_data.get('address', '') + "\n"
                                                                    "Customer Contact: " + self.customer_data.get('contact', '') + "\n"
                                                                    "Check-in Date: " + self.customer_data.get('checkin', '') + "\n"
                                                                    "Check-out Date: " + self.customer_data.get('checkout', ''))
        self.customer_info_label.pack()
        
        self.back_button = tk.Button(self.customer_info_tab, text="Back", command=self.go_back)
        self.back_button.pack()
        
    def go_back(self):
        self.notebook.select(self.main_menu_tab)
    def show_schedules(self):
        self.check_in_date = simpledialog.askstring("Check-In Date", "Enter check-in date (MM/DD/YYYY):")
        self.check_out_date = simpledialog.askstring("Check-Out Date", "Enter check-out date (MM/DD/YYYY):")
        messagebox.showinfo("Schedule", "Check-in date: " + self.check_in_date + "\nCheck-out date: " + self.check_out_date)
        
    def show_available_rooms(self):
        available_rooms = {} 
        rooms = {'Single':25 , 'Double Deluxe':10 , 'Premium Suite':5} 

        
        for room_type, total_rooms in rooms.items():
            booked_rooms = 0 
            for customer in self.customer_data:
                if customer['room_type'] == room_type:
                    booked_rooms += 1
            available_rooms[room_type] = total_rooms - booked_rooms

        
        messagebox.showinfo("Available Rooms", f'Single Rooms: {available_rooms["Single"]}\nDouble Deluxe Rooms: {available_rooms["Double Deluxe"]}\n Premium Suite Rooms: {available_rooms["Premium Suite"]}')
    def show_available_foods(self):
        foods = ["Meal 1 - {Adobo, Rice,Soup, Free Beverage of Choice} = 175", "Meal 2 - {Sinigang, Rice, Desert, Free Soup, Free Beverage of Choice} = PHP200", "Meal 3 - {Lumpia, Rice, 2 Boiled Eggs, Sauce, Dessert, Free Beverage of Choice} = PHP185", "Meal 4 - {Kare-kare, Rice, Dessert, Free Beverage of Choice} = PHP190", "Meal 5 - {Sisig, Tokwa, Rice, Dessert, Free Beverage of Choice } = PHP220"]
        messagebox.showinfo("Available Foods", "\n".join(foods))
        
    def show_available_drinks(self):
        foods = ["Water = PHP20", "Juice = PHP30", "Wine = PHP100", "Beer = PHP190", "Whiskey = PHP250"]
        messagebox.showinfo("Available drinks", "\n".join(foods))
        
    def show_available_hygiene_items(self):
        foods = ["Package 1 - {Toothpaste, Toothbrush, Shampoo, Soap, Floss} = PHP250", "Package 2 - {Condom, Lotion, Tissue}= PHP200", "Package 3 - {Face Cleanser(Sachet), Face Moisturizer(Sachet), Sunblock(Sachet), Cotton Buds} = PHP150", "Package 4 - {Alcohol 50ML, Cotton, Sanitizer 30 ML} = PHP 120", "Package 5 - {Shampoo, Conditioner, Keratin} = PHP100", "Package 6 - {Feminine Wash, Tampons, Pads} = PHP 120"]
        messagebox.showinfo("Available hygiene items", "\n".join(foods))

    def book_schedule(self):
        selected_schedule = self.schedule_listbox.get(self.schedule_listbox.curselection())
        messagebox.showinfo("Info", f"You have successfully booked the {selected_schedule} schedule")

    def show_receipt(self):
        receipt_text = "Hotel Management System\n\n"
        receipt_text += "Name: {}\n".format(self.customer_data.get('name', 'N/A'))
        receipt_text += "Address: {}\n".format(self.customer_data.get('address', 'N/A'))
        receipt_text += "Contact: {}\n".format(self.customer_data.get('contact', 'N/A'))
        receipt_text += "Check-in: {}\n".format(self.customer_data.get('checkin', 'N/A'))
        receipt_text += "Check-out: {}\n".format(self.customer_data.get('checkout', 'N/A'))
        receipt_text += "\nRoom Rent: PHP{}\n".format(self.room_rent)
        receipt_text += "\nRoom type: ={}\n".format(self.rt)
        receipt_text += "\nFood Purchased: PHP{}\n".format(self.food_purchased)
        receipt_text += "\nFood type: = {}\n".format(self.ft)
        receipt_text += "\nDrink Purchased: PHP{}\n".format(self.drink_purchased)
        receipt_text += "\nDrink type: = {}\n".format(self.dt)
        receipt_text += "\nItem Purchased: PHP{}\n".format(self.item_purchased)
        receipt_text += "\nItem type: = {}\n".format(self.it)
        receipt_text += "Total Cost: PHP{}\n".format(self.total_cost)
        messagebox.showinfo("Receipt", receipt_text)
        
    def save_receipt(self):
        receipt_text = "Hotel Management System\n\n"
        receipt_text += "Name: {}\n".format(self.customer_data.get('name', 'N/A'))
        receipt_text += "Address: {}\n".format(self.customer_data.get('address', 'N/A'))
        receipt_text += "Contact: {}\n".format(self.customer_data.get('contact', 'N/A'))
        receipt_text += "Check-in: {}\n".format(self.customer_data.get('checkin', 'N/A'))
        receipt_text += "Check-out: {}\n".format(self.customer_data.get('checkout', 'N/A'))
        receipt_text += "\nRoom Rent: PHP{}\n".format(self.room_rent)
        receipt_text += "\nRoom type: ={}\n".format(self.rt)
        receipt_text += "\nFood Purchased: PHP{}\n".format(self.food_purchased)
        receipt_text += "\nFood type: = {}\n".format(self.ft)
        receipt_text += "\nDrink Purcahsed: PHP{}\n".format(self.drink_purchased)
        receipt_text += "\nDrink type: = {}\n".format(self.dt)
        receipt_text += "\nItem Purchased: PHP{}\n".format(self.item_purchased)
        receipt_text += "\nItem type: = {}\n".format(self.it)
        receipt_text += "Total Cost: PHP{}\n".format(self.total_cost)

        filename = "{}_C:\\Users\\WIN 10\\Downloads\\Hotel Management System\\Receipt.txt".format(self.customer_data.get('name', 'N/A'))
        with open(f"C:\\Users\\WIN 10\\Downloads\\Hotel Management System\\Receipt.txt", 'w') as receipt_file:
            receipt_file.write(receipt_text)

        messagebox.showinfo("Receipt", "Receipt saved to {}".format(filename))
    
root = tk.Tk()
Hotel = Hotel(root)
root.minsize(1000,475)
root.configure(bg="Light Grey")
root.mainloop()


        
