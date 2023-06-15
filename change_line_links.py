# %% GPT change_line_links
import sys
# %%

def rewrite_string_links(text):
    # Replace " https:" with "  \nhttps:"
    rewritten_text = text.replace(' https:', '  \nhttps:')

    # Replace " http:" with "  \nhttp:"
    rewritten_text = rewritten_text.replace(' http:', '  \nhttp:')

    return rewritten_text

"""
################
test code
################
input_text = 'This is a https: example. Another http: example.'
rewritten_text = rewrite_string(input_text)
print(rewritten_text)
"""

# %%
def main(file_name):
    with open(file_name) as f:
        markdown_text = f.read()
        # $ underscores $
        replaced_text = rewrite_string_links(markdown_text)
        # file name
        # replaced_filename = replace_extension(file_name)
        replaced_filename = file_name

    with open(replaced_filename, 'w') as f:
        f.write(replaced_text)


args = sys.argv
file_name = args[1]
main(file_name)
