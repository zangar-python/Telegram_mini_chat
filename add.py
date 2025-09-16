from tasks import add

result = add.delay(4,6)
print("Task is confurmed")
print("Id task:",result.id)
print("result",result.get())