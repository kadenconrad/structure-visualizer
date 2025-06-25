import pytest
from src.models.singly_LL import SLLNode, SinglyLL
from src.models.doublyLL import DLLNode, DoublyLL

class TestSLLNode:
    def test_node_creation(self):
        node = SLLNode(42)
        assert node.data == 42
        assert node.next is None
    
    def test_node_with_different_data_types(self):
        node_int = SLLNode(5)
        node_str = SLLNode("hello")
        node_list = SLLNode([1, 2, 3])
        
        assert node_int.data == 5
        assert node_str.data == "hello"
        assert node_list.data == [1, 2, 3]


class TestSinglyLL:
    
    def test_empty_list_creation(self):
        sll = SinglyLL()
        assert sll.head is None
        assert sll.tail is None
    
    def test_display_empty_list(self, capsys):
        sll = SinglyLL()
        sll.display()
        captured = capsys.readouterr()
        assert captured.out == "Nothing to display.\n"
    
    def test_append_single_element(self):
        sll = SinglyLL()
        sll.append(42)
        
        assert sll.head is not None
        assert sll.tail is not None
        assert sll.head == sll.tail
        assert sll.head.data == 42
        assert sll.head.next is None
    
    def test_append_multiple_elements(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        assert sll.head.data == 1
        assert sll.head.next.data == 2
        assert sll.head.next.next.data == 3
        assert sll.tail.data == 3
        assert sll.tail.next is None
    
    def test_append_node_object(self):
        sll = SinglyLL()
        node = SLLNode(99)
        sll.append(node)
        
        assert sll.head == node
        assert sll.tail == node
        assert sll.head.data == 99
    
    def test_prepend_single_element(self):
        sll = SinglyLL()
        sll.prepend(42)
        
        assert sll.head is not None
        assert sll.tail is not None
        assert sll.head == sll.tail
        assert sll.head.data == 42
    
    def test_prepend_multiple_elements(self):
        sll = SinglyLL()
        sll.prepend(1)
        sll.prepend(2)
        sll.prepend(3)
        
        assert sll.head.data == 3
        assert sll.head.next.data == 2
        assert sll.head.next.next.data == 1
        assert sll.tail.data == 1
    
    def test_prepend_node_object(self):
        sll = SinglyLL()
        node = SLLNode(99)
        sll.prepend(node)
        
        assert sll.head == node
        assert sll.tail == node
        assert sll.head.data == 99
    
    def test_search_existing_value(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        result = sll.search(2)
        assert result.data == 2
        assert result == sll.head.next
    
    def test_search_nonexistent_value(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        with pytest.raises(ValueError, match="Value 99 not found in list."):
            sll.search(99)
    
    def test_search_empty_list(self):
        sll = SinglyLL()
        
        with pytest.raises(ValueError, match="Value 1 not found in list."):
            sll.search(1)
    
    def test_insert_after_value(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(3)
        
        sll.insert_after(1, 2)
        
        assert sll.head.data == 1
        assert sll.head.next.data == 2
        assert sll.head.next.next.data == 3
        assert sll.tail.data == 3
    
    def test_insert_after_node(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(3)
        
        node = sll.search(1)
        sll.insert_after(node, 2)
        
        assert sll.head.data == 1
        assert sll.head.next.data == 2
        assert sll.head.next.next.data == 3
    
    def test_insert_after_tail(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        
        sll.insert_after(2, 3)
        
        assert sll.tail.data == 3
        assert sll.head.next.next.data == 3
    
    def test_insert_after_empty_list(self):
        sll = SinglyLL()
        sll.insert_after(None, 42)
        
        assert sll.head.data == 42
        assert sll.tail.data == 42
        assert sll.head == sll.tail
    
    def test_remove_after_value(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        sll.remove_after(1)
        
        assert sll.head.data == 1
        assert sll.head.next.data == 3
        assert sll.tail.data == 3
    
    def test_remove_after_node(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        node = sll.search(1)
        sll.remove_after(node)
        
        assert sll.head.data == 1
        assert sll.head.next.data == 3
    
    def test_remove_after_none_removes_head(self):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        sll.remove_after(None)
        
        assert sll.head.data == 2
        assert sll.head.next.data == 3
        assert sll.tail.data == 3
    
    def test_remove_after_none_single_element(self):
        sll = SinglyLL()
        sll.append(1)
        
        sll.remove_after(None)
        
        assert sll.head is None
        assert sll.tail is None
    
    def test_display_populated_list(self, capsys):
        sll = SinglyLL()
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        sll.display()
        captured = capsys.readouterr()
        assert captured.out == "\n[1, 2, 3]\n"


class TestDLLNode:
    def test_node_creation(self):
        node = DLLNode(42)
        assert node.data == 42
        assert node.next is None
        assert node.prev is None
    
    def test_node_with_different_data_types(self):
        node_int = DLLNode(5)
        node_str = DLLNode("hello")
        node_list = DLLNode([1, 2, 3])
        
        assert node_int.data == 5
        assert node_str.data == "hello"
        assert node_list.data == [1, 2, 3]


class TestDoublyLL:
    def test_empty_list_creation(self):
        dll = DoublyLL()
        assert dll.head is None
        assert dll.tail is None
    
    def test_display_empty_list(self, capsys):
        dll = DoublyLL()
        dll.display()
        captured = capsys.readouterr()
        assert captured.out == "Nothing to display.\n"
    
    def test_append_single_element(self):
        dll = DoublyLL()
        dll.append(42)
        
        assert dll.head is not None
        assert dll.tail is not None
        assert dll.head == dll.tail
        assert dll.head.data == 42
        assert dll.head.next is None
        assert dll.head.prev is None
    
    def test_append_multiple_elements(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        # Check forward links
        assert dll.head.data == 1
        assert dll.head.next.data == 2
        assert dll.head.next.next.data == 3
        assert dll.tail.data == 3
        
        # Check backward links
        assert dll.tail.prev.data == 2
        assert dll.tail.prev.prev.data == 1
        assert dll.head.prev is None
        assert dll.tail.next is None
    
    def test_append_node_object(self):
        dll = DoublyLL()
        node = DLLNode(99)
        dll.append(node)
        
        assert dll.head == node
        assert dll.tail == node
        assert dll.head.data == 99
    
    def test_prepend_single_element(self):
        dll = DoublyLL()
        dll.prepend(42)
        
        assert dll.head is not None
        assert dll.tail is not None
        assert dll.head == dll.tail
        assert dll.head.data == 42
    
    def test_prepend_multiple_elements(self):
        dll = DoublyLL()
        dll.prepend(1)
        dll.prepend(2)
        dll.prepend(3)
        
        # Check forward links
        assert dll.head.data == 3
        assert dll.head.next.data == 2
        assert dll.head.next.next.data == 1
        assert dll.tail.data == 1
        
        # Check backward links
        assert dll.tail.prev.data == 2
        assert dll.tail.prev.prev.data == 3
    
    def test_prepend_node_object(self):
        dll = DoublyLL()
        node = DLLNode(99)
        dll.prepend(node)
        
        assert dll.head == node
        assert dll.tail == node
    
    def test_search_existing_value(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        result = dll.search(2)
        assert result.data == 2
        assert result == dll.head.next
    
    def test_search_nonexistent_value(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        with pytest.raises(ValueError, match="Value 99 not found in list."):
            dll.search(99)
    
    def test_search_empty_list(self):
        dll = DoublyLL()
        
        with pytest.raises(ValueError, match="Value 1 not found in list."):
            dll.search(1)
    
    def test_insert_after_value(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(3)
        
        dll.insert_after(1, 2)
        
        # Check forward links
        assert dll.head.data == 1
        assert dll.head.next.data == 2
        assert dll.head.next.next.data == 3
        
        # Check backward links
        assert dll.tail.prev.data == 2
        assert dll.tail.prev.prev.data == 1
    
    def test_insert_after_node(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(3)
        
        node = dll.search(1)
        dll.insert_after(node, 2)
        
        # Check the new node's links
        new_node = dll.head.next
        assert new_node.data == 2
        assert new_node.prev.data == 1
        assert new_node.next.data == 3
    
    def test_insert_after_tail(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        
        dll.insert_after(2, 3)
        
        assert dll.tail.data == 3
        assert dll.tail.prev.data == 2
        assert dll.tail.next is None
    
    def test_insert_after_none(self):
        dll = DoublyLL()
        dll.insert_after(None, 42)
        
        assert dll.head.data == 42
        assert dll.tail.data == 42
        assert dll.head == dll.tail
    
    def test_remove_value_middle_node(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        node_to_remove = dll.search(2)
        dll.remove_value(node_to_remove)
        
        assert dll.head.data == 1
        assert dll.head.next.data == 3
        assert dll.tail.data == 3
        assert dll.tail.prev.data == 1
        
        # Check removed node is cleaned up
        assert node_to_remove.next is None
        assert node_to_remove.prev is None
    
    def test_remove_value_head_node(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        head_node = dll.head
        dll.remove_value(head_node)
        
        assert dll.head.data == 2
        assert dll.head.prev is None
        assert dll.tail.data == 3
        
        # Check removed node is cleaned up
        assert head_node.next is None
        assert head_node.prev is None
    
    def test_remove_value_tail_node(self):
        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        tail_node = dll.tail
        dll.remove_value(tail_node)
        
        assert dll.head.data == 1
        assert dll.tail.data == 2
        assert dll.tail.next is None
        
        # Check removed node is cleaned up
        assert tail_node.next is None
        assert tail_node.prev is None
    
    def test_remove_value_single_node(self):
        dll = DoublyLL()
        dll.append(42)
        
        node = dll.head
        dll.remove_value(node)
        
        assert dll.head is None
        assert dll.tail is None
        
        # Check removed node is cleaned up
        assert node.next is None
        assert node.prev is None
    
    def test_display_populated_list(self, capsys):

        dll = DoublyLL()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        dll.display()
        captured = capsys.readouterr()
        assert captured.out == "\n[1, 2, 3]\n"


# Integration tests
class TestLinkedListIntegration:
    
    def test_singly_linked_list_complex_operations(self):
        sll = SinglyLL()
        
        # Build list: 1 -> 2 -> 3
        sll.append(1)
        sll.append(2)
        sll.append(3)
        
        # Prepend 0: 0 -> 1 -> 2 -> 3
        sll.prepend(0)
        
        # Insert 1.5 after 1: 0 -> 1 -> 1.5 -> 2 -> 3
        sll.insert_after(1, 1.5)
        
        # Remove node after 1.5 (removes 2): 0 -> 1 -> 1.5 -> 3
        sll.remove_after(1.5)
        
        # Verify final state
        values = []
        current = sll.head
        while current:
            values.append(current.data)
            current = current.next
        
        assert values == [0, 1, 1.5, 3]
        assert sll.tail.data == 3
    
    def test_doubly_linked_list_complex_operations(self):
        dll = DoublyLL()
        
        # Build list: 1 <-> 2 <-> 3
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        # Prepend 0: 0 <-> 1 <-> 2 <-> 3
        dll.prepend(0)
        
        # Insert 1.5 after 1: 0 <-> 1 <-> 1.5 <-> 2 <-> 3
        dll.insert_after(1, 1.5)
        
        # Remove 2: 0 <-> 1 <-> 1.5 <-> 3
        node_2 = dll.search(2)
        dll.remove_value(node_2)
        
        # Verify final state (forward)
        values_forward = []
        current = dll.head
        while current:
            values_forward.append(current.data)
            current = current.next
        
        # Verify final state (backward)
        values_backward = []
        current = dll.tail
        while current:
            values_backward.append(current.data)
            current = current.prev
        
        assert values_forward == [0, 1, 1.5, 3]
        assert values_backward == [3, 1.5, 1, 0]