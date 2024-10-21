#iterations and comprehensions
#use to process multiple items or repeat.

#Iteration
#An iterable is ay object that can return its members one at a time
servers = ['web1', 'web2', 'web3', 'web4', 'db1']
for server in servers:
    print(f"checking status of the servers: {server}")


#List-Comprehensions: List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
log_files = {'app.log', 'db.log', 'error.log', 'access.log', 'debug.log'}
important_logs = [log for log in log_files if log.startswith('e','a')]
print(f"checking important logs: {important_logs}")

#directionary comprehensions
#ex: creating a server status dictionary