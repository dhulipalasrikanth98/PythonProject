import re
str1='''
he format of an email address is local-part@domain, where the local part may be up to 64 octets long and the domain may have a maximum of 255 octets.[4] The formal definitions are in RFC 5322 (sections 3.2.3 and 3.4.1) and RFC 5321—with a more readable form given in the informational RFC 3696[a] and the associated errata.

An email address also may have an associated display name for the recipient, which precedes the address specification, now surrounded by angled brackets, for example: John Smith 
john.smith@example.org.

Earlier forms of email addresses for other networks than the Internet included other notations, such as that required by X.400, and the UUCP bang path notation, in which the address was given in the form of a sequence of computers through which the message should be relayed. This was widely used for several years, but was superseded by the Internet standards promulgated by the Internet Engineering Task Force (IETF).

Local-part
The local-part of the email address may be unquoted or may be enclosed in quotation marks.

If unquoted, it may use any of these ASCII characters:

uppercase and lowercase Latin letters A to Z and a to z
digits 0 to 9
printable characters !#$%&'*+-/=?^_`{|}~
dot ., provided that it is not the first or last character and provided also that it does not appear consecutively (e.g., John.. is not allowed).[5]
Doe.smith@my_email.com
If quoted, it may contain Space, Horizontal Tab (HT), any ASCII graphic except Backslash and Quote and a quoted-pair consisting of a Backslash followed by HT, Space or any ASCII graphic; it may also be split between lines anywhere that HT or Space appears. In contrast to unquoted local-parts, the addresses ".John.Doe"@example.com, "John.Doe."@example.com and "John..Doe"@example.com are allowed.

'''

s=re.compile(r'[a-zA-Z.]+@[a-zA-Z._0-9]+\.(com|org)')
k=s.finditer(str1)
for i in k:
    with open('emails.txt','a') as f:
        f.write('\n')
        print(f"{i.group}\n data added to the file")
        f.write(i.group())