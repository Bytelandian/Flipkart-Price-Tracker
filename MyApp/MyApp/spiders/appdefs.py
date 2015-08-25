def getName(soup):
	try:
		temp=soup.find("div",class_="product-details line")
		temp=temp.find("h1",class_="title")
		name=temp.string
		return str(name)
	except:
		return None

def getPrice(soup):
	try:
		temp=soup.find("span","selling-price omniture-field")
		Rs = str(temp.string).replace(",", "")
		return Rs[4:]
	except:
		return None

def getRating(soup):
	try:
		temp=soup.find("div","ratingHistogram")
		if (temp==None):
			return ["None","None"]
		rating=temp.find("div","bigStar").string
		userRated=temp.find_all("p","subText")[1].string
		userRated=userRated.split()[2]
		return [str(rating),str(userRated).replace(",", "")]
	except:
		return ["None","None"]

def getDescription(soup):
	try :
		temp=soup.find("div","rpdSection")
		temp=temp.find_all("p","description")
		if (len(temp)==0):
			temp=soup.find("div","description-text")
			if (temp==None):
				return "No Description"
			temp=temp.find_all("p")
			temp=temp[0]
			des=temp.text
		else:
			temp=temp[0]
			des=temp.string
		return str(des.encode('ascii', 'ignore'))
	except :
		return "No Description"