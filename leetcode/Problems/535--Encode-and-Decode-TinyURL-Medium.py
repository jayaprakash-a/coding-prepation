class Codec:
    def __init__(self):
        self.urlDict = {}
        self.index = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urlDict[self.index] = longUrl
        url = 'http://tinyurl.com/'+str(self.index)
        self.index += 1
        return url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # print(shortUrl, shortUrl.split('http://tinyurl.com/'))
        index = int(shortUrl.split('http://tinyurl.com/')[-1])
        
        return self.urlDict[index]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))