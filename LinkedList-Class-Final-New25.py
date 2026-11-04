# Constant and class definitions

NullPointer = -1

class ListNode:
    # Data : STRING
    # Pointer : INTEGER

    def __init__(self, data="", pointer=NullPointer):
        self.Data = data
        self.Pointer = pointer


# Global declarations

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

    if FreeListPtr != NullPointer:

        # Allocate a node from the free list
        NewNodePtr = FreeListPtr
        FreeListPtr = List[FreeListPtr].Pointer

        # Store the new data
        List[NewNodePtr].Data = NewItem

        # Find the correct insertion position
        ThisNodePtr = StartPointer
        PreviousNodePtr = NullPointer

        while (ThisNodePtr != NullPointer and
               List[ThisNodePtr].Data < NewItem):

            PreviousNodePtr = ThisNodePtr
            ThisNodePtr = List[ThisNodePtr].Pointer

        # Insert at the beginning
        if PreviousNodePtr == NullPointer:

            List[NewNodePtr].Pointer = StartPointer
            StartPointer = NewNodePtr

        # Insert between nodes or at the end
        else:

            List[NewNodePtr].Pointer = ThisNodePtr
            List[PreviousNodePtr].Pointer = NewNodePtr

        print(f"Inserted '{NewItem}' successfully.")

    else:
        print("No space available in the list!")


# PROCEDURE DeleteNode(DataItem)

def DeleteNode(DataItem):
    global StartPointer, FreeListPtr

    ThisNodePtr = StartPointer
    PreviousNodePtr = NullPointer

    # Search for the node
    while (ThisNodePtr != NullPointer and
           List[ThisNodePtr].Data != DataItem):

        PreviousNodePtr = ThisNodePtr
        ThisNodePtr = List[ThisNodePtr].Pointer

    # If the node is found
    if ThisNodePtr != NullPointer:

        # Delete the first node
        if ThisNodePtr == StartPointer:
            StartPointer = List[ThisNodePtr].Pointer

        else:
            # Link previous node to the next node
            List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer

        # Return deleted node to the free list
        List[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr

        print(f"Deleted '{DataItem}' successfully.")

    else:
        print(f"Item '{DataItem}' not found in the list.")


# PROCEDURE Traverse()

def Traverse():

    current = StartPointer

    print("\nStart Pointer:", StartPointer)
    print("Free List Pointer:", FreeListPtr)
    print("\nIndex | Data | Pointer")

    while current != NullPointer:

        print(f"{current:5} | {List[current].Data:4} | {List[current].Pointer:7}")

        current = List[current].Pointer

    print()


# FUNCTION FindNode(DataItem) RETURNS INTEGER

def FindNode(DataItem):

    CurrentNodePtr = StartPointer

    while (CurrentNodePtr != NullPointer and
           List[CurrentNodePtr].Data != DataItem):

        CurrentNodePtr = List[CurrentNodePtr].Pointer

    return CurrentNodePtr


# Main menu

def main():

    print("\n----- LINKED LIST MENU -----")
    print("[1. Insert] [2. Delete] [3. Traverse] [4. Find] [5. Quit]")

    choice = int(input("Select your choice: "))

    while choice != 5:

        if choice == 1:

            value = input("Enter a value to insert: ")
            InsertNode(value)

        elif choice == 2:

            item = input("Enter a value to delete: ")
            DeleteNode(item)

        elif choice == 3:

            Traverse()

        elif choice == 4:

            DataItem = input("Enter data to search: ")
            result = FindNode(DataItem)

            if result != NullPointer:
                print("Item found at index:", result)
            else:
                print("Item not found.")

        else:
            print("Invalid choice!")

        print("\n[1. Insert] [2. Delete] [3. Traverse] [4. Find] [5. Quit]")

        choice = int(input("Select your choice: "))

    print("Thanks for using the menu...")


if __name__ == "__main__":
    main()
