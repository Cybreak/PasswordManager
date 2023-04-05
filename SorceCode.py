import os
import colorama


founddata = ''
def GetEP(name=str):
    global founddata
    file = open('EP.txt', 'r')
    data = file.read()
    data = data.split(sep='///')
    for i in data:
        d = i.split(sep='---')
        if d[0] == name:
            founddata = d
    
    file.close()
    return(founddata[1], founddata[2])
    

def addEP(name=str, email=str, password=str):
    if '' in [name, email, password]:
        return(False)
    file = open('EP.txt', 'r')
    filedata = file.read()
    file.close()
    
    file = open('EP.txt', 'w')
    file.write(f'{filedata}///{name}---{email}---{password}')
    file.close()
    return(True)
    

def main():
    while True:
        os.system('cls')
        print(colorama.Fore.CYAN + """
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")
        pickinput = input('GetEP[1]/AddEP[2]: ')
        if pickinput == '1':
            name = input('Name: ')
            email, password = GetEP(name)
            print(f'Email: {email}   Password: {password}')
            input()
        
        if pickinput == '2':
            name = input('Name: ')
            email = input('Email: ')
            password = input('Password: ')
            con = addEP(name, email, password)
            if con:
                print(colorama.Fore.GREEN + 'Success')
                input()
            else:
                print(colorama.Fore.RED + 'Error')
                input()







main()