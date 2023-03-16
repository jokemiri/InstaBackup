import instaloader

insta = instaloader.Instaloader()

account = 'jokemiri'

insta.download_profile(account, profile_pic_only=False)