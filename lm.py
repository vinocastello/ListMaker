import os.path
import random
import time

def print_list(lst):
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")

def save_list(list_choices):
    # Always overwrite
    if os.path.exists(f"{list_choices.name}.txt"):
        open(f"{list_choices.name}.txt", 'w').close()
    
    with open(f"{list_choices.name}.txt",mode = "a") as f:
        f.write(f"Name of list: {list_choices.name}\n")
        f.write(f"Length of list: {list_choices.length}\n")
        f.write("items:\n")
        for i in range(1,list_choices.length+1):
            f.write(f"{i}. {list_choices.get(i)}")
            if i < list_choices.length:
                f.write("\n")
    print(f"{list_choices.name} saved!")

def load_list(list_name):
    try:
        with open(f"{list_name}.txt",mode = "r") as f:
            f_lines = f.readlines()
            # Get name of list
            l_index = f_lines[0].find(":")
            r_index = f_lines[0].rfind("\n")
            temp_name = f_lines[0][l_index + 2: r_index]
            # Get length of list
            l_index = f_lines[1].find(":")
            r_index = f_lines[1].rfind("\n")
            temp_length = int(f_lines[1][l_index + 2: r_index])

            temp_object = LIST_CHOICES(temp_name)
            
            # Get items
            try:
                items_index = f_lines.index("items:\n")
                n = len(f_lines)
                for j in range(items_index+1,n):
                    dot_index = f_lines[j].find(".")
                    if j < n-1:
                        space_index = f_lines[j].rfind("\n")
                        tmp_choice = f_lines[j][dot_index + 2: space_index]
                    else:
                        tmp_choice = f_lines[j][dot_index + 2:]
                    temp_object.add(tmp_choice)
                return temp_object
            except ValueError:
                print("Text file has invalid input!")
                return -2
    except FileNotFoundError:
        print(f"{list_name} does not exist!")
        return -1

class LIST_CHOICES:
    def __init__(self,name):
        self.__name = name
        self.__length = 0
        self.__choices = []
    
    # Getter methods

    @property
    def name(self):
        return self.__name
    @property
    def choices(self):
        return self.__choices
    @property
    def length(self):
        return self.__length
    
    # Setter method

    @name.setter
    def name(self,new_name):
        self.__name = new_name
    
    # Utility methods

    def show(self):
        print(f"{self.name}:")
        print_list(self.choices)

    def add(self,new_choice):
        self.choices.append(new_choice)
        self.__length += 1

    def insert(self,location,new_choice):
        self.choices.insert(location,new_choice)

    def get(self,position):
        if position < 1 or position > self.length:
            raise IndexError
        else:
            return self.choices[position-1]

    def remove(self,item_to_remove):
        if self.length <= 0:
            print(f"{self.name} is still empty!")
            return
        if type(item_to_remove) == int:
            del self.choices[item_to_remove - 1]
            self.__length -= 1
            return
        found = False
        for i in range(1,self.length+1):
            if self.get(i) == item_to_remove:
                print(f"{item_to_remove} is found!")
                print(f"Deleting {item_to_remove}...")
                time.sleep(2)
                del self.choices[i]
                print("Deleted successfully!")
                found = True
                self.length -= 1
                break
        if not found:
            print(f"{item_to_remove} was not found in your list: {self.name}")

    def edit(self,curr_choice,edit_choice):
        if type(curr_choice) == int:
            self.choices[curr_choice - 1] = edit_choice
        else:
            if curr_choice == edit_choice:
                print("Your new choice is the same as the old one!")
                return
            found = False
            for i in range(1,self.length+1):
                if self.get(i) == curr_choice:
                    found = True
                    print(f"{curr_choice} is found!")
                    self.choices[i] = edit_choice
                    print(f"changing {curr_choice} with {edit_choice}...")
                    time.sleep(2)
                    break
            if not found:
                print(f"{curr_choice} was not found in your list: {self.name}")

LIST_OF_CHOICES = []

while True:
    print("LIST MAKER")
    print("[1] Create a new list of items")
    print("[2] Load an existing list of items")
    print("[3] Exit")
    command = input("command: ")
    if command == "1":
        list_name = input("Enter name of your list of items: ")
        if os.path.exists(f"{list_name}.txt"):
            print(f"You already have a list named {list_name}!")
            choice = input("Do you want to overwrite this? (Y/N): ")
            if choice.upper() == "Y":
                open(f"{list_name}.txt", 'w').close()
            else:
                print("List cannot be saved!")
                continue
        new_list = LIST_CHOICES(list_name)
        choice_num = 1
        while True:
            print("Enter the items (type END to stop adding items)")
            choice = input(f"items #{choice_num}: ")
            if choice == "END":
                break
            new_list.add(choice)
            choice_num += 1
        print("This is your new list!")
        new_list.show()
        save_list(new_list)
        LIST_OF_CHOICES.append(new_list)

    elif command == "2":
        lst_name = input("name of list to load: ")
        lst = load_list(lst_name)
        if lst != -1:
            while True:
                lst.show()
                print("[1] Add item to list")
                print("[2] Edit item in list")
                print("[3] Remove item in list")
                print("[4] Exit")
                new_choice = input("What do you want to do (1/2/3): ")
                if new_choice == "1":
                    new_item = input("New item to be added: ")
                    lst.add(new_item)
                elif new_choice == "2":
                    old_item_pos = int(input("Position of item you want to edit (number): "))
                    new_item = input("What you will replace it with: ")
                    lst.edit(old_item_pos,new_item)
                    print("Successfully edited list!")
                elif new_choice == "3":
                    del_item_pos = int(input("Position of item you want to delete (number): "))
                    lst.remove(del_item_pos)
                elif new_choice == "4":
                    print("Going back to main menu...")
                    break
                save_list(lst)

    elif command == "3":
        print("Thank you for using my app!")
        print("Exiting...")
        time.sleep(1)
        break
    else:
        print("Invalid command!")