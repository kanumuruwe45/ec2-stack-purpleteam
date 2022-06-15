from faker import Faker
redisClient = redis.StrictRedis(host=os.getenv('redisip'),port=6379,db=0,decode_responses=True)
fake = Faker()
for _ in range(10):
  name = fake.name()
  ssn = str(fake.ssn())
  redisClient.set(name, ssn)]
app.logger.info("Generated dummy entries!")
