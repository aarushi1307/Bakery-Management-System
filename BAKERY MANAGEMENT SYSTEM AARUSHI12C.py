import pymysql
db=pymysql.Connect(host='localhost',user='root',password='tiger')
cur=db.cursor()
from prettytable import PrettyTable

def emp_add():
    g=cur.execute("select * from employee;")
    x=cur.fetchall()
    l=cur.rowcount
    if l>0:
        while True:
        
         E_CODE=input("ECODE")
         NAME=input("NAME")
         POSITION=input("POSITION")
         SALARY=input("SALARY")
         JOINING_DATE=input("JOINING_DATE")
         q="insert into employee values('{}','{}','{}','{}','{}')".format(E_CODE,NAME, POSITION,SALARY,JOINING_DATE )
         cur.execute(q)
         db.commit()
         print("record added")

         ch=input('do you want to continue y/n')
         if ch.lower()=='n':
             break
             
def emp_edit():
    x=input("E_CODE to edit")
    q="select * from employee where E_CODE='%s'"%(x)
    cur.execute(q)
    u=cur.rowcount
    if u<1:
        print("record not found")
    else:
        print("old Values\n",cur.fetchall())
        NAME=input("NAME")
        POSITION=input("POSITION")
        SALARY=input("SALARY")
        JOINING_DATE=input("JOINING_DATE")
        q1="update employee set NAME='%s' where E_CODE='%s'"%(NAME,x)
        q2="update employee set POSITION='%s' where E_CODE='%s'"%(POSITION,x)
        q3="update employee set SALARY='%s' where E_CODE='%s'"%(SALARY,x)
        q4="update employee set JOINING_DATE='%s' where E_CODE='%s'"%(JOINING_DATE,x)
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
        db.commit()
        print("record edited")

def emp_search():
    x=input("Employee Name to Search")
    q="select * from employee where NAME='%s'"%(x)
    cur.execute(q)
    x1=cur.fetchall()

    r=cur.rowcount
    if r<1:
        print("record not found")
    else:
        print(x1)
    
def emp_delete():
    x=  input("E_CODE to delete")
    q="select * from employee where E_CODE='%s'"%(x)
    cur.execute(q)
    x1=cur.fetchall()

    r=cur.rowcount
    if r<1:
        print("record not found")
    else:
        q="delete from employee where E_CODE='%s'"%(x)
    cur.execute(q)
    db.commit()
    print("record deleted")
def emp_display():
    b=cur.execute('select *from employee')
    s=cur.fetchall()
    print('E_CODE',':','NAME',':','\t','POSITION',':','\t','SALARY',':', 'JOINING_DATE',':' )
    for b in s:
        print("{}\t {}\t{}\t{}\t\t{}".format (b[0],b[1],b[2],b[3],b[4]))
    print('-------------------------------------------------------------------------------------------------------------------------')
print('                         WELCOME TO OUR BAKERY!')
print('         🎧 ✩｡☕ 🤎 ₊˚.🍪˖⁺‧₊˚ ☕︎˚₊‧⁺˖ 🍪 ₊˚.🎧 ✩｡☕ 🤎')
cur.execute('use bakery')
e=cur.execute('select *from employee')
xy=int(input('''enter 1 : if you are ADMIN
enter 2: if you are CUSTOMER'''))
if xy==1:
    print('-ˋˏ ༻✿༺ ˎˊ-')
    pw=input('enter password')
    print(pw)
    if pw==('BAKERY'):
        while True:
            cur.execute('use bakery')
            cur=db.cursor()
            b=cur.execute('select *from employee')
            s=cur.fetchall()
             
            v = PrettyTable(['E_CODE','NAME','POSITION','SALARY', 'JOINING_DATE'])
            for b in s:
                v.add_row(b)
            print(v)
            #print("{}\t {}\t{}\t{}\t{}".format (b[0],b[1],b[2],b[3],b[4]))
            print("1. Add Record\n 2. Edit Record\n 3. Search Record\n 4. Delete Record\n 5. Display\n 6. END\n")
            o=int(input("Choice"))
            if o==1:
                emp_add()
            if o==2:
                emp_edit()
            if o==3:
                emp_search()
            if o==4:
                emp_delete()
            if o==5:
                emp_display()
            if o==6:
                break


if xy==2:
    print('select below options from the menu')
    a=int(input('''WHICH MENU DO YOU WANT TO VIEW:
                1. Bakery
                2. Café: '''))
    
    if a==1:
            cur.execute('use bakery')
            cur=db.cursor()
            row=cur.execute('select *from item')
            res=cur.fetchall()
            t = PrettyTable(['sno', 'itemname','price', 'each_qty'])
            for i in res:
                t.add_row(i)
            print(t)
            cur.execute('use bakery')
            cur=db.cursor()
            r1=cur.execute('select *from flavours')
            re=cur.fetchall()
            t = PrettyTable(['sno', 'flavours'])
            for i in re:
                t.add_row(i)
            print(t)
            print('WHAT DO YOU WANT TO ORDER?')
            cur.execute('use bakery')
            row=cur.execute('select *from item')
            res=cur.fetchall()
            d=int(input('ENTER SERIAL NO. OF THE ITEM YOU WANT TO ORDER----> FROM THE MENU:'))
            if d==1:
                        cur.execute('use bakery')
                        '''cur=db.cursor()
                        r=cur.execute('select *from flavours')
                        a=cur.fetchall()

                    #print('rows fetched', a,r)
                        print('sno',':','\t', 'flavours',':')
                        for r in a:
                            print("{}\t{}\t".format (r[0],r[1]))
                        print('-------------------------------------------------------------------------------------------------------------------------')'''
                        print('WHICH CAKE DO YOU WANT TO BUY?')
                        print('<------ PRICE VARIES ACCORDING TO QTY----->')
                        c=int(input('ENTER YOUR CHOICE:'))
                        if c==1:
                                print('HOW MUCH QTY OF VANILLA CAKE DO YOU WANT?')
                                qty=int(input('ENTER QTY:'))
                                print('\n')
                                print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                                print('  ')
                                
                                q=cur.execute('select price from item')
                                q=cur.fetchall()
                                q=q[0][0]
                                c=int(q)
                                print('PRICE OF 1 CAKE:',q)
                                print('TOTAL QTY OF CAKE:', qty)
                                              
                                print('TOTAL AMOUNT',qty*q)
                                print('\n')
                        if c==2: 
                                print('HOW MUCH QTY OF STRAWBERRY CAKE DO YOU WANT?')
                                qty=int(input('ENTER QTY:'))
                                print('\n')
                                print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                                print('  ')
                                                        

                                q=cur.execute('select price from item')
                                q=cur.fetchall()
                                q=q[0][0]
                                c=int(q)
                                print('PRICE OF 1 CAKE:',q)
                                print('TOTAL QTY OF CAKE:', qty)
                                print('TOTAL AMOUNT',qty*q)
                                print('\n')
                        if c==3:
                                print('HOW MUCH QTY OF CHOCOLATE CAKE DO YOU WANT?')
                                qty=int(input('ENTER QTY:'))
                                print('\n')
                                print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                                print('  ')
                                
                                                    
                                q=cur.execute('select price from item')
                                q=cur.fetchall()
                                q=q[0][0]
                                c=int(q)
                                print('PRICE OF 1 CAKE:',q)
                                print('TOTAL QTY OF CAKE:', qty)
                                print('TOTAL AMOUNT',qty*q)
                        if c==4:
                                print('HOW MUCH QTY OF BUTTERSCOTCH CAKE DO YOU WANT?')
                                qty=int(input('ENTER QTY:'))
                                print('\n')
                                print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                                print('  ')
                                                        
                                q=cur.execute('select price from item')
                                q=cur.fetchall()
                                q=q[0][0]
                                c=int(q)
                                print('PRICE OF 1 CAKE:',q)
                                print('TOTAL QTY OF CAKE:', qty)
                                print('TOTAL AMOUNT',qty*q)
                                print('\n')
            if d==2:
                cur.execute('use bakery')
                '''cur=db.cursor()
                r=cur.execute('select *from flavours')
                a=cur.fetchall()

            #print('rows fetched', a,r)
                print('sno',':','\t', 'flavours',':')
                for ra in a:
                    print("{}\t{}\t".format (ra[0],ra[1]))
                print('-------------------------------------------------------------------------------------------------------------------------')'''
                print('WHICH DONUT DO YOU WANT TO BUY?')
                print('<------ PRICE VARIES ACCORDING TO QTY----->')
                c=int(input('ENTER YOUR CHOICE:'))
                if c==1:
                        print('HOW MUCH QTY OF VANILLA DONUT DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "donuts" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 DONUT:',q)
                        print('TOTAL QTY OF DONUT:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==2: 
                        print('HOW MUCH QTY OF STRAWBERRY DONUT DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "donuts" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 DONUT:',q)
                        print('TOTAL QTY OF DONUT:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==3:
                        print('HOW MUCH QTY OF CHOCOLATE DONUT DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "donuts" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 DONUT:',q)
                        print('TOTAL QTY OF DONUT:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==4:
                        print('HOW MUCH QTY OF BUTTERSCOTCH DONUT DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "donuts" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 DONUT:',q)
                        print('TOTAL QTY OF DONUT:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')

            if d==4:
                cur.execute('use bakery')
                
                print('WHICH COOKIE DO YOU WANT TO BUY?')
                print('<------ PRICE VARIES ACCORDING TO QTY----->')
                c=int(input('ENTER YOUR CHOICE:'))
                if c==1:
                        print('HOW MUCH QTY OF VANILLA COOKIE DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "COOKIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 COOKIE:',q)
                        print('TOTAL QTY OF COOKIE:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==2: 
                        print('HOW MUCH QTY OF STRAWBERRY COOKIE DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "COOKIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 COOKIE:',q)
                        print('TOTAL QTY OF COOKIE:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==3:
                        print('HOW MUCH QTY OF CHOCOLATE COOKIE DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "COOKIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 COOKIE:',q)
                        print('TOTAL QTY OF COOKIE:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==4:
                        print('HOW MUCH QTY OF BUTTERSCOTCH COOKIE DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "COOKIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 COOKIE:',q)
                        print('TOTAL QTY OF COOKIE:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')

            if d==3:
                cur.execute('use bakery')
                
                print('WHICH MILKSHAKE  DO YOU WANT TO BUY?')
                print('<------ PRICE VARIES ACCORDING TO QTY----->')
                c=int(input('ENTER YOUR CHOICE:'))
                if c==1:
                        print('HOW MUCH QTY OF VANILLA MILKSHAKE  DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "MILKSHAKE" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 MILKSHAKE :',q)
                        print('TOTAL QTY OF :', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==2: 
                        print('HOW MUCH QTY OF STRAWBERRY MILKSHAKE DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "MILKSHAKE" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 MILKSHAKE:',q)
                        print('TOTAL QTY OF MILKSHAKE:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==3:
                        print('HOW MUCH QTY OF CHOCOLATE MILKSHAKE DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "MILKSHAKE" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 MILKSHAKE:',q)
                        print('TOTAL QTY OF MILKSHAKE:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==4:
                        print('HOW MUCH QTY OF BUTTERSCOTCH MILKSHAKE DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "MILKSHAKE" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 MILKSHAKE:',q)
                        print('TOTAL QTY OF MILKSHAKE:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')

            if d==5:
                cur.execute('use bakery')
                
                print('WHICH PASTRY  DO YOU WANT TO BUY?')
                print('<------ PRICE VARIES ACCORDING TO QTY----->')
                c=int(input('ENTER YOUR CHOICE:'))
                if c==1:
                        print('HOW MUCH QTY OF VANILLA PASTRY DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "PASTRIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 PASTRY:',q)
                        print('TOTAL QTY OF PASTRY:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==2: 
                        print('HOW MUCH QTY OF STRAWBERRY PASTRY DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "PASTRIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 PASTRY:',q)
                        print('TOTAL QTY OF PASTRY:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==3:
                        print('HOW MUCH QTY OF CHOCOLATE PASTRY DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "PASTRIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 PASTRY:',q)
                        print('TOTAL QTY OF PASTRY:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')
                if c==4:
                        print('HOW MUCH QTY OF BUTTERSCOTCH PASTRY DO YOU WANT?')
                        qty=int(input('ENTER QTY:'))
                        print('\n')
                        print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
                        print('  ')
                        
                        q=cur.execute('select price from item  where itemname= "PASTRIES" ')
                        q=cur.fetchall()
                        q=q[0][0]
                        c=int(q)
                        print('PRICE OF 1 PASTRY:',q)
                        print('TOTAL QTY OF PASTRY:', qty)
                                      
                        print('TOTAL AMOUNT',qty*q)
                        print('\n')


                        
                

                
                        
            print('-------------------------VISIT AGAIN-----------------------------')

            print('''Mahalo. Gracias. Merci. Grazie. Obrigado. Dhanyavaad. Xiéxié.\n
           <<---In other words, thank you seven times over for your purchase!--->>''')
            print('｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ')

            

            








    if a==2:
        cur.execute('use bakery')
        cur=db.cursor()
        r2=cur.execute('select *from cafe')
        o=cur.fetchall()
        b = PrettyTable(['sno', 'itemname','price', 'each_qty'])
        for i in o:
            b.add_row(i)
        print(b)
        o=int(input('ENTER SERIAL NO. OF THE ITEM YOU WANT TO ORDER?'))
        if o==1:
            print('HOW MUCH QTY OF Eye-opener Espresso DO YOU WANT?')
            qty=int(input('ENTER QTY:'))
            print('\n')
            print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
            print('  ')
                        
            q=cur.execute('select price from cafe  where itemname= "Eye-opener Espresso" ')
            q=cur.fetchall()
            q=q[0][0]
            c=int(q)
            print('PRICE OF 1 Eye-opener Espresso:',q)
            print('TOTAL QTY OF Eye-opener Espresso:', qty)
                                      
            print('TOTAL AMOUNT',qty*q)
            print('\n')
            print('\n')
            print('-------------------------VISIT AGAIN-----------------------------')

        if o==2:
            print('HOW MUCH QTY OF Café Mocha DO YOU WANT?')
            qty=int(input('ENTER QTY:'))
            print('\n')
            print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
            print('  ')
                        
            q=cur.execute('select price from cafe  where itemname= "Café Mocha" ')
            q=cur.fetchall()
            q=q[0][0]
            c=int(q)
            print('PRICE OF 1 Café Mocha:',q)
            print('TOTAL QTY OF Café Mocha :', qty)
                                      
            print('TOTAL AMOUNT',qty*q)
            print('\n')
            print('\n')
            print('-------------------------VISIT AGAIN-----------------------------')

        if o==3:
            print('HOW MUCH QTY OF Cappuccino DO YOU WANT?')
            qty=int(input('ENTER QTY:'))
            print('\n')
            print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
            print('  ')
                        
            q=cur.execute('select price from cafe  where itemname= "Cappuccino" ')
            q=cur.fetchall()
            q=q[0][0]
            c=int(q)
            print('PRICE OF 1 Cappuccino:',q)
            print('TOTAL QTY OF Cappuccino :', qty)
                                      
            print('TOTAL AMOUNT',qty*q)
            print('\n')
            print('\n')
            print('-------------------------VISIT AGAIN-----------------------------')

        if o==4:
            print('HOW MUCH QTY OF Café Latte DO YOU WANT?')
            qty=int(input('ENTER QTY:'))
            print('\n')
            print(':;;;;;:*★:;;;;;:★:;;;;;:★ORDER PLACED!!:;;;;;:★:;;;;;:★:;;;;;:★:;;;;')
            print('  ')
                        
            q=cur.execute('select price from cafe  where itemname= "Café Latte" ')
            q=cur.fetchall()
            q=q[0][0]
            c=int(q)
            print('PRICE OF 1 Café Latte:',q)
            print('TOTAL QTY OF Café Latte :', qty)
                                      
            print('TOTAL AMOUNT',qty*q)
            print('\n')
            print('\n')
            print('-------------------------VISIT AGAIN-----------------------------')
        print('''Mahalo. Gracias. Merci. Grazie. Obrigado. Dhanyavaad. Xiéxié.
<<--------In other words, thank you seven times over for your purchase!-------->>''')
        print('｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡')
