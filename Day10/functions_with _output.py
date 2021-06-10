# Function with output
# Now here we  will use titile() which is used for Making every first letter  of a word  captial_case

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"

print(format_name("fazal", "MAHMOOD"))