

def swap_name(name):
    """Swap the first name and the last name of a person's name."""
    name_list = name.split()
    return name_list[1] + ', ' + name_list[0]
