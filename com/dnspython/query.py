import dns.resolver

A = dns.resolver.query('www.google.com', 'A')
for i in A.response.answer:
    for j in i.items:
        print j.address

MX = dns.resolver.query('163.com', 'MX')
for i in MX:
    print 'MX preference = ', i.preference, 'mail exchange = ', i.exchange

A2 = dns.resolver.query('163.com', 'A')
for i in A2.response.answer:
    for j in i.items:
        print j.address
