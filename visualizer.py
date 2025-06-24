from src.models.queue import Queue
from src.models.stack import Stack
from src.models._array import Array
from src.models.singly_LL import SinglyLL
from src.models.doublyLL import DoublyLL
from colorama import Fore, Back, Style
from time import sleep

COLOR_MAPPING = {"green": Back.LIGHTGREEN_EX, "blue": Back.LIGHTBLUE_EX, "yellow": Back.LIGHTYELLOW_EX, 
                "red": Back.LIGHTRED_EX, "dark_green": Back.GREEN}


class QueueVisualizer:
    def __init__(self, queue: Queue):
        self.queue = queue
        print(f"""
        Welcome to the Queue Visualizer! 
        The front of the queue is at the left, and the rear is at the right.\n
 
              You'll see four colors in the Queue:
              -{Back.GREEN + Fore.WHITE} GREEN: {Back.RESET + Fore.RESET} Currently IN the queue.
              -{Back.BLUE + Fore.WHITE} BLUE: {Back.RESET + Fore.RESET} Just added to the queue; i.e, currently in the queue.
              -{Back.RED + Fore.WHITE} RED: {Back.RESET + Fore.RESET} Just removed from the queue; currently NOT in the queue.
              -{Back.YELLOW + Fore.WHITE} YELLOW: {Back.RESET + Fore.RESET} Currently in the queue; you're probably taking a little {Fore.YELLOW}*peek*{Style.RESET_ALL} at it.

              {Fore.LIGHTGREEN_EX}- BEST Ω(1) {Fore.LIGHTMAGENTA_EX}- AVG Θ(1) {Fore.LIGHTRED_EX}- WORST O(1){Style.RESET_ALL}
              """)

    def visualize_queue(self):
        cur_node = self.queue.list.head
        while cur_node is not None:
            self.print_queue_element(cur_node.data, "green")
            sleep(0.5)
            cur_node = cur_node.next
    
    def print_queue_element(self, element, color, end=" ", flush=True):
        print(f"{Fore.WHITE + COLOR_MAPPING[color.lower()]}[ {str(element)} ]{Style.RESET_ALL}", end=end, flush=True)

    def visualize_enqueue(self, item):
        enqueued = self.queue.enqueue(item)
        print(self.__str__())
        cur_node = self.queue.list.head
        is_first = True
        while cur_node is not None:
            if is_first:
                print("in →", end=" ")
                self.print_queue_element(cur_node.data, "blue")
                is_first = False
            else:
                self.print_queue_element(cur_node.data, "green")
            sleep(0.5)
            cur_node = cur_node.next
        print(end="\n")

        print("\nreturned →", end=" ", flush=True)
        self.print_queue_element(enqueued, "blue", end="\n")

    def visualize_dequeue(self):
        dequeued = self.queue.dequeue()
        print(self.__str__())
        self.visualize_queue()
        print(f"out→ ", end="", flush=True)
        self.print_queue_element(dequeued, "red", end="\n")
        print(f"\nreturned →", end=" ", flush=True)
        self.print_queue_element(dequeued, "red", end="\n")
    
    def visualize_peek(self):
        print(self.__str__())
        cur_node = self.queue.list.head
        while cur_node is not None:
            if cur_node == self.queue.list.head:
                self.print_queue_element(str(self.queue.peek()), "yellow")
            else:
                self.print_queue_element(str(cur_node.data), "green")
            sleep(0.5)
            cur_node = cur_node.next
        sleep(0.5)
        print("\n\nreturned → ", end="")
        self.print_queue_element(str(self.queue.peek()), "yellow", end="\n")
        sleep(0.5)

    def __str__(self):
        return f"\n\nQUEUE: [Size: {self.queue.list.size()}]"


# ----------- ARRAY VISUALIZER -------------- #

class ArrayVisualizer:
    def __init__(self, array: Array):
        self.array = array
        self.size = array.size
        self.type = array.array_type
        self.vals = array.memory
        print(f"""\n\nWelcome to Array Visualizer!
        
            - {Back.GREEN} Green: {Style.RESET_ALL} Regular, schmegular elements. Not much going on with them (yet!).
            - {Back.LIGHTBLUE_EX} Blue: {Style.RESET_ALL} About to shift or has just shifted.
            - {Back.LIGHTGREEN_EX} Light Green: {Style.RESET_ALL} About to be shifted onto (RIP...)

        """)

    def visualize_array(self):
        for i in range(self.size):
            if i is not None:
                print(f"{Back.GREEN + Fore.WHITE}[ {self.vals[i]} ]{Style.RESET_ALL}", end=" ", flush=True)
                sleep(0.5)
        print("", end="\n\n")
    
    def size(self):
        return self.array.size()

    def visualize_set_index(self, index, value):
        self.array.set_index(index, value)
        self.visualize_array()

    def print_array_element(self, element, color, end=" "):
        print(f"{COLOR_MAPPING[color.lower()]}[ {element} ]{Style.RESET_ALL}", end=end, flush=True)
        sleep(0.5)

    def print_array_elements(self, elements, color, end=" "):
        for i in range(len(elements)):
            if i == len(elements) - 1:
                self.print_array_element(elements[i], color, end=end)
            else:
                self.print_array_element(elements[i], color)

    def visualize_insert(self, index, data):
        print(f"Inserting {data} into index {index}...")
        old_arr = list(self.vals)
        self.array.insert(index, data)
        new_arr = list(self.vals)

        for i in range(self.size -1, index, -1):
            print(f"\ni = {i}")
            sleep(0.5)

            self.print_array_elements(elements=old_arr[:i-1], color="dark_green")
            if i == self.size - 1:
                self.print_array_element(old_arr[i-1], "blue")
                self.print_array_element(old_arr[i], "green", end="\n")
            else:
                self.print_array_element(old_arr[i-1], "blue")
                self.print_array_element(old_arr[i], "green")
                self.print_array_elements(old_arr[i+1:], "dark_green", end="\n")
            self.format_arrows(i, old_arr)
            print("")

            self.print_array_elements(elements=old_arr[:i-1], color="dark_green")
            if i == self.size-1:
                self.print_array_element(old_arr[i-1], color="dark_green")
                self.print_array_element(new_arr[i], color="blue", end="\n")
            else:
                self.print_array_element(old_arr[i-1], color="dark_green")
                self.print_array_element(new_arr[i], color="blue")
                self.print_array_elements(new_arr[i+1:], color="dark_green", end="\n")
            print("")
            old_arr = old_arr[:i] + new_arr[i:]
            
        
        for i in range(len(old_arr[:index])):
            print(f"⎯⎯⎯⎯⎯ ", end="", flush=True)
            sleep(0.5)
        print(f"({data})↴")
        self.print_array_elements(new_arr[:index], color="green")
        self.print_array_element(new_arr[index], color="blue")
        if index < self.size:
            self.print_array_elements(new_arr[index+1:], color="green")
        print("\n")

    def format_arrows(self, i, old_arr):
        for j in range(len(old_arr[:i-1])):
            element = "[ " + str(old_arr[j]) + " ]"
            print("⎯" * len(element), end=" ", flush=True)
            sleep(0.5)


        for j in range(len(old_arr[i-1:])):
            element = "[ " + str(old_arr[j]) + " ]"
            elem_len = len(element)
            mid = elem_len // 2
            high = elem_len - mid
            low = elem_len - high - 1
            if j == 0:
                print(" " * low + " ↑" + " " * high, end=" ")
            else:
                print(" " * low + "→ ↴" + " " * high, end="\n")
                break
        sleep(0.5)

    def __str__(self):
        print(f"Size: {self.size()} - Type: {self.type}")

if __name__ == "__main__":
    queue = QueueVisualizer(Queue())
    queue.visualize_enqueue(1)
    queue.visualize_enqueue(2)
    queue.visualize_enqueue(3)
    queue.visualize_dequeue()
    queue.visualize_enqueue(4)
    queue.visualize_enqueue(5)
    queue.visualize_dequeue()
    queue.visualize_dequeue()
    queue.visualize_peek()

    my_array = Array("int", 5)
    my_array.set_index(0, 0)
    my_array.set_index(1, 1)
    my_array.set_index(2, 2)
    my_array.set_index(3, 3)
    my_array.set_index(4, 4)

    array = ArrayVisualizer(my_array)
    array.visualize_insert(2, 0)