# PROJECT OVERVIEW
As a team of junior data engineers, we want to get data from Twitter API by using a crawler program, so we can store the data in a database and analyze from it to get insights.


# THIS PROJECT IS DEVELOPED BY
GROUP 2
Teamate 1: Karen
Teamate 2: Circle
Teamate 3: Jiu


# OBJECTIVE
1. get information of a user from twitter API
2. design a database and store the information
3. anylyze from the database:
	a. Which month the user posted most frequently?
	b. *Which keywords were the most common used?


# TIME PHASE 1
Design the program to:

    1. get profile information of user //user = api.get_user('user_name')
        a. name
        b. description/ bio
        c. following_count
        d. followers_count
        e. location
        f. joined date
        g. id

    2. get social network of user //user.friends()
        a. following acconts (name, id)
    
    3. get tweets from a user //
        a. from 01/01/2020 until now
        b. keywords in (covid, coronavirus, covid19, pandemic, virus, corona, vaccine, vaccination, Pfizer-BioNTech, BioNTech, Moderna, Johnson & Johnson, Pfizer, mrk, jnj)


# TIME PHASE 2
Design database
Clean the information and store in the database
Analyze from the database

# TIME PHASE 3 
Test