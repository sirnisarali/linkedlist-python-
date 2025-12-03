# Constant and class definitions
NullPointer = -1

class ListNode:
    def __init__(self, data="", pointer=NullPointer):
        self.Data = data
        self.Pointer = pointer


# Global Declarations
maxSize = 7
List = [ListNode() for _ in range(maxSize)]

StartPointer = NullPointer
FreeListPtr = 0

# Initialize the free list
for index in range(maxSize - 1):
    List[index].Pointer = index + 1
List[maxSize - 1].Pointer = NullPointer


# PROCEDURE InsertNode(NewItem)
def InsertNode(NewItem):
    global StartPointer, FreeListPtr

    if FreeListPtr != NullPointer:  # there is space
        # Take a node from free list and store data
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer

        # Find insertion point
        ThisNodePtr = StartPointer
        PreviousNodePtr = NullPointer

        while ThisNodePtr != NullPointer and List[ThisNodePtr].Data < NewItem:
            PreviousNodePtr = ThisNodePtr
            ThisNodePtr = List[ThisNodePtr].Pointer

        # Insert new node
        if PreviousNodePtr == NullPointer or NewItem < List[ThisNodePtr].Data:  # insert at start
            List[NewNodePtr].Pointer = StartPointer
            StartPointer = NewNodePtr
        else:  # insert between previous and this node
            List[NewNodePtr].Pointer = ThisNodePtr   # ✅ use ThisNodePtr here
            List[PreviousNodePtr].Pointer = NewNodePtr

        print(f"Inserted '{NewItem}' successfully.")
    else:
        print("No space available in the list!")

# PROCEDURE DeleteNode(DataItem)
def DeleteNode(DataItem):
    global StartPointer, FreeListPtr

    ThisNodePtr = StartPointer
    PreviousNodePtr = NullPointer

    # search for the node
    while ThisNodePtr != NullPointer and List[ThisNodePtr].Data != DataItem:
        PreviousNodePtr = ThisNodePtr
        ThisNodePtr = List[ThisNodePtr].Pointer

    # if found
    if ThisNodePtr != NullPointer:
        if ThisNodePtr == StartPointer:
            # delete the first node
            StartPointer = List[StartPointer].Pointer
        else:
            # link previous node to next of current
            List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer

        # add deleted node back to free list
        List[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr

        print(f"Deleted '{DataItem}' successfully.")
    else:
        print(f"Item '{DataItem}' not found in the list.")


# Traversal procedure for checking the result
def Traverse():
    global StartPointer
    current = StartPointer
    print("The start Pointer:", current)
    print("The Free List Pointer:", FreeListPtr)
    print("\nIndex | Data | Pointer")
    while current != NullPointer:
        print(f"{current:5} | {List[current].Data:4} | {List[current].Pointer:7}")
        current = List[current].Pointer
    print()

# FUNCTION FindNode(DataItem) RETURNS INTEGER
def FindNode(DataItem):
    global StartPointer
    CurrentNodePtr = StartPointer   # start at beginning

    while CurrentNodePtr != NullPointer and List[CurrentNodePtr].Data != DataItem:
        CurrentNodePtr = List[CurrentNodePtr].Pointer  # follow pointer to next node

    return CurrentNodePtr   # returns NullPointer (-1) if not found


def main():
    print()
    print("-----LINKED LIST MENU---------")
    print("[1.Insert], [2. Delete], [3. Travers], [4. Find][5. Quit]")
    choice = int(input("Select your choice:"))

    while choice != 5:
        if choice == 1:
            value = input("Enter a value to insert in linked list:")
            InsertNode(value)
        elif choice == 2:
            item = input("Enter a value to delete linked list:")
            DeleteNode(item)
        elif choice == 3:
            Traverse()
        elif choice == 4:
            DataItem = input("Enter data to search:")
            FindNode(DataItem)
        else:
            print("Invalid choice..")
        print()

        print("[1.Insert], [2. Delete], [3. Travers], [4. Find][5. Quit]")
        choice = int(input("Select your choice:"))

    print("Thanks for using the menu...")


if __name__ == "__main__":
    main()

