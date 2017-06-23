import Bot


def handler(event, context):
    WeatherAlertsDC = Bot.Bot()
    WeatherAlertsDC.create_tweet()
    WeatherAlertsDC.post_tweet()
