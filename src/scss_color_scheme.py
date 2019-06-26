import os, re, sys

def regexify(input):
    input = re.sub("\(", "\\(", input)
    input = re.sub("\.", "\\.", input)
    input = re.sub("\)", "\\)", input)
    input = re.sub("\$", "\\$", input)
    return input

def retrieveColors(item, i):
    used_colors = [] # Create an empty set to store found colors
    file_prefix = re.findall(r'(?<=/)[\w\d\-_]+(?=\..*)|(?<!/)[\w\d]+(?=\..*)', item) # File name without extension
    output = '' # Output for the given file
    with open(item, "r") as source:
        content = source.read() #read file content
    
        colors_hex = re.findall(r'\#[\d\w]{6}(?=\s?\;)', content)
        colors_rgba = re.findall(r'rgba\s?\(.*?\)', content)
        #find all occurrences of hex and rgba color strings

    for c_hex in colors_hex: # Iterate through hex colors in file
        if c_hex not in used_colors: # Eliminate Duplicates
            used_colors.append(c_hex)

    for c_rgba in colors_rgba: #Iterate through rgba colors in file
        if c_rgba not in used_colors: # Eliminate duplicates
            used_colors.append(c_rgba)

    for color in used_colors:
        i += 1
        output += f"${file_prefix[0]}_{i}:{color};\n"
        # Add the color variable into output
        try:
            content = re.sub(regexify(color),f"${file_prefix[0]}_{i}", content)
        except Exception as e:
            print(e)
        # Substitute values in source file for variable

    with open(item, "w") as source_file:
        source_file.write(content) # Rewrite the source file
    
    return output

def main():
    files = os.listdir() #get the file list in current folder
    output = ''
    recursive = False
    supported_files = ('.scss', '.less', '.css', '.sass')
    if not 1 < len(sys.argv) < 4:
        print("Please, use with argument -h or --help to see usage")    
        return

    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("\n\
        Usage: python create_color_scheme.py <target scss scheme file> [-r]\n\
        Example: python create_color_scheme.py colors.scss\n\
        NOTE: This app supports .scss, .less, .sass and .css format\n\
        Run with second argument -r to do recursive search")
        return

    if len(sys.argv) == 3 and sys.argv[2] == '-r':
        recursive = True

    i = 0 #counter
    for item in files:
        if str(item).endswith(supported_files):
            print(f'Working on: {item}')
            # Iterate through files, if it is not the target scheme file,
            #  add file name to target and add output from retrieveColors()
            if not item == sys.argv[1]:
                output += f"//{item}\n" + retrieveColors(item, i) + "\n"
        
        elif not "." in str(item) and recursive:
            # Iterate through files in a folder
            for folder_item in os.listdir(item):
                print(f'Working on: {item}/{folder_item}')
                output += f"//{item}/{folder_item}\n" + retrieveColors(item+"/"+folder_item, i) + "\n"

    with open(sys.argv[1], 'w+') as scheme_file:
        scheme_file.write(output) # Write the final output to the scheme file

if __name__ == '__main__':
    main()