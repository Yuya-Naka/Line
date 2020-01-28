from line import LINENotifyBot

bot=LINENotifyBot(access_token='XahqoKzRuuYxIslysEbGIMGqlzSEKFoxlF2Na3kXLBi')

bot.send(
    message='Hello雄哉',
    image='test.jpg',
    sticker_package_id=1,
    sticker_id=13,
    )
