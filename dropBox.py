from collections import List


"""
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, 
return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) 
respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, 
it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. 
For each group, it contains all the file paths of the files that have the same content. 
A file path is a string that has the following format:

"directory_path/file_name.txt"
"""

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
    
        
        for path_info in paths:
            
            info = path_info.split()
            directory = info[0]
            
            
            for file_info in info[1:]:
                
                left_paren = file_info.index('(')
                file_name = file_info[:left_paren]
                content = file_info[left_paren+1:-1]
                
               
                full_path = directory + '/' + file_name
                
               
                if content in content_map:
                    content_map[content].append(full_path)
                else:
                    content_map[content] = [full_path]
        
        
        return [group for group in content_map.values() if len(group) > 1]
            