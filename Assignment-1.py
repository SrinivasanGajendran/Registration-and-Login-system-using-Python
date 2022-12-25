import json
special_character = """[~!@#$%^&*()_+-={};':",/?><]"""

def password(passwd):
    val = True
    if len(passwd) == 0:
        print("Pasword Cannot Be Empty")
        val = False
    if len(passwd) < 5 and len(passwd) > 16:
        print('length should be s-16 Characters ')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in special_character for char in passwd):
        print('''Password should have at least one of the symbols ~!@#$%^&*()_+-={};':",/?><''')
        val = False
    if val:
        return val



def usr_nme(user_name):
    if '@' in user_name and '.' in user_name:
        index = user_name.index('@')
        domain = user_name[index+1:]
        name = user_name[:index]
        if name.isalpha() and special_character not in domain and domain.count('.') == 1 :
            return True
        else:
            print("Invalid Username")
    else:
        print("invalid username")

def writing():
    if usr_nme(user_name) and password(passwd) == True:
        val1 = {user_name:passwd}
        with open('D:/Practice/Guvi.txt', 'a+') as g:
            g.seek(0)
            red = g.read()
            js1 = json.dumps(red)
            if user_name in js1:
                print("Already Registered Please Login")
            else:
                with open('D:/Practice/Guvi.txt', 'a+') as f:
                    js = json.dumps(val1)
                    f.seek(0,2)
                    f.write(js)
                    f.write('\n')
                    print("Registered Successfully !!!")

def password_update(user,js):
    with open('D:/Practice/Guvi.txt', 'r') as file:
        a = file.readlines()
        file.seek(0)
        with open('D:/Practice/Guvi.txt', 'w') as file:
            for g in a:
                if user in g:
                    file.write(js)
                    file.write('\n')
                else:
                    file.write(g)

print("Registration and Login system using Python, file handling")
print("Do You Want to Register or Login")
option = input().lower()
if option == 'register':
    user_name = input("Enter The User Name: ")
    passwd = input("Password :")
    writing()
elif option == 'login':
    user_name2 = input("Username :")
    passwd_2 = input("Password :")
    val2={user_name2:passwd_2}
    if usr_nme(user_name2) and password(passwd_2) == True :
        with open('D:/Practice/Guvi.txt', 'r+') as j:
            che = j.readlines()
            j.seek(0)
            number = len(j.readlines())
            js1 = json.dumps(val2)
            count = 0
            for i in che:
                if js1 in i:
                    print("Logged In.")
                elif user_name2 in i and passwd_2 not in i:
                    opt = input("Pasword Wrong You Wish To See The Pasword (YES/NO) :").lower()
                    if opt == 'yes':
                        print(i)
                    elif opt == 'no':
                        sec_opt = input("Do You Wish To Set New Password (YES/NO) :").lower()
                        if sec_opt == 'yes':
                            new_pd = input("New Password")
                            if password(new_pd) == True:
                                js2 = {user_name2:new_pd}
                                js3 = json.dumps(js2)
                                password_update(user_name2,js3)
                                print("Updated Successfully")

                elif user_name2 not in i:
                    count += 1
        if count >= number:
                    print("User Not Registered Please Register and Login")

