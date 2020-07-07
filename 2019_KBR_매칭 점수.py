import re

def solution(word, pages):
    answer = 0
    urls = {}
    word = word.lower()
    data = []
    for num, page in enumerate(pages):
        base_score = 0
        meta = page.split("<meta")
        body = page.split("<body>")[1].split("</body>")[0]
        for i in range(1, len(meta)):
            if 'content="' in meta[i]:
                url = meta[i].split('content="')[1].split('"')[0]
                urls[url] = num
                
        #print(body)
        tags = body.split('<a href="')
        links = []
        words = " " + tags[0]
        for i in range(1, len(tags)):
            tag = tags[i].split('">')
            links.append(tag[0])
            innertag = tag[1].split("</a>")
            words += " " + innertag[0] + " " + innertag[1] + " "
        words = words.lower()
        match = re.split('[^a-zA-Z]', words)
        #print(words)
        #print(match)
        #print(links)
        data.append([match.count(word),links, 0])
        
    #print(data)
    
    for i in range(len(data)):
        for link in data[i][1]:
            if link in urls:
                idx = urls[link]
                data[idx][2] += (data[i][0]/len(data[i][1]))
    
    for i in range(len(data)):
        if data[i][0] + data[i][2] > data[answer][0] + data[answer][2]:
            answer = i
    return answer