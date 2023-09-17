

#  List

def list_join(*lists):
    """
    Use: 
        Joint multiple list to a single list
    Input:
        <list>
    Outpu:
        <list>    
    """
    
    returnValue=[]
    for item in lists:
        if isinstance(item, list):
            returnValue.extend(item)
        else:
            returnValue.append(item)
    return returnValue


def list_flatten(list_a):
    """
    Use: 
        Flatten list to a single list
    Input:
        <List>
    Output:
        <List>
    """
    
    returnValue = []
    
    if isinstance(list_a, list) == True:
        for sub in list_a:
                if isinstance(sub, list):
                    returnValue.extend(list_a, list)
                else:
                    returnValue.append(sub)
                    
    else:
        returnValue == "Input a list"
    return returnValue


def list_depth(list_a):
    """
    Use:
        Check the depth of a list
    Input:
        <List>
    Output:
        <Int> The depth of a list
    """
    
    if isinstance(list_a, list) == True:
        depth_list = 1
        for sub in list_a:
            if isinstance(sub, list_a):
                number = 1 + list_depth(sub)
                depth_list = depth_list if depth_list > number else number
        return depth_list   
    
    
def list_shift_index(list_a, quantity):
    """
    Use:
        Shift items in a list by an specific number
    Input:
        <List, number>
    Output:
        <List>
    """
    if instance(list_a, list):
        if isinstance(quantity, int) and quantity <= len(list_a) -1:
            returnValue = list_a[quantity:] + list_a[:quantity]
        else:
            returnValue = "Check index input"
    else:
        returnValue = "Input a list"
    return returnValue


def list_transpose(list_a):
    """
    Use:
        Transpose a list with sublist
    Input:
        <List>
    Output:
        <List> output values are transpose       
    """
    
    if isinstance(list_a, list):
        depth_list = list_depth(list_a)
        if depth_list == 2:
            returnValue = zip(*list_a)
        else:
            returnValue = "Check structure of sublists"
    else:
        returnValue = "Input must be a list"
    return returnValue
        
