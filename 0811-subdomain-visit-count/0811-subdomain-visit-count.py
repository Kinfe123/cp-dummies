class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    
        DomainCountMap = {}
        res = []
        
        def addToDict(count, domain):
            if domain not in DomainCountMap:
                DomainCountMap[domain] = int(count)
            else:
                DomainCountMap[domain] += int(count)
        for cpDomain in cpdomains:
            count, domain = cpDomain.split(' ')
            while domain.find('.') >= 0:
                addToDict(count, domain)
                domain = domain[domain.index('.') + 1:]
            addToDict(count, domain)
        for key, value in DomainCountMap.items():
            res.append(str(value) + ' ' + key)
        
        return res