#!/usr/bin/python3

class MyList(list):
    """A class that inherits from list and prints a sorted version of itself."""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        print(sorted(self))

if __name__ == "__main__":
    MyList = __import__('my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)


