### Problem 3

def check_deletion(first, second):
    if len(first) - len(second) != 1:
        return(False)

    for i in range(len(first)):
        if first[:i] + first[i+1:] == second:
            return(True)
    
    return(False)


def check_substitution(first, second):
    if len(first) != len(second):
        return(False)

    counter = 0
    for i in range(len(first)):
        if first[i] == second[i]:
            counter += 1
    
    if counter == len(first) - 1:
        return(True)
    else:
        return(False)

def check_for_edit(first, second):
    return(first == second or check_deletion(first, second) or check_deletion(second, first) or check_substitution(first, second))

check_for_edit("pale", "bale") #substitution
check_for_edit("pale", "bake") #more than one substitution
check_for_edit("pale", "pae") #deletion
check_for_edit("pale", "pe") #more than one deletion
check_for_edit("pae", "pale") #insertion
check_for_edit("pae", "pales") #more than one insertion

check_for_edit("pale", "pale") #no edits