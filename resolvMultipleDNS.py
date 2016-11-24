import dns.resolver,sys,socket

myResolver = dns.resolver.Resolver()
myAnswers = myResolver.query(sys.argv[1], sys.argv[2])
for rdata in myAnswers:
    host = socket.gethostbyaddr(str(rdata))
    print str(host[0])+" & ip : "+str(host[2])
