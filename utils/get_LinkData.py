### ---FUNCTIONS--- ###

def main(linkFile):
	allLinks = []

	links = open(linkFile, 'r')
	
	for line in links.readlines():
		if line[0] != '#' and line[0] != '<' and len(line) > 1:
			link = line.strip().split(',')
			linkName = link[0].strip()
			if len(linkName) > 8:
				linkName = linkName[:7] + '…'
			allLinks += [[linkName, link[1].strip(), link[2].strip()]]
		elif len(line) > 1 and line[0] == '<' and line[len(line)-2] == '>':
			allLinks += [[line.strip()]]
	links.close()
	#print(allLinks)
	return allLinks

### ---PROGRAM--- ###

if __name__ == "__main__":
	linkFile = 'links.txt'
	imageFolder = 'images/'
	main(linkFile)

