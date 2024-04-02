import re

txt = "snaiyer.ualberta.ca"
x = re.search("((.*)(ualberta.ca))", txt)
print(x.groups())