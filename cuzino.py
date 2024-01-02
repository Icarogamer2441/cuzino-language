import time
import subprocess

def talk(*message):
  print(*message)

def ifs(condition1, condition2, *code):
  if variaveis[condition1] == variaveis[condition2]:
    execute_cuzino(*code)

def vs(varname):
  if varname in variaveis:
    valor = variaveis.get(varname)
    print(valor)
  else:
    print('unknown varname')

def whiles(condition, *code):
  while condition:
    execute_cuzino(*code)

variaveis = {}
functions = {}

def addtext(varname, text):
  variaveis[varname] = variaveis[varname] + text

def execfilee(filename):
  with open(filename + '.cuz', 'r') as file:
    code = file.read()
  execute_cuzino(code)

def talkfile(filename):
  with open(filename, 'r') as file:
    content = file.read()
  print(content)

def cop(question, varname):
  if varname in variaveis:
    variaveis[varname] = input(question)
  else:
    print('uknown var')

def read(filename, varname):
  if varname in variaveis:
    with open(filename, 'r') as file:
      variaveis[varname] = file.read()
  else:
    print('unknown file or variable')

def cup(seconds):
  time.sleep(float(seconds))

def write(filename, code):
  with open(filename, 'w') as f:
    f.write(code)

def append(filename, code):
  with open(filename, 'a') as f:
    f.write(code)

def fors(times, code):
  for i in range(int(times)):
    execute_cuzino(code)

def cip(typename, varname, value):
  if typename == 'str':
    variaveis[varname] = str(value)
  elif typename == 'boo':
    variaveis[varname] = bool(value)
  elif typename == 'int':
    variaveis[varname] = int(value)
  elif typename == 'flo':
    variaveis[varname] = float(value)
  else:
    assert False, 'uknown var type'

def fun(funcname,code):
  if len(funcname) >= 2:
    functions[funcname] = code
  else:
    assert False, "use more than 1 character to write a function name"

def cfun(funcname):
  if funcname in functions:
    execute_cuzino(functions[funcname])
  else:
    assert False, f"no function named {funcname}"

def helps():
    print("Functions available in the language:")
    print("talk(message): Displays a message on the screen.")
    print("ifs(condition1, condition2){code}: Executes a code block if two conditions are equal.")
    print("vs varname: Displays the value associated with a variable.")
    print("whiles(condition){code}: Executes a code block while the condition is true.")
    print("addtext(varname, text): Adds text to the value of a variable.")
    print("importfile filename: Executes the code from a .cuz file.")
    print("talkfile filename: Displays the content of a file.")
    print("cop question (varname): Asks the user a question and saves the response in a variable.")
    print("read(filename)>varnams<: Reads the content of a file and stores it in a variable.")
    print("cup<([seconds])>: Pauses the program execution for a specified number of seconds.")
    print("write(filename)>code<: Writes code content to a file.")
    print("append(filename,code): Appends code content to the end of a file.")
    print("execlines<code1, code2>: executes two codes in one line. can be used on the whiles and ifs function")
    print("cip(type)<varname, value>:creates a variable with the tyoe you write. types: str, boo, int, flo")
    print("terminal{terminal comand}: executes a terminal command")
    print("clear: clear the terminal")
    print("fors<times_to_repeat>[cuzino_code]: repeats the code for some time")
    print("fun funcname {code}: defines a function with the cuzino code")
    print('cfun(funcname): call a function')

def terminal(command):
  subprocess.run(command, shell=True)

def writehtml(code):
  with open('index.html', 'w') as f:
    f.write(code)

def appendhtml(code):
  with open('index.html', 'a') as f:
    f.write(code)

def execute_cuzino(code):
  lines = code.split('\n')
  
  for index, line in enumerate(lines):
    if line.startswith("talk"):
      if '(' in line and ')' in line:
        message = line.split('(')[1].split(')')[0].strip()
        talk(message)
    elif line.startswith("ifs"):
      condition1 = line.split('(')[1].split(',')[0].strip('\"\'')
      condition2 = line.split(',')[1].split(')')[0].strip()
      coding = line.split('{')[1].split('}')[0].strip()
      ifs(condition1, condition2, coding)
    elif line.startswith("cip"):
      typename = line.split('(')[1].split(')')[0].strip('\"\'')
      name = line.split('<')[1].split(',')[0].strip('\"\'')
      value = line.split(',')[1].split('>')[0].strip('\"\'')
      
      cip(typename, name, value)
    elif line.startswith("vs"):
      varname = line.split()[1].strip('\"\'')
      vs(varname)
    elif line.startswith('whiles'):
      condition = line.split('(')[1].split(')')[0].strip()
      coding = line.split('{')[1].split('}')[0].strip()
      whiles(condition, coding)
    elif line.startswith('addtext'):
      varname = line.split('(')[1].split(',')[0].strip()
      text = line.split(',')[1].split(')')[0].strip()
      addtext(varname, text)
    elif line.startswith('importfile'):
      filename = line.split(' ')[1].strip()
      execfilee(filename)
    elif line.startswith('talkfile'):
      filename = line.split()[1].strip('\"\'')
      talkfile(filename)
    elif line.startswith('cop'):
      question = line.split()[1].strip('\"\'')
      varname = line.split('(')[1].split(')')[0].strip()
      cop(question, varname)
    elif line.startswith('read'):
      filename = line.split('(')[1].split(')')[0].strip('\"\'')
      varname = line.split('>')[1].split('<')[0].strip('\"\'')
      read(filename, varname)
    elif line.startswith('cup'):
      seconds = line.split('<([')[1].split('])>')[0].strip('\"\'')
      cup(seconds)
    elif line.startswith('write'):
      filename = line.split('(')[1].split(')')[0].strip('\"\'')
      code = line.split('>')[1].split('<')[0].strip('\"\'')
      write(filename, code)
    elif line.startswith('append'):
      filename = line.split('(')[1].split(',')[0].strip('\"\'')
      code = line.split(',')[1].split(')')[0].strip('\"\'')
      append(filename, code)
    elif line.startswith('help'):
      helps()
    elif line.startswith('execlines'):
      code1 = line.split('<')[1].split(',')[0].strip('\"\'')
      code2 = line.split(',')[1].split('>')[0].strip('\"\'')
      execute_cuzino(code1)
      execute_cuzino(code2)
    elif line.startswith('terminal'):
      split_line = line.split('{')
      if len(split_line) > 1:
        command = split_line[1].split('}')[0].strip('\"\'')
        terminal(command)
      else:
        print("Comando 'terminal' não está formatado corretamente")
    elif line.startswith('clear'):
      terminal('clear')
    elif line.startswith('fors'):
      times = line.split('<')[1].split('>')[0].strip('\"\'')
      code = line.split('[')[1].split(']')[0].strip('\"\'')
      fors(times, code)
    elif line.startswith('fun'):
      funcname = line.split()[1].strip('\"\'')
      code = line.split('{')[1].split('}')[0].strip('\"\'')
      fun(funcname, code)
    elif line.startswith('cfun'):
      funcname = line.split('(')[1].split(')')[0].strip('\"\'')


def execfileex(filename):
  with open(filename + '.cuzx', 'r') as file:
    code = file.read()
  execute_cuzinox(code)

def execute_cuzinox(code):
  lines = code.split('\n')
  
  for index, line in enumerate(lines):
    if line.startswith('<doc>'):
      writehtml('<!DOCTYPE html>')
    elif line.startswith('tag'):
      htmlcode = line.split('(')[1].split(')')[0].strip('\"\'')
      appendhtml(htmlcode + '\n')

file_name = input('.cuz file name (use only the name not the name.cuz) > ')
if file_name.lower() == 'x':
  file_name = input('type your file .cuzx name but without the .cuzx > ')
  execfileex(file_name)
elif file_name.lower() == 'helpx':
  print('you need to have a html file named index.html to work and have a .cuzx file and write x in the name of the .cuz file to open the .cuzx file executor')
  print('<doc>: writes the <!DOCTYPE html> into the index.html file')
  print('tag(html_code): writes html code into the index.html file')
  
else:
  execfilee(file_name)
