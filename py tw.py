import textwrap

def wrap(string, max_width):
    # textwrap.fill wraps the text and returns a single string 
    # with newline characters inserted at the specified width.
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
