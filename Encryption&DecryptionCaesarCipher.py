dicitonary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def UserInterface():
    File1 = open('EncryptedFile.txt', 'r')
    File2 = open('DecryptedFile.txt','w')
    Container = File1.readlines()
    message = ''.join(Container)
    message = message.replace(" "," ")
    message=message.upper()
    UserInput = input("Welcome To Hashmat Ali Shah Tool \n For Encypted Press e \n For Decrypted press d")
    if UserInput == 'e':
        print('Enter the Key Value: ')
        Key = int(input())
        File1.write(Encrypted(message,Key) + '\n')
    else:
        if UserInput == 'd':
            print('Enter the Key Value: ')
            Key = int(input())
            File2.write(Decrypted(message,Key) + '\n')
        else:
            print(UserInput.replace('Please ReEnter Process Again: - '))


def Encrypted(message,Key):
    encrypt_message = ""
    for i in message:
        location = Key + dicitonary.index(i)
        location%=26
        encrypt_message+= dicitonary[location]
    print('Encryption is Completed \n Please Check Encrypted File')
    return encrypt_message

def Decrypted(message,Key):
    decrypt_message = ""
    for i in message:
        location = Key + dicitonary.index(i) -Key
        location%=26
        decrypt_message+= dicitonary[location]
    print('Encryption is Completed \n Please Check Encrypted File')
    return decrypt_message

UserInterface()
