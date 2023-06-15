# %%
import re
import sys

# %%
def replace_latex_math_mode(text):
    """
    Replaces LaTeX math mode expressions ($...$) with [tex: ...] in a given text.
    """
    # Regular expression to match LaTeX math mode expressions
    latex_math_mode_pattern = r'\$(.*?)\$'
    # Replace LaTeX math mode expressions with [tex: ...]
    replaced_text = re.sub(latex_math_mode_pattern, r'[tex: \1] ', text)
    return replaced_text

def replace_extension(filename):
    # Check if the file has a ".md" extension
    if filename.endswith(".md"):
        # Replace ".md" with "_hatena.md"
        replaced_filename = filename.replace(".md", "_hatena.md")
        return replaced_filename
    else:
        # If the file does not have a ".md" extension, return the original filename
        return filename
# %% GPT
# import re

def rewrite_underscores(expression):
    # Regular expression pattern to match the expression enclosed in $'s
    pattern = r'\$([^$]+)\$'

    # Find all matches of the pattern in the expression
    matches = re.findall(pattern, expression)

    # Loop through each match and replace underscores with \_
    for match in matches:
        # Replace underscores with \_
        replaced = match.replace('_', r'\_')
        # added manually
        # brackets escaped.
        replaced = replaced.replace('[', r'\\[')
        replaced = replaced.replace(']', r'\\]')
        
        # Replace the original match with the replaced one in the expression
        expression = expression.replace(f'${match}$', f'${replaced}$')

    return expression

# %%
args = sys.argv
# file_name = input()#"01.md"
file_name = args[1]#"01.md"
with open(file_name) as f:
    latex_text = f.read()
    # $ underscores $
    replaced_text = rewrite_underscores(latex_text)
    # [tex: ]
    replaced_text = replace_latex_math_mode(replaced_text)    
    # file name
    replaced_filename = replace_extension(file_name)

with open(replaced_filename, 'w') as f:
    f.write(replaced_text)

# %%
################
# memo
################
def find_displaymath(x):
    return re.findall(r"\$\$.+\$\$", x)
# %%
def find_inlinemath(x):
    if find_displaymath(x):
        raise ValueError("include display math mode")
    
    y = re.findall(r"\$[^\$]+\$", x)
    return y

# %%
# %%
def search_inlinemath(x):
    if find_displaymath(x):
        raise ValueError("include display math mode")
    
    y = re.search(r"\$[^\$]+\$", x)
    return y
# a = "$ a $, $ \gamma_{0}$, \n $b$"
# %%