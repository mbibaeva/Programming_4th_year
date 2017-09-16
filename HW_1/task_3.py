
class UniqObject:
    instance = None
    
    def __init__(self):
        if self.instance is not None:
            raise ValueError ('UniqObject already exists')

    @classmethod
    def create_object(cls):
        if cls.instance is None:
            cls.instance = UniqObject()
        return cls.instance

Singleton = UniqObject()
print(Singleton.create_object())
Singleton1 = UniqObject()
print(Singleton1.create_object())
