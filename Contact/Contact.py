import os
#한글저장 및 읽기 TRY EXCEPT절 변수 즉 TRY절 안에 선언한거 FINALLY절에서 사용하기
class Contact:
    def __init__(self,name,addr,tel):
        self.name=name
        self.addr=addr
        self.tel =tel
    def print_info(self):
        print('name:%s,addr:%s,tel:%s' % (self.name,self.addr,self.tel))

def set_contact():
    name =input('이름을 입력?')
    addr =input('주소를 입력?')
    tel  =input('전번을 입력?')
    contact = Contact(name,addr,tel)
    print('name:%s,addr:%s,tel:%s' % (name, addr, tel))
    return contact


def print_menu():
    print('1.주소입력 2.주소출력 3.주소 삭제 4.종료')
    menu = input('메뉴번호 입력?')
    return int(menu)

def print_contact(contacts):
    #print(contacts,len(contacts))
    for contact in contacts:
        contact.print_info()

def del_contact(contacts,name):
    for index,contact in enumerate(contacts):
        if name == contact.name:
            del contacts[index]
            print(name+'이 삭제됨')
    print(name+'가(이) 없습니다')

def save(contacts):
    f= open('./content/contacts.txt','w',encoding='utf8')
    for contact in contacts:
        f.write(contact.name+'\n')
        f.write(contact.addr + '\n')
        f.write(contact.tel + '\n')
    print('%d명이 저장되었습니다' % len(contacts))
    f.close()

def load(contacts):
    f=None
    try:
        if os.path.exists('./content/contacts.txt'):
            f = open('./content/contacts.txt', 'r',encoding='utf8')
            list=f.readlines()
            num=int(len(list)/3)
            for i in range(num):
                name = list[3*i].rstrip('\n')
                addr = list[3 * i+1].rstrip('\n')
                tel = list[3 * i+2].rstrip('\n')
                contacts.append(Contact(name,addr,tel))
            #f.close()
    except FileNotFoundError as e:
        print(str(e)+':파일이 없어요')
    finally:
        print('finally절')
        if f is not None:
           # pass
        #else:
            f.close()

def run():
    contacts =[]
    load(contacts)
    while True:
        menu = print_menu()
        if menu== 4:
            save(contacts)
            break
        elif menu==1:
            contacts.append(set_contact())
        elif menu==2:
            print_contact(contacts)
        else:
            name=input('삭제할 이름?')
            del_contact(contacts, name)

if __name__ =='__main__':
    run()
#print(print_menu()+100)

#set_contact()
#def test_run():
#contact=Contact('홍길동1','강남1','010')
#contact.print_info()
#if __name__ =='__main__':
#    test_run()
