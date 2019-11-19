from datetime import date
first_name = input("What's your first name?")
last_name = input("What's your last name?")
birth_year = int(input("In what year were you born?"))
today = date.today()
age = int(today.strftime("%Y")) - birth_year
last_job = input("What was your last job?")
email = input("What's your email?")

hmtl_CV = f'''
<!DOCTYPE html>
<html>
<head>
    <title>CV</title>
</head>
<body>
    <h1>CV</h1>
    <ul>
        <li>Name: {first_name} {last_name}</li>
        <li>Age: {age}</li>
        <li>Last job: {last_job}</li>
        <li>E-mail: {email}</li>
    </ul>
</body>
</html>
'''

print(hmtl_CV)