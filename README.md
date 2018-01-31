# pylexo
Pylexo wraps lex lambda events and converts it into an object so you don't have to remember string keys. All you have to do is pass your event to LexInputEvent

# Installation
To use pylexo in AWS Lambda you will have to package pylexo in your lambda package. pylexo depends on jsonobject 0.7.1 (0.8 wouldn't work in AWS Lambda)

```
pip install pylexo -t /path/to/lambda/package
```
you can also put it in a sub folder
pip install pylexo -t /path/to/lambda/package/subfolder
but you will have to run this code in your AWS Lambda handler before importing pylexo
```python
import os
root = os.environ.get("LAMBDA_TASK_ROOT")
if root:
    packages = os.path.join(root, 'subfolder')
    logging.info("Inserting {} to path".format(packages))
    sys.path.insert(0, packages)
```

# Usage
This is how to enable auto-complete
```python
import pylexo
event =  {
    "messageVersion": "1.0",
    "invocationSource": "DialogCodeHook",
    "userId": "user_123",
    "sessionAttributes": {
        "RequestorCity": "Portland"
    },
    "bot": {
        "name": "OrderFlowers",
        "alias": None,
        "version": "$LATEST"
    },
    "outputDialogMode": "Text",
    "currentIntent": {
        "name": "OrderFlowers",
        "slots": {
            "PickupTime": None,
            "FlowerType": "Roses",
            "PickupDate": None
        },
        "confirmationStatus": "None"
    }
}

pylexo_event = pylexo.LexInputEvent(event)
print("messageVersion:   {}".format(pylexo_event.messageVersion))
print("invocationSource: {}".format(pylexo_event.invocationSource))
print("userId:           {}".format(pylexo_event.userId))
print("PickupTime:       {}".format(pylexo_event.currentIntent.slots['PickupTime']))
```

# Custom Slots
if you would like to have autocomplete on slots you will have to Override LexInputEvent. Please note that we rely on jsonobject for modeling JSON schema.
you can use pylexo command line interface to generate those stubs. after installing pylexo execute the following command to generate a file like order_flower_intent.py
```
pylexo --filepath order_flower_intent.py --slots PickupTime FlowerType PickupDate --sessions RequestorCity
```

once order_flower_intent.py is generated you can do the following

```python
import order_flower_intent

def lambda_handler(event, context):
    flower_event = order_flower_intent.LexInputEvent(event)
    print(event.messageVersion)
    print(event.invocationSource)
    print(event.userId)
    print(event.bot.name)
    print(event.bot.alias)
    print(event.bot.version)
    print(event.outputDialogMode)
    print(event.currentIntent.name)
    print(event.currentIntent.confirmationStatus)
    print(event.currentIntent.slots.PickupTime)
    print(event.currentIntent.slots.FlowerType)
    print(event.currentIntent.slots.PickupDate)

