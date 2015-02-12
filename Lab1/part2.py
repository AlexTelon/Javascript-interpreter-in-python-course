import account

hest = account.make_account(100, 0.05)
print(hest['get_value'](1))
hest['withdraw'](10, 10)
hest['deposit'](10, 11)
print(hest['get_value'](12))
