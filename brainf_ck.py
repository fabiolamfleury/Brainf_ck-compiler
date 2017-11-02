import click

# dictonary from brainfuck commands to c
bf_to_c_dict = {
    '+': '\t++(*ptr);\n',
    '-': '\t--(*ptr);\n',
    '>': '\t++ptr;\n',
    '<': '\t--ptr;\n',
    '.': '\tprintf("%c",(*ptr));\n',
    ',': '\t*ptr = getchar();\ngetchar();\n',
    '[': '\twhile(*ptr) {\n',
    ']': '\t}\n'
}

"""
click commands are used to get arguments on command line
first argument is the source file in brainfuck
second argument "-o file_name" is the file in c that will receive
the translation
"""
@click.command()
@click.argument('source', type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))
def parser(source, o):
    """
    converts code in brainfuck to c code
    """
    program = ("#include <stdio.h>\n#include <stdlib.h>\n int main(){"
            "\n\tunsigned char *memory = malloc(sizeof(char)*30000);\n"
               "\n\tunsigned char *ptr =  &memory[0];\n"
              )
    data = source.read()
    for char in data:
        if char in bf_to_c_dict:
            program += bf_to_c_dict[char]

    program += '\n    return 0;\n}'

    o.write(program)
    o.flush()

if __name__ == '__main__':
    parser()
