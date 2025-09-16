import redis

r = redis.Redis("localhost",6379,db=0,decode_responses=True)

class User():
    def __init__(self,username,age):
        self.username = username
        self.age = age
        self._id = r.incr("id")
        print(self._id)
        self.name = f"user:{self._id}"
        self.addToRedis()
    
    def addToRedis(self):
        user_ = {
            "username":self.username,
            "age":self.age,
            "_id":self._id
        }
        try:
            r.hset(self.name,mapping=user_)
            return True
        except:
            return False
    def getUser(self):
        return r.hgetall(self.name)
    
    @staticmethod
    def getAllUsers():
        keys = r.keys("user:*")
        users = []
        for key in keys:
            data = r.hgetall(key)
            users.append(data)
            print(data)
        return users
# user1 = User("Zangar",17)
# user2 = User("Daniar",18) 
# print(user1.getUser())
# print(user2.getUser())
# r.delete("user:0")
# print(User.getAllUsers())
print(r.keys("*"))