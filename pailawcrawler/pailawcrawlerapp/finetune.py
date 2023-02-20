import os

def combine_text_files(directory):
    text = ''
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as f:
                text += f.read() + '\n'
    return text