# intruder-for-sql
First of all it is for portswinger security academy for blind sql injection
at the url need to be placed target then i suddenly revealed how many characters is in admins password via "'AND (SELECT users FROM user WHERE username='administrator' AND LENGTH(password)>1) = 'a"
