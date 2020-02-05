# crypto_currencies_price

Merge charts of all crypto currencies(*/JPY) in Coincheck to one image and post it to slack.

## Usage

create `credentials.py` like:

```
SLACK_URL = {
   'my_channel': 'https://hooks.slack.com/services/the_webhook/url_of/my_channel',
}
SLACK_ACCESS_TOKEN = 'xoxp-1234567890-12345678-1234567890986432-8493a5d342133d2da0560e56369c3420f'
SLACK_CHANNEL_ID = {
   'my_channel': 'AACC323BB',
}

```

Then in terminal, run it:

```
$ python3 main.py my_channel
```

## Screenshot

![](https://raw.githubusercontent.com/wiki/hrdrq/crypto_currencies_price/img/20200131162522-times_son-1.png)
