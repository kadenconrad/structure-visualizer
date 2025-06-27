from src.models._array import Array
from colorama import Back, Fore, Style
from time import sleep
from QueueVisualizer import COLOR_MAPPING
import ctypes


class ArrayVisualizer:
    def __init__(self, array: Array):
        self.array = array
        self.size = array.size
        self.type = array.array_type
        self.vals = array.memory
        print(
            f"""\n\nWelcome to Array Visualizer!
        
            - {Back.GREEN} Green: {Style.RESET_ALL} Regular, schmegular elements. Not much going on with them (yet!).
            - {Back.LIGHTBLUE_EX + Style.BRIGHT} Blue: {Style.RESET_ALL} Element of concern, i.e., about to shift, has just shifted, or is being compared or pivoted from.
            - {Back.LIGHTGREEN_EX} Light Green: {Style.RESET_ALL} Slightly less regular elements. May be sorted.
            - {Back.YELLOW + Style.BRIGHT} Yellow: {Style.RESET_ALL} Element(s) of secondary concern. Not the most important, but watch out! Possibly about to be shifted onto...
        """
        )
        global COLOR_MAPPING
        COLOR_MAPPING.update(
            {
                "blue": Back.LIGHTBLUE_EX + Style.BRIGHT,
                "yellow": Back.LIGHTYELLOW_EX + Style.BRIGHT,
            }
        )

    def visualize_array(self):
        for i in range(self.size):
            if i is not None:
                print(
                    f"{Back.GREEN + Fore.WHITE}[ {self.vals[i]} ]{Style.RESET_ALL}",
                    end=" ",
                    flush=True,
                )
                sleep(0.5)
        print("", end="\n\n")

    def size(self):
        return self.array.size()

    def visualize_set_index(self, index, value):
        self.array.set_index(index, value)
        self.visualize_array()

    def print_array_element(self, element, color, end=" "):
        print(
            f"{COLOR_MAPPING[color.lower()]}[ {element} ]{Style.RESET_ALL}",
            end=end,
            flush=True,
        )
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

        for i in range(self.size - 1, index, -1):
            print(f"\ni = {i}")
            sleep(0.5)

            self.print_array_elements(elements=old_arr[: i - 1], color="dark_green")
            if i == self.size - 1:
                self.print_array_element(old_arr[i - 1], "blue")
                self.print_array_element(old_arr[i], "green", end="\n")
            else:
                self.print_array_element(old_arr[i - 1], "blue")
                self.print_array_element(old_arr[i], "green")
                self.print_array_elements(old_arr[i + 1 :], "dark_green", end="\n")
            self.format_arrows(i, old_arr)
            print("")

            self.print_array_elements(elements=old_arr[: i - 1], color="dark_green")
            if i == self.size - 1:
                self.print_array_element(old_arr[i - 1], color="dark_green")
                self.print_array_element(new_arr[i], color="blue", end="\n")
            else:
                self.print_array_element(old_arr[i - 1], color="dark_green")
                self.print_array_element(new_arr[i], color="blue")
                self.print_array_elements(
                    new_arr[i + 1 :], color="dark_green", end="\n"
                )
            print("")
            old_arr = old_arr[:i] + new_arr[i:]

        for i in range(len(old_arr[:index])):
            print(f"⎯⎯⎯⎯⎯ ", end="", flush=True)
            sleep(0.5)
        print(f"({data})↴")
        self.print_array_elements(new_arr[:index], color="green")
        self.print_array_element(new_arr[index], color="blue")
        if index < self.size:
            self.print_array_elements(new_arr[index + 1 :], color="green")
        print("\n")

    def format_arrows(self, i, old_arr):
        for j in range(len(old_arr[: i - 1])):
            element = "[ " + str(old_arr[j]) + " ]"
            print("⎯" * len(element), end=" ", flush=True)
            sleep(0.5)

        for j in range(len(old_arr[i - 1 :])):
            element = "[ " + str(old_arr[j]) + " ]"
            elem_len = len(element)
            mid = elem_len // 2
            high = elem_len - mid
            low = elem_len - high - 1
            if j == 0:
                print(" " * low + "↑" + " " * high, end=" ")
            else:
                print(" " * low + "→ ↴" + " " * high, end="\n")
                break
        sleep(0.5)

    def __str__(self):
        print(f"Size: {self.size()} - Type: {self.type}")

    def visualize_binary_search(self, target):
        print(f"\nPerforming binary search for target: {target}")

        low = 0
        high = self.array.size - 1
        found = False

        while low <= high:
            print("\nCurrent array state:")
            for i in range(self.array.size):
                if i == (low + high) // 2:  # mid
                    self.print_array_element(self.array.get_index_data(i), "blue")
                elif low <= i <= high:  # search range
                    self.print_array_element(self.array.get_index_data(i), "green")
                else:  # not in search partition of array
                    self.print_array_element(self.array.get_index_data(i), "dark_green")
                sleep(0.5)
            print()

            mid = (low + high) // 2
            if target > self.array.get_index_data(mid):
                print(f"\n{target} > {mid} ← mid index element")
                low = mid + 1
            elif target < self.array.get_index_data(mid):
                print(f"\n{target} < {mid} ← mid index element")
                high = mid - 1
            elif target == self.array.get_index_data(mid):
                print(
                    f"\n{Fore.LIGHTMAGENTA_EX}{target} found at index {mid}!{Style.RESET_ALL}"
                )
                found = True
                return {mid}

            sleep(0.5)

        if not found:
            print(
                f"\n{Fore.LIGHTRED_EX}Target {target} not found in the array.{Style.RESET_ALL}"
            )
            return -1

    def visualize_selection_sort(self):
        print("\nPerforming Selection Sort:")

        for i in range(self.array.size - 1):
            print(f"\nIteration {i+1}:")

            min_idx = i
            print(f"Current minimum: {i}...")
            sleep(0.5)

            for j in range(i + 1, self.array.size):
                print(
                    f"\nComparing {self.array.get_index_data(j)} with current minimum: {self.array.get_index_data(min_idx)}..."
                )
                for k in range(self.array.size):
                    if k == min_idx:
                        self.print_array_element(self.array.get_index_data(k), "blue")
                    elif k == j:
                        self.print_array_element(self.array.get_index_data(k), "yellow")
                    elif k < i:
                        self.print_array_element(self.array.get_index_data(k), "green")
                    else:
                        self.print_array_element(
                            self.array.get_index_data(k), "dark_green"
                        )
                    sleep(0.5)

                if self.array.get_index_data(j) < self.array.get_index_data(min_idx):
                    print(
                        f"\nNew minimum found: {self.array.get_index_data(j)} at index {j}!"
                    )
                    min_idx = j
                    sleep(0.5)

            if min_idx != i:
                print(
                    f"\nSwapping {self.array.get_index_data(i)} with {self.array.get_index_data(min_idx)}"
                )

                temp = self.array.get_index_data(i)
                self.array.set_index(i, self.array.get_index_data(min_idx))
                self.array.set_index(min_idx, temp)
                sleep(1)

                print(f"\nAfter swap – current min: {min_idx}")
                for k in range(self.array.size):
                    if k == i or k == min_idx:
                        self.print_array_element(self.array.get_index_data(k), "blue")
                    elif k < i:
                        self.print_array_element(self.array.get_index_data(k), "green")
                    else:
                        self.print_array_element(
                            self.array.get_index_data(k), "dark_green"
                        )
                    sleep(0.5)
            else:
                print(f"\nNo swap needed...")

        print("\n\nSelection Sort Complete!")
        print("\nFinal array:")
        self.visualize_array()

    def visualize_insertion_sort(self):
        print("\nPerforming Insertion Sort:")

        for i in range(1, self.array.size):
            print(f"\nIteration {i}:")
            print(
                f"Finding element {self.array.get_index_data(i)}'s place in the sorted portion of the array"
            )
            sleep(1)

            key = self.array.get_index_data(i)
            j = i - 1

            print("\nBefore insertion:")
            for k in range(self.array.size):
                if k == i:
                    self.print_array_element(
                        self.array.get_index_data(k), "blue"
                    )  # element being inserted
                elif k < i:
                    self.print_array_element(
                        self.array.get_index_data(k), "green"
                    )  # sorted
                else:
                    self.print_array_element(
                        self.array.get_index_data(k), "dark_green"
                    )  # unsorted
                sleep(0.5)

            while j >= 0 and self.array.get_index_data(j) > key:
                print(f"\nShifting {self.array.get_index_data(j)} to the right")
                self.array.set_index(j + 1, self.array.get_index_data(j))
                j -= 1

            self.array.set_index(j + 1, key)

            print("\nAfter insertion:")
            for k in range(self.array.size):
                if k == j + 1:
                    self.print_array_element(self.array.get_index_data(k), "blue")
                elif k <= i:
                    self.print_array_element(self.array.get_index_data(k), "green")
                else:
                    self.print_array_element(self.array.get_index_data(k), "dark_green")
                sleep(0.2)

        print("\n\nInsertion Sort Complete!")
        print("\nFinal array:")
        self.visualize_array()

    def visualize_shell_sort(self):
        print("\nPerforming Shell Sort:")

        gap = self.array.size // 2
        while gap > 0:
            print(f"\nCurrent gap: {gap}")
            sleep(1)

            for i in range(gap, self.array.size):
                print(
                    f"\nProcessing element at index {i}: {self.array.get_index_data(i)}"
                )

                temp = self.array.get_index_data(i)
                j = i

                print("\nBefore shifting:")
                for k in range(self.array.size):
                    if k == i:
                        self.print_array_element(self.array.get_index_data(k), "blue")
                    elif k < i and (k % gap == i % gap):
                        self.print_array_element(self.array.get_index_data(k), "yellow")
                    else:
                        self.print_array_element(
                            self.array.get_index_data(k), "dark_green"
                        )
                    sleep(0.2)

                while j >= gap and self.array.get_index_data(j - gap) > temp:
                    print(
                        f"\nShifting {self.array.get_index_data(j - gap)} to position {j}"
                    )
                    self.array.set_index(j, self.array.get_index_data(j - gap))
                    j -= gap

                self.array.set_index(j, temp)

                print("\nAfter insertion:")
                for k in range(self.array.size):
                    if k == j:
                        self.print_array_element(self.array.get_index_data(k), "blue")
                    elif k % gap == j % gap:
                        self.print_array_element(self.array.get_index_data(k), "green")
                    else:
                        self.print_array_element(
                            self.array.get_index_data(k), "dark_green"
                        )
                    sleep(0.2)

            print(f"\nReducing gap from {gap} to {gap//2}")
            gap //= 2

        print("\n\nShell Sort Complete!")
        print("\nFinal array:")
        self.visualize_array()

    def visualize_quicksort(self):
        print("\nPerforming Quicksort:")
        self._visualize_quicksort_helper(0, self.array.size - 1)
        print("\n\nQuicksort Complete!")
        print("\nFinal array:")
        self.visualize_array()

    def _visualize_quicksort_helper(self, low, high):
        if low < high:
            print(f"\nPartitioning array from index {low} to {high}")
            sleep(1)

            pivot = self.array.get_index_data(high)
            print(f"\nPivot element: {pivot}")
            i = low - 1

            for j in range(low, high):
                print(f"\nComparing {self.array.get_index_data(j)} with pivot {pivot}")

                for k in range(self.array.size):
                    if k == high:
                        self.print_array_element(self.array.get_index_data(k), "blue")
                    elif k == j:
                        self.print_array_element(self.array.get_index_data(k), "yellow")
                    elif k <= i:
                        self.print_array_element(self.array.get_index_data(k), "green")
                    else:
                        self.print_array_element(
                            self.array.get_index_data(k), "dark_green"
                        )
                    sleep(0.2)

                if self.array.get_index_data(j) <= pivot:
                    i += 1
                    if i != j:
                        print(
                            f"\nSwapping {self.array.get_index_data(i)} and {self.array.get_index_data(j)}"
                        )
                        temp = self.array.get_index_data(i)
                        self.array.set_index(i, self.array.get_index_data(j))
                        self.array.set_index(j, temp)
                sleep(0.5)

            temp = self.array.get_index_data(i + 1)
            self.array.set_index(i + 1, self.array.get_index_data(high))
            self.array.set_index(high, temp)

            pivot_index = i + 1

            self._visualize_quicksort_helper(low, pivot_index - 1)
            self._visualize_quicksort_helper(pivot_index + 1, high)

    def visualize_merge_sort(self):
        """Visualize merge sort algorithm"""
        print("\nPerforming Merge Sort:")
        self._visualize_merge_sort_helper(0, self.array.size - 1)
        print("\n\nMerge Sort complete!")
        print("\nFinal array:")
        self.visualize_array()

    def _visualize_merge_sort_helper(self, left, right):
        if left < right:
            mid = (left + right) // 2

            print(f"\nDividing array from index {left} to {right}")
            for k in range(self.array.size):
                if left <= k <= right:
                    if k == mid:
                        self.print_array_element(self.array.get_index_data(k), "blue")
                    else:
                        self.print_array_element(self.array.get_index_data(k), "yellow")
                else:
                    self.print_array_element(self.array.get_index_data(k), "dark_green")
                sleep(0.2)
            print()

            self._visualize_merge_sort_helper(left, mid)
            self._visualize_merge_sort_helper(mid + 1, right)

            self._merge(left, mid, right)

    def _merge(self, left, mid, right):
        print(f"\nMerging subarrays from index {left} to {mid} and {mid+1} to {right}")

        left_size = mid - left + 1
        right_size = right - mid

        left_arr = [self.array.get_index_data(left + i) for i in range(left_size)]
        right_arr = [self.array.get_index_data(mid + 1 + i) for i in range(right_size)]

        print("\nSubarrays being merged:")
        print("Left subarray: ", end="")
        for x in left_arr:
            print(f"{Back.YELLOW + Fore.WHITE}[ {x} ]{Style.RESET_ALL}", end=" ")
        print("\nRight subarray: ", end="")
        for x in right_arr:
            print(f"{Back.YELLOW + Fore.WHITE}[ {x} ]{Style.RESET_ALL}", end=" ")
        print("\n")

        i = j = 0
        k = left

        while i < left_size and j < right_size:
            print(f"\nComparing {left_arr[i]} and {right_arr[j]}")
            sleep(0.5)

            if left_arr[i] <= right_arr[j]:
                self.array.set_index(k, left_arr[i])
                i += 1
            else:
                self.array.set_index(k, right_arr[j])
                j += 1

            print("Current array state:")
            for x in range(self.array.size):
                if x == k:
                    self.print_array_element(self.array.get_index_data(x), "blue")
                elif left <= x <= right:
                    self.print_array_element(self.array.get_index_data(x), "yellow")
                else:
                    self.print_array_element(self.array.get_index_data(x), "dark_green")
                sleep(0.2)
            print()
            k += 1

        while i < left_size:
            self.array.set_index(k, left_arr[i])
            print(f"\nCopying remaining left element: {left_arr[i]}")

            for x in range(self.array.size):
                if x == k:
                    self.print_array_element(self.array.get_index_data(x), "blue")
                elif left <= x <= right:
                    self.print_array_element(self.array.get_index_data(x), "yellow")
                else:
                    self.print_array_element(self.array.get_index_data(x), "dark_green")
                sleep(0.2)
            print()

            i += 1
            k += 1

        while j < right_size:
            self.array.set_index(k, right_arr[j])
            print(f"\nCopying remaining right element: {right_arr[j]}")

            for x in range(self.array.size):
                if x == k:
                    self.print_array_element(self.array.get_index_data(x), "blue")
                elif left <= x <= right:
                    self.print_array_element(self.array.get_index_data(x), "yellow")
                else:
                    self.print_array_element(self.array.get_index_data(x), "dark_green")
                sleep(0.2)
            print()

            j += 1
            k += 1


if __name__ == "__main__":
    my_array = Array("int", 5)
    my_array.set_index(0, 4)
    my_array.set_index(1, 1)
    my_array.set_index(2, 3)
    my_array.set_index(3, 5)
    my_array.set_index(4, 2)

    visualizer = ArrayVisualizer(my_array)
    visualizer.visualize_merge_sort()
