from bs4 import BeautifulSoup

f = open("instafollowers.txt", "r", encoding = 'UTF-8')
instafollowers= f.read()
Soup=BeautifulSoup(instafollowers, features='html.parser')
classtag = "x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"
mydivs = Soup.find_all("div", class_=classtag)
followerlist = []
for usernames in mydivs:
    followerlist.append(str(usernames).split('<div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1">')[1].split("</div>")[0])

ff = open("instafollowing.txt", "r", encoding = 'UTF-8')
instafollowing= ff.read()
Soup=BeautifulSoup(instafollowing, features='html.parser')
mydivss = Soup.find_all("div", class_=classtag)
followinglist = []
for usernames in mydivss:
    if "Verified" not in (str(usernames).split('<div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1">')[1].split("</div>")[0]):
            followinglist.append((str(usernames).split('<div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1">')[1].split("</div>")[0]))
        
    else:

         followinglist.append(str(str(usernames).split('<div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1">')[1].split("</div>")[0]).split('<div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh xsgj6o6 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><span class="_act0 _a9_u _9ys8" title="Verified">Verified</span>')[0])
followsmeback =[]
for i in range(len(followinglist)):
     for z in range(len(followerlist)):
          if str(followinglist[i]) == str(followerlist[z]):
               followsmeback.append(followerlist[z])




#print(followsmeback)
print('You have '+ str(len(followerlist))+ ' followers')
print('You are following '+str(len(followinglist)) + ' people')
print(str(len(followsmeback)) + ' people follow you back :)')
print(set(followinglist).difference(followsmeback))    
print(str(len(set(followinglist).difference(followsmeback)))+ " people don't follow you back :(")    
'''
print(followinglist)

print(followerlist)
'''
