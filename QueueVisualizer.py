from src.models.queue import Queue
from colorama import Fore, Back, Style
from time import sleep

COLOR_MAPPING = {
    "green": Back.LIGHTGREEN_EX,
    "blue": Back.LIGHTBLUE_EX,
    "yellow": Back.LIGHTYELLOW_EX,
    "red": Back.LIGHTRED_EX,
    "dark_green": Back.GREEN,
}


class QueueVisualizer:
    def __init__(self, queue: Queue):
        self.queue = queue
        print(
            f"""
        Welcome to the Queue Visualizer! 
        The front of the queue is at the left, and the rear is at the right.\n
 
              You'll see four colors in the Queue:
              -{Back.GREEN + Fore.WHITE} GREEN: {Back.RESET + Fore.RESET} Currently IN the queue.
              -{Back.BLUE + Fore.WHITE} BLUE: {Back.RESET + Fore.RESET} Just added to the queue; i.e, currently in the queue.
              -{Back.RED + Fore.WHITE} RED: {Back.RESET + Fore.RESET} Just removed from the queue; currently NOT in the queue.
              -{Back.YELLOW + Fore.WHITE} YELLOW: {Back.RESET + Fore.RESET} Currently in the queue; you're probably taking a little {Fore.YELLOW}*peek*{Style.RESET_ALL} at it.

              {Fore.LIGHTGREEN_EX}- BEST Ω(1) {Fore.LIGHTMAGENTA_EX}- AVG Θ(1) {Fore.LIGHTRED_EX}- WORST O(1){Style.RESET_ALL}
              """
        )

    def visualize_queue(self):
        cur_node = self.queue.list.head
        while cur_node is not None:
            self.print_queue_element(cur_node.data, "green")
            sleep(0.5)
            cur_node = cur_node.next

    def print_queue_element(self, element, color, end=" ", flush=True):
        print(
            f"{Fore.WHITE + COLOR_MAPPING[color.lower()]}[ {str(element)} ]{Style.RESET_ALL}",
            end=end,
            flush=True,
        )

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
