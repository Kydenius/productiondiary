## Production Diary
Online Production Diary Management System in Flask using mySQL

## Getting Started

## Clone this repository and set your path to a folder, to get it up and running on your local system.✨

```
git clone https://github.com/kydenius/productiondiary.git
cd productiondiary
```

### Prerequisites

To run this system you will need:

-  Python ( https://www.python.org/ )
-  Flask ( a library used, downloads automatically via requirements.txt command )
-  SQLALCHEMY ( a library used, downloads automatically via requirements.txt command)
-  PHPMyAdmin (like XAMPP: https://www.apachefriends.org/ )


Assuming you have Python and a backend like XAMPP (to run Apache and a MySQL server), proceed to install the rest of the requirements using the command below:

```
pip3 install -r requirements.txt

```

##write on the terminal:

```

python 

(## opens up python interpreter )

from App import db

(## create db tables from the code )

db.create_all()

(## self explanitory )

quit()

(## quits python interpreter on the terminal instance)

````

````

If you have XAMPP (Apache and MySQL) running, Run the program on a development server with the following command (Werkzeug):

````
python app.py run

````


### The Main Page

The program's main page is singular, the ID's assigned, are unique to all the events that are added to the database. Notice that the missing ID lines are going to be missing upon deletion in the database (IE. Database: 1-5, and you delete number #3).

[![unknown-7.png](https://i.postimg.cc/W380TCNM/unknown-7.png)](https://postimg.cc/wyt1kWsv)


###  Adding a incident

A new incident/event can be added by entering the date, name, and the required information needed, like the free comment section. A new ID is assigned to each added line of events.

[![unknown-9.png](https://i.postimg.cc/7YGJWf21/unknown-9.png)](https://postimg.cc/VdwNSs45)

###  Updating an event information

The current information of a already added incident/event can be updated quickly, just use the Edit function on the page to reorganize the event information.

[![unknown-8.png](https://i.postimg.cc/cL3Yrr11/unknown-8.png)](https://postimg.cc/FY916FJw)

###  MySQL database using the XAMPP server

XAMPP is bundle package to install MySQL and PHPMyAdmin. PHPMyAdmin is the GUI to handle and perform all the operations of the MySQL Database.


# Built using
- Flask
- SQLAlchemy
- Bootstrap
- XAMPP Server

# 📃License

This project is licensed under the MIT License - see the License file for the details. The creator will not be held liable of any issues legal or not with the product, you are free to distribute and edit the product as wanted, even commercially, as long as the attached MIT licence is included in the product.

