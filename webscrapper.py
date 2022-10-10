from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def branch(n):

    if n == 1:
        return 'http://mjcollege.ac.in/dept/civildept/stafflist.php','CIVIL DEPT'
    elif n ==2:
        return 'http://mjcollege.ac.in/dept/csedept/stafflist.php','CSE DEPT'
    elif n == 3:
        return 'http://mjcollege.ac.in/dept/mechdept/stafflist.php','MECH DEPT'
    elif n == 4:
        return 'http://mjcollege.ac.in/dept/ecedept/stafflist.php','ECE DEPT'
    elif n == 5:
        return 'http://mjcollege.ac.in/dept/ee/stafflist.php','EE DEPT'
    elif n == 6:
        return 'http://mjcollege.ac.in/it/stafflist.php','IT DEPT'
    else :
        return False


m = int(input( "\n 1.CIVIL  \n 2.CSE \n 3.MECH \n 4.ECE \n 5.EE \n 6.IT \n"
             "PLEASE SELECT YOUR DEPARTMENT : "))
#dept = branch(m)
my_url , dept = branch(m)
print("FETCHING DATA PLEASE WAIT ...")
print(dept.upper())
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html , "html.parser")

containers1 = page_soup.findAll("tr", {"class" : "even"})
containers2 = page_soup.findAll("tr", {"class" : "odd"})
#print(len(containers1)
container1 = containers1[0]
container2 = containers2[0]

person_name1 = container1.findAll("span", {"class" : "portletHeader"})
person_name2 = container2.findAll("span", {"class" : "portletHeader"})
#print(person_name[0].text)
email1 = container1.findAll("div",{"class" : "emailAddress"})
email2 = container2.findAll("div",{"class" : "emailAddress"})
#print(email[0].text)
phone_no1 = container1.findAll("div",{"class" : "hasPhoneNumber"})
phone_no2 = container2.findAll("div",{"class" : "hasPhoneNumber"})
#print(phone_no[0].text)

filename = dept + " details.csv"
f = open(filename, "w")

headers = "Faculty_Name,Phone_no,Email \n"
f.write(headers)

for container1 in containers1:
    p_name1 = container1.findAll("span", {"class" : "portletHeader"})
    person_name1 = p_name1[0].text

    p_mail1 = container1.findAll("div",{"class" : "emailAddress"})
    email1 = p_mail1[0].text

    p_mobile1 = container1.findAll("div",{"class" : "hasPhoneNumber"})
    phone_no1 = p_mobile1[0].text

    print("Faculty name : " + person_name1 + ",\t Phone Number : " + phone_no1 + ",\tEmail : " + email1 + "\n")
    f.write(person_name1 + "," + phone_no1 + ", " + email1+ "\n")

for container2 in containers2:
    p_name2 = container2.findAll("span", {"class": "portletHeader"})
    person_name2 = p_name2[0].text

    p_mail2 = container2.findAll("div", {"class": "emailAddress"})
    email2 = p_mail2[0].text

    p_mobile2 = container2.findAll("div", {"class": "hasPhoneNumber"})
    phone_no2 = p_mobile2[0].text

    print("Faculty name : " + person_name2 + ",""\t Phone Number : " + phone_no2 + ",""\tEmail : " + email2+ "\n")
    f.write(person_name2 + "," + phone_no2 + ", " + email2 + "\n")
f.close()
