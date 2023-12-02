def replace_in_list(my_list, idx, element):
    # check if idx is valid
    if idx >= 0 and idx < len(my_list):
        # replace the element at idx with the new element
        my_list[idx] = element
    # return the modified or original list
    return my_list
