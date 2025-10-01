# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()
        result = []
        result.append(folder[0])
        
        for i in range(1, len(folder)):
            last_added_folder = result[-1]
            if not folder[i].startswith(last_added_folder + "/"):
                result.append(folder[i])
                
        return result
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        