# noveo_exercise

#### Exercise
 
We value working on real solutions to real problems, and as such we think the best way to understand your capabilities is to give you the opportunity to solve a problem similar to the ones we solve on a daily basis.

We ask you to write a simple Python/Flask application:
It listens for requests, and on receiving a notification the application should re-dispatch it to multiple targets (e.g. log, email, HTTP, SMS, Slack, etc.).

Write few lines about how to improve your design;
If you have access to a linux docker environment, our team would love to docker build & run it.
 
#### Requirements:
Have a generic interface for target backends;

Two target backends;

Have relevant tests.

The assignment is supposed to be vague so you can choose to "show off" what matters to you.

One could spend a lot of time with it... But rest assured that we value your time : For some part of your project you can resort to simply stating your intentions, what you would have implemented if you had more time, special considerations, etc.

You should spend at least a few hours on this so the end result is meaningful enough to help us understand how you work.

Once completed, share it with uPRos by email or through a private GitHub repository with a full history available.

If you have access to a linux docker environment, our team would love to docker build & run it.


#### Propose of improvments
Need to write error handling of controller's notify_all function, now there is nothing handles. If we get exception at notify_all must have a detailed error description, that must add to endpoint response

#### Up for run
```bash
$ cd noveo-exercise
(noveo-exercise)$ pip install -U pip pipenv
(noveo-exercise)$ pipenv install --dev
```

docker
```bash
$ cd noveo-exercise
(noveo-exercise)$ docker up
```

#### Example request
```bash
curl --location --request POST 'http://127.0.0.1:5000/notify' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sender": "NOVEO Test",
    "messages": [
        {
            "text": "Notification text #1",
            "recipients": [
                "LOG", "HTTP"
            ]
        },
        {
            "text": "Notification text #2",
            "recipients": [
                "LOG", "SMS", "SLACK"
            ]
        }
    ]
}'
```