import tweepy
import time
import config

def main():
    # consumer　第一引数に(consumer　key)　第二引数に(consumer　secret) #
    auth = tweepy.OAuthHandler(config.MOKUPRO_CONSUMER_KEY, config.MOKUPRO_CONSUMER_SECRET)
    # ACCESS_TOKEN_KEY 第一引数に(Access token)　第二引数に(Access token secret) #
    auth.set_access_token(config.MOKUPRO_ACCESS_TOKEN, config.MOKUPRO_ACCESS_TOKEN_SECRET)

    # wait_on_rate_limit = レート制限が補充されるのを自動的に待つかどうか #
    # wait_on_rate_limit_notify = Tweepyがレート制限の補充を待っているときに通知を出力するかどうか #
    api = tweepy.API(auth, wait_on_rate_limit=True)



    # 取得したいキーワード #
    search_list = ['#もくプロ', '#プログラミング勉強中',
                '#ハッカソン', '#春から帝京大学', '#春から明星', '#春から帝京', '帝京大学' ]
    # ツイート数50件 #
    tweet_count = 50

    for search in search_list:
        print('Searching... {}' .format(search))
        # サーチ結果 #
        search_result = api.search_tweets(q=search, count=tweet_count)
        for tweet in search_result:
            tweet_id = tweet.id
            try:
                # いいねの処理 #
                api.create_favorite(id=tweet_id)
                print('Tweet_liked')
                time.sleep(2)
            except tweepy.errors.TweepyException as e:
                print(e)
            except StopIteration:
                break


if __name__ == '__main__':
    main()