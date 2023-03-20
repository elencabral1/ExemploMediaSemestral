linguagem = input ('Linguagem: ')

match linguagem:
    case 'Python'|'python'|'PYTHON':
        print('Modelos de IA')
    case 'Java'|'JAVA'|'java':
        print('Mobile/backend')
    case 'JavaScript'|'javascript'|'JAVASCRIPT':
        print('Web')
    case 'PHP'|'php'|'Php':
        print('backend')
    case 'Swift'|'SWIFT'|'swift':
        print('mobile iOS')
    case _:
        print('Nenhuma linguagem listada!')
