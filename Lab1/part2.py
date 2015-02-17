import account

#hest = account.make_account(100, 0.05)
#print(hest['get_value'](1))
#hest['withdraw'](10, 10)
#hest['deposit'](10, 11)
#print(hest['get_value'](12))


a1 = account.make_account(10, 0.1)
a2 = account.make_account(10, 0.01)
a1['deposit'](100, 10) # deposit 100 at t=10
print(a1['get_value'](10))
a2['withdraw'](10, 10)
print(a2['get_value'](10))
