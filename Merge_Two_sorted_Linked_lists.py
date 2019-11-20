from SingleLinkedList import SingleLinkedList as ll

def merge(list_1, list_2):
    l1 = ll()
    j = 0
    i = 0
    # list 1 nodes
    while i >= 0 and i <= len(list_1)-1 and j <= len(list_2) -1:        
        if list_1[i] < list_2[j]:
            l1.insert_a_node_at_end(list_1[i])
            #print('Less : ', list_1[i], ' < ', list_2[j])
            i += 1
        else:
            l1.insert_a_node_at_end(list_2[j])
            #print('greater : ', list_1[i], ' > ',list_2[j])
            j += 1
            
    # if any nodes left in the list_1
    while i != len(list_1):
        l1.insert_a_node_at_end(list_1[i])
        i += 1
    # if any nodes left in the list_2
    while j != len(list_1):
        l1.insert_a_node_at_end(list_2[j])
        j += 1
    print('----------------------------------------------------')
    l1.print_list()
    print('\n----------------------------------------------------')



list_1 = [4,5,7,9,8]
list_2 = [1,2,3,6,10]
merge(list_1, list_2)
