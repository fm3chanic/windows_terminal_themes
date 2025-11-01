# Disclaimer:
# this code was made to work with specific files in mind
# HTML files based on "color_scheme_template.html" 
# you can find this template in https://github.com/fm3chanic/color_schemes
# the target files are "winterm_scheme_template.json" and "winterm_theme_template.json"
# you can find this template in https://github.com/fm3chanic/windows_terminal_themes

import pandas as pd
import sys

#function for replacing values from the templates with the values from the scheme
def create_files(tab1_replace, tab2_replace, tab1_values, tab2_values, templates, output_files, index):
    # reading the template
    template_file = templates[index]
    f = open(template_file, 'r', encoding='utf-8')
    content = f.read()
    f.close()

    #iterating through lists
    #mapped expression will be replaced with color codes accordingly
    for i in range(9):
        if index != 0:
            tmpstr = tab1_values[i]
            tmpstr = tmpstr.upper()
            content = content.replace(tab1_replace[i], tmpstr)
        else:          
            content = content.replace(tab1_replace[i], tab1_values[i])

    if index == 0:
        for i in range(6):
            content = content.replace(tab2_replace[i], tab2_values[i])    

    if index != 0 and int(sys.argv[2]) == 1:
        content = content.replace('AppMode', 'dark')
    else:
        content = content.replace('AppMode', 'light')

    content = content.replace('ThemeName', sys.argv[1])


    # creating the completed output file
    output_file = output_files[index]
    f = open(output_file, 'w', encoding='utf-8')
    f.write(content)
    f.close()
    
#define required lists
tab1_values = []
tab2_values = []

#define values for replacement
tab1_replace = ['BackGround1','BackGround2','BackGround3','ForeGround1','ForeGround2','ForeGround3','HighLight1','HighLight2','HighLight3']
tab2_replace = ['Syn1','Syn2','Syn3','Syn4','Syn5','Syn6']

#define values for file creation
input_file = f'{sys.argv[1]}.html'
scheme_output_file = f'{sys.argv[1]}_scheme.json'
theme_output_file = f'{sys.argv[1]}_theme.json'
templates = ['winterm_scheme_template.json','winterm_theme_template.json']
output_files = [scheme_output_file,theme_output_file]

#output of read_html() is a list with two data frames
df = pd.read_html(input_file, header=0)

#copying data frames to create dedicated lists
tab1 = df[0]
tab1_values = tab1.iloc[0:9,1].tolist()

tab2 = df[1]
tab2_values = tab2.iloc[0:7,1].tolist()

#loops the replacement of values, because there are 2 templates
for i in range(2):
    index = i
    create_files(tab1_replace, tab2_replace, tab1_values, tab2_values, templates, output_files, index)