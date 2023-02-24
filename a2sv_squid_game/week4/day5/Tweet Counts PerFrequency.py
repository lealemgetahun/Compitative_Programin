class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        f = 60
        if freq == 'minute':
            f = 60 
        elif freq == 'hour' :
            f = 3600
        else :
            f  = 86400 
        chunck = (endTime - startTime) // f + 1
        ans = [0]*chunck

        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                chunck = (time - startTime) // f
                ans[chunck] += 1

        return ans
        


        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)