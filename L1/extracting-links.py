page = '<ul class="nav-bar"> <li><a href="https://example.com/about">about</a></li> </ul>'

start_link = page.find('<a href=')
print start_link #position start link

start_quote = page.find('"', start_link)
print start_quote #position start first quote of link

end_quote = page.find('"', start_quote + 1)
print end_quote #position end quote

url = page[start_quote + 1: end_quote]
print url
