def format_date(date):
    #strftime method converts it to a string
  return date.strftime('%m/%d/%y')

#tests filter for date
from datetime import datetime
print(format_date(datetime.now()))

#this removes extra info from a url leaving only domain name
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

#tests url filter
print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))

def format_plural(amount, word):
    #!= is does not equal
  if amount != 1:
    return word + 's'

  return word

#tests plural filter
print(format_plural(2, 'cat'))
print(format_plural(1, 'dog'))