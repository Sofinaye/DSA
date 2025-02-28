# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution(object):
    def subdomainVisits(self, cpdomains):
        collection = {}
        result = []
        for i in cpdomains:
            temp_arr = i.split()
            temp_count = int(temp_arr[0])
            domain = temp_arr[1]
            subdomains = domain.split(".")

            for j in range(len(subdomains)):
                subdomain = ".".join(subdomains[j:])
                collection[subdomain] = collection.get(subdomain, 0) + temp_count
            

        for key, value in collection.items():
            result.append(str(value) + " " + key)

        return result

        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        