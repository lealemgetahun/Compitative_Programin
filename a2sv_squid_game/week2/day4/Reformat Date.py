class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12" }
        day, mon, year = date.split()
        n = len(day) - 2
        day = day[:n]
        if len(day) == 1:
            day = "0"+day
        mon = month[mon]

        date = "-".join([year, mon, day])

        return date