text= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer non luctus libero. Nam tristique eros nec leo rutrum, quis accumsan metus condimentum. Pellentesque sed lectus massa. Fusce ultrices libero id diam volutpat dignissim. In non libero a nisi dapibus congue. Aenean vestibulum tellus nulla. Sed venenatis erat nulla, vitae tempus ipsum dignissim ut. Pellentesque a posuere ex. Integer aliquam tellus at accumsan posuere. In hac habitasse platea dictumst. Maecenas eget cursus augue. Praesent sed mauris venenatis, fermentum nisi ut, porttitor turpis. Aenean mauris mauris, elementum eu nulla ac, accumsan congue nibh. Duis dolor ipsum, placerat ut laoreet id, tristique at dolor. Cras fermentum interdum pharetra. Quisque massa erat, consequat vel vulputate eu, venenatis sed augue. Curabitur lobortis magna quis mi tempus, non vehicula dolor vehicula. Aenean vulputate magna ut porta efficitur. Donec convallis mi eget condimentum rhoncus. Sed in facilisis mi. Sed vulputate nisl vitae nibh tempor laoreet. Suspendisse eu erat placerat, fringilla justo in, ultrices dolor. Maecenas tristique urna sit amet orci venenatis dignissim. In cursus augue nulla, luctus dictum lacus ultricies quis."
number = len(text)
Acount = 0
for i in text:
	if (i == 'a' or i == 'A'):
		Acount = Acount + 1	
print (text.title())
print ("A szöveg hossza:{:^10}".format (number) + "|")
print ('Az "a" betűk száma:{:<20}'.format (Acount) + "|")
