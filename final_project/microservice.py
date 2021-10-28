# import docker
# client = docker.from_env()

def open_apache_hadoop():
	# client.containers.run("ubuntu:latest", "echo hello world")
	print("open apache hadoop")

def open_apache_spark():
	print("open apache spark")

def open_jupyter_notebook():
	print("open jupyter notebook")

def open_sonar():
	print("open sonar")



print("Welcome to Big Data Processing Application")
print("Please type the number that corresponds to which application you would like to run:")
print("1. Apache Hadoop")
print("2. Apache Spark")
print("3. Jupyter Notebook")
print("4. SonarQube and SonarScanner")

choice = input("Type the number here > ")
print(choice)
choice_int = int(choice)
if choice_int == 1:
	open_apache_hadoop()
elif choice_int == 2:
	open_apache_spark()
elif choice_int == 3:
	open_jupyter_notebook()
elif choice_int == 4:
	open_sonar()
else:
	print("invalid input, please try again")