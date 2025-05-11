import unittest


'''
assumes input is 9 characters long for numerical digit without hyphen
'''
def isvalid_ssn(ssn:str) -> bool:
    if ssn is None:
        raise ValueError
    if ssn == '':
        raise ValueError
    if len(ssn) != 9:
        raise ValueError
    if not ssn.isdigit():
        raise ValueError
    return True


'''
assumes input for dob is exactly 8 characters 'YYYYMMDD'
'''
def isvalid_dob(dob:str) -> bool:
    if dob is None:
        raise ValueError
    if dob == '':
        raise ValueError
    if len(dob) != 8:
        raise ValueError
    return True
    

def isvalid_name(f_name, m_name, l_name)->bool:
    if f_name is None:
        raise ValueError
    if l_name is None:
        raise ValueError
    if (f_name == '') or (l_name == ''):
        raise ValueError
    
    return True

class Node:
    def __init__(self, ssn, dob, f_name, m_name, l_name):
        if isvalid_ssn(ssn):
            self.ssn = ssn
        if isvalid_dob(dob):
            self.dob = dob
        if isvalid_name(f_name, m_name, l_name):
            self.f_name = f_name
            self.m_name = m_name
            self.l_name = l_name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):

        new_node = node
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    
    def merge(self, l1:'LinkedList', l2: 'LinkedList') -> 'LinkedList':

        l3 = LinkedList()

        c_1 = l1.head
        c_2 = l2.head

        while c_1 and c_2:
            if c_1.ssn <= c_2.ssn:
                l3.append(c_1)
                c_1 = c_1.next
            else:
                l3.append(c_2)
                c_2 = c_2.next

        while c_1: # c_1 is longer
            l3.append(c_1)
            c_1 = c_1.next

        while c_2: # c_2 is longer
            l3.append(c_2)
            c_2 = c_2.next
            
        return l3
    
    def display(self):
        current = self.head
        while current:
            print(f"{current.ssn}\n")
            current = current.next



class TestLinkedList(unittest.TestCase):

    def test_ssn(self):
        #check empty
        #check len
        #check is digit
        ssn1 = '123456789'
        self.assertEqual(isvalid_ssn(ssn1),True)
        ssn2 = 'foo'
        with self.assertRaises(ValueError):
            isvalid_ssn(ssn2)
        with self.assertRaises(ValueError):
            isvalid_ssn('')

    
    def test_age(self):
        #check empty
        #check None
        #ceck len

        dob1 = '20000101'
        self.assertEqual(isvalid_dob(dob1), True)
        dob2 = '2000/01/01'
        dob3 = None
        
        with self.assertRaises(ValueError):
            isvalid_dob(dob2)
        
        with self.assertRaises(ValueError):
            isvalid_dob('')

        with self.assertRaises(ValueError):
            isvalid_dob(dob3)

    
    def test_name(self):
        #check empty

        #check None

        f_name1 = ''
        m_name = None
        l_name = None

        with self.assertRaises(ValueError):
            isvalid_name(f_name1, m_name, l_name)
        
        self.assertEqual(isvalid_name('joh',None,'doe'),True)

    def test_empty_list(self):
        # test merge with empty list
        l1 = LinkedList()
        l2 = LinkedList()

        n1 = Node('123456789', '19700101', 'john', None, 'doe')
        l2.append(n1)

        merged = l1.merge(l1,l2)
        self.assertEqual(merged.head, n1)


    def test_sample1(self):
        l1 = LinkedList()
        l2 = LinkedList()
        n1 = Node('123456789', '19700101', 'john', None, 'doe')
        n2 = Node('003456789', '19700101', 'alice', None, 'doe')
        l2.append(n1)
        l1.append(n2)
        merged = l1.merge(l1,l2)
        merged.display()
        self.assertEqual(merged.head, n2)
    

    def test_sample2(self):
        pass


if __name__ == "__main__":
    unittest.main()