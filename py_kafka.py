from kafka import KafkaProducer
import json
import uuid
import time

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers="10.255.50.128:31255"
)
packageUUId = uuid.uuid4()  # 生成图片UUID

js = {
    "dataType": "securityCheckingAlarm",
    "recvTime": "2021-03-10T12:39:01.000+08:00",
    "sendTime": "2021-03-10T12:39:00.000 +08:00",
    "dateTime": "2021-03-10T12:39:00+08:00",
    "ipAddress": "10.19.134.11",
    "portNo": 80,
    "channelID": 1,
    "eventType": "securityCheckingResult",
    "eventDescription": "securityCheckingResult",
    "securityCheckingResult": [
        {
            "dangerousGoodsInfo": [
                {
                    "rect": {
                        "width": 0.112148,
                        "x": 0.526409,
                        "y": 0.459809,
                        "height": 0.110279
                    },
                    "dangerousGoodsType": "batteries",
                    "confidence": 0,
                    "manual_mark_flag": 0
                }
            ],
            "imageUrl": "http://10.255.60.131:30880/security/config/file/download?imagePath=/si-inspect/20210310/16/c783472b-8948-4cfe-9b0c-2bc07363e2db.jpg",
            "targetAttrs": {
                "imageServerCode": "0d8f4216-984a-433c-8f99-ba6a71440b45",
                "deviceIndexCode": "7b788b5c104b4448b1deddd942a0c6e5"
            },
            "dangerousGoodsNum": 6,
            "ruleID": 1,
            "deviceID": "128886889"
        }
    ],
    "packageUUId": f"{packageUUId}",
    "focus_judge": 1  # 集中判图数据结构
}

num = input("请输入需要发送的消息条数：")
# while True:
for i in range(int(num)):
# for i in range(1):
    time.sleep(1)
    data = js
    producer.send('SEND_IMAGE_DATA', data)
producer.close()
