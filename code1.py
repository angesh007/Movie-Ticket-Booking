from flask import Flask,render_template,redirect,request
import psycopg2
import calendar;
import time;
hostname='localhost'
db='cia3'
port='5432'
uname='postgres'
con = psycopg2.connect(
        host=hostname,
        database=db,
        user=uname,
        password=pwd,
        port=&#39;5432&#39;)
cursor = con.cursor()
app = Flask(__name__)
a=False
isloggedin = a
@app.route(&quot;/Login&quot;,methods =[&quot;GET&quot;])
def loginindex():
    global isloggedin
    isloggedin = False
    return render_template(&quot;login.html&quot;)
@app.route(&#39;/Checkout&#39;, methods =[&quot;GET&quot;,&#39;POST&#39;])
def che():
    return render_template(&quot;checkout.html&quot;)
           
       
@app.route(&#39;/Register&#39;, methods =[&quot;POST&quot;])
def reg():
    global isloggedin
    if isloggedin: return redirect(&quot;/&quot;)
    isloggedin = False
    if request.form.get(&quot;rusername&quot;) and request.form.get(&quot;rpassword&quot;):
        username = request.form.get(&quot;rusername&quot;)
        password = request.form.get(&quot;rpassword&quot;)
        mobno = request.form.get(&quot;rmno&quot;)
        email = request.form.get(&quot;remail&quot;)
        address = request.form.get(&quot;raddress&quot;)
        area = request.form.get(&quot;rarea&quot;)
gmt = time.gmtime()
        ts = calendar.timegm(gmt)
        cursor.execute(&quot;INSERT INTO login (login_id,login_password) values(%s,
%s)&quot;,(username, password))
        cursor.execute(&quot;INSERT INTO customer
(cust_name,cust_mobile,cust_email,cust_address,area) values(%s, %s, %s, %s,
%s)&quot;,(username, mobno,email, address, area))
        con.commit()
        isloggedin=True
        return redirect(&quot;/&quot;)
    else:
        return redirect(&quot;/Login?msg=2&quot;)
@app.route(&#39;/Login&#39;, methods =[&quot;POST&quot;])
def log():
    global isloggedin
    if isloggedin: return redirect(&quot;/&quot;)
    isloggedin = False
    if request.form.get(&quot;lusername&quot;) and request.form.get(&quot;lpassword&quot;):
        user = request.form.get(&quot;lusername&quot;)
        password = request.form.get(&quot;lpassword&quot;)
        cursor.execute(&quot;select login_id,login_password from login where
login_id=&#39;&quot;+user+&quot;&#39; and login_password=&#39;&quot;+password+&quot;&#39;&quot;)
        # print(cursor[0])
        for row in cursor:
            if row[0]:
                isloggedin=True
                print(&quot;hello&quot;)
                return redirect(&quot;/&quot;)
        return redirect(&quot;/Login?msg=1&quot;)
# isloggedin = log()
 
   
@app.route(&quot;/Orderplaced&quot;, methods =[&quot;GET&quot;,&#39;POST&#39;])
def ord():
    numticket = request.form.get(&quot;cnum&quot;)
    amount = request.form.get(&quot;camount&quot;)
    tdate = request.form.get(&quot;cdate&quot;)
    ttime = request.form.get(&quot;ctime&quot;)
    cursor.execute(&quot;INSERT INTO ticketbooking
(num_of_tickets,amount,book_date,book_time) values(%s, %s, %s,
%s)&quot;,(numticket, amount, tdate, ttime))
    con.commit()
    print(numticket,amount,tdate,ttime)
    return render_template(&quot;orderplaced.html&quot;)
@app.route(&#39;/&#39;)
def index():
print(isloggedin)
    if(isloggedin):
        return render_template(&quot;index.html&quot;)
    else:
        return redirect(&quot;/Login&quot;, code=302)
       
if __name__ == &#39;__main__&#39;:
    app.run(debug=True)