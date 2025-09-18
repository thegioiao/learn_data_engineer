from confluent_kafka import Producer
import json, random, time
from faker import Faker

fake = Faker()

p = Producer({"bootstrap.servers":"localhost:9092"})
topic = "orders_events"

def gen_order_event(order_id):
    return {
        "order_id": order_id,
        "user_id": random.randint(1, 1_000_000),
        "order_date": fake.iso8601(),
        "total_amount": round(random.uniform(10, 2000),2),
        "status": random.choice(["created","paid","shipped","cancelled"])
    }

def ack(err, msg):
    if err:
        print(f"Failed :", err)

if __name__ == "__main__":
    order_id = 1
    while True:
        ev = gen_order_event(order_id)
        p.produce(topic, json.dump(ev).encode("utf-8"), callback=ack)
        p.poll(0)
        order_id += 1

        #Throughut control Tang dan khi test
        time.sleep(0.01)

