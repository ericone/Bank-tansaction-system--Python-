#-*- coding:utf-8 -*-
import pickle
import sys
import time

# test on github
def Operation(h, acc, balance, account):
    print "Please choose the transaction you want <<<<<<<<"
    print "------------------------------------------------------------------------------------"
    print "|                                                                                  |"
    print "|\t1. Bank Transfer \t2. Withdraw Money \t3. Partial Repayment       |"
    print "|\t4. Record Query \t5. Pay Online \t\t6. Exit                    |"
    print "|                                                                                  |"
    print "------------------------------------------------------------------------------------"
    while(True):
        n = raw_input("So your choice is No.? >>>")
        n = int(n)
        if n == 1:
            bank_transfer(h, acc, balance, account)
            break
        elif n == 2:
            withdraw_money(h, acc, balance, account)
            break
        elif n == 3:
            partial_repayment(h, acc, balance, account)
            break
        elif n == 4:
            record_query(h, acc, balance, account)
            break
        elif n == 5:
            pay_online(h, acc, balance, account)
            break
        elif n == 6:
            _exit()
            break
        else:
            n = raw_input("So your choice is No.? >>>")

def bank_transfer(h, acc, balance, account):
    while True:
        print "Please input the account that you want to transfer your money and check it "
        b = raw_input("<<").strip()
        if b != account:
            break
        else:
            print "Excuse me, you can't transfer the money to yourself -_-!"
    account2 = b + '\n'
    while True:
        print "Please input the amount of the money you want to transfer"
        c = raw_input(">>").strip()
        if int(c) < 0:
            print "Please input the number that is more than 0"
        else:
            break
    balance = balance - int(c)
    kind = 'transfer'
    Item = 'deal'
    Object = 'bank'
    info_insert(h, acc, b, kind, c, Item, Object, balance)
    fp_history = open('pk' + str(h.index(account2) + 1) + '.l', 'rb')
    acc_pre_info = pickle.load(fp_history)
    fp_history.close()
    a = len(acc_pre_info)
    balance2 = acc_pre_info[a][6]
    balance2 = balance2 + int(c)
    info_insert(h, account2, account, kind, c, Item, Object, balance2)
    print "Congratulations, the transaction has been completed successfully ! *_*"
    while True:
        if raw_input("If you want to return to the menu , please click the 'Enter' <<") == '':
            break
    _return(h, acc, balance, account)

def withdraw_money(h, acc, balance, account):
    print "The balance of your account is %s $" % balance
    print "Please input the amount of the money you want to withdraw "
    n = raw_input("<<").strip()
    balance = balance - int(n)
    Kind = 'withdraw'
    Money = n
    Item = 'deal'
    Object = 'bank'
    Balance = balance
    Account = account
    info_insert(h, acc, Account, Kind, Money, Item, Object, Balance)
    print "Please take your money right away ! *_*"
    while True:
        if raw_input("If you want to return to the menu , please click the 'Enter' <<") == '':
            break
    _return(h, acc, balance, account)


def partial_repayment(h, acc, balance, account):
    print "The balance of your account is %s $" %balance
    print "Please input the amount of the money you want to return "
    while True:
        n = raw_input("<<").strip()
        if n != '' and int(n) > 0:
            break
        else:
            print "Sorry , the number you input should more than 0 -_-! "
    balance = balance + int(n)
    Kind = 'repayment'
    Money = n
    Item = 'debt'
    Object = 'bank'
    Balance = balance
    Account = account
    info_insert(h, acc, Account, Kind, Money, Item, Object, Balance)
    print "Congratulations, you have return the money in time ! \n You are an honest man! ^_^ "
    while True:
        if raw_input("If you want to return to the menu , please click the 'Enter' <<") == '':
            break
    _return(h, acc, balance, account)


def record_query(h, acc, balance, account):
    fp_history = open('pk' + str(h.index(acc) + 1) + '.l', 'rb')
    acc_pre_info = pickle.load(fp_history)
    fp_history.close()
    i = len(acc_pre_info)
    print "History Record: \n"
    print "Time\t" + "\t\tAccount\t" + "\tKind\t" + "\tSum\t" + "\tItem\t" + "\tObject\t" + "\tBalance($)"
    print '\n'
    for i in range(1, i+1):
        print acc_pre_info[i][0] + "\t\t" + acc_pre_info[i][1] + "\t\t" + acc_pre_info[i][2] + "\t" + acc_pre_info[i][3] + "\t\t" +acc_pre_info[i][4] +  "\t\t" +acc_pre_info[i][5] + "\t\t" + str(acc_pre_info[i][6])
    print '\n'
    while True:
        if raw_input("If you want to return to the menu , please click the 'Enter' <<") == '':
            break
    _return(h, acc, balance, account)

def _exit():
    print "You have logged out successfully !"
    sys.exit()

def _return(h, acc, balance, account):
    Operation(h, acc, balance, account)

def log_in(h, j, account1, password1, account):
    t = False
    i = 0
    for acc in h:
        i += 1
        if i >= 3:
            break
        if acc == account1:
            if password1 == j[h.index(acc)]:   #h.index(acc) the index of the account
                print "\n Welcome, Mr%r " % account + "\t\tTime:" + time.strftime("%Y-%M-%d %H:%M:%S ", time.localtime())
                print "\n \tMr %r, Is the condition safe ? And do you want to continue the process?" % account
                print "Press RETURN to continue or CTRL-C to exit."
                raw_input('?')
                t = True
                break
            else:
                print "There are 3 opportunities for you. %s more left!" % (3 - i)
                acc2 = raw_input("Please input your account numbers:>").strip()
                account1 = acc2 + '\n'
                pas2 = raw_input("Please input your password:>").strip()
                password1 = pas2 + '\n'
                continue
        else:
            print "There are 3 opportunities for you. %s more left!" % (3 - i)
            acc2 = raw_input("Please input your account numbers:>").strip()
            account1 = acc2 + '\n'
            pas2 = raw_input("Please input your password:>").strip()
            password1 = pas2 + '\n'
            continue
    if not t:
        print "\nI'm Sorry to informed you that your account have been locked !\n"
        sys.exit()

def pay_online(h, acc, balance, account):
    Goods_info = {'1': ['100', 'iPhone', 'JinDong'],
                  '2': ['100', 'Kindle', 'Amazon'],
                  '3': ['200', 'clothes', 'TianMao'],
                  '4': ['300', 'iMac', 'JinDong'],
                  '5': ['200', 'iPod', 'Apple'],
                  '6': ['150', 'Gel', 'Assics']
                  }
    print "-----------------------------------------------------------------"
    print "|\tNo\t|\tItem\t|\tPrice\t|\tMarket\t|"
    print "|               |               |               |               |"
    print "-----------------------------------------------------------------"
    for a in range(1, 7):
        i = str(a)
        # print "---------------------------------------------------------------"
        print "|\tNo.%s\t|\t%s$\t|\t%s\t|\t%s\t|" % (i, Goods_info[i][0], Goods_info[i][1], Goods_info[i][2])
        print "-----------------------------------------------------------------"
    n = raw_input("Please Input the number of good that you want to buy <<")
    while True:
        if n != '' and int(n) > 0 and int(n) < 6:
           break
        else:
            print "The number should be more than 0 and less than 7"
            n = raw_input("Please Input the number of good that you want to buy <<")
    balance = balance - int(Goods_info[str(n)][0])
    print "You have bought %s successfully !" % Goods_info[str(n)][1]
    print "And you have paid %s$ for it" % Goods_info[str(n)][0]
    print "balance = %s $" % balance
    if balance < 0:
        print "Please make sure you can make  ends meet when you decide to buy sth !"
    kind = 'pay_online'
    info_insert(h, acc, account, kind, Goods_info[str(n)][0], Goods_info[str(n)][1], Goods_info[str(n)][2], balance)
    while True:
        if raw_input("If you want to return to the menu , please click the 'Enter' <<") == '':
            break
    _return(h, acc, balance, account)
    '''
    f_history = file('pk' + str(h.index(acc) + 1) + '.l', 'wb')
    pickle.dump(acc_info, f_history)
    # acc_info = {'date':['money', 'item', 'place']}
    f_history.close()
    '''

def info_insert(h, acc, Account, Kind, Money, Item, Object, Balance):
    fp_pre_his = open('pk' + str(h.index(acc) + 1) + '.l', 'rb')
    aaa = pickle.load(fp_pre_his)
    fp_pre_his.close()
    i = len(aaa)
    i = i + 1
    Time = str(time.localtime()[0]) + '/' + str(time.localtime()[1]) + '/' + str(time.localtime()[2]) + '/' + str(time.localtime()[3]) + ':' + str(time.localtime()[4])
    aaa[i] = [Time, Account, Kind, Money, Item, Object, Balance]
    fp_his = file('pk' + str(h.index(acc) + 1) + '.l', 'wb')
    pickle.dump(aaa, fp_his)
    fp_his.close()

def main():
    f = open("account.txt", 'r')
    g = open("password.txt", 'r')
    h = f.readlines()
    j = g.readlines()
    f.close()
    g.close()
    account = raw_input("Please input your account numbers:>").strip()
    account1 = account + '\n'
    password = raw_input("Please input your password:>").strip()
    password1 = password + '\n'
    log_in(h, j, account1, password1, account)
    fp_history = open('pk' + str(h.index(account1) + 1) + '.l', 'rb')
    acc_pre_info = pickle.load(fp_history)
    fp_history.close()
    a = len(acc_pre_info)
    balance = acc_pre_info[a][6]
    Operation(h, account1, balance, account)

main()
