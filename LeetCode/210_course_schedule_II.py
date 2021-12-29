from collections import defaultdict
"""
Do topological sort
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = defaultdict(list,{ k:[] for k in range(numCourses)})
        for aft, bef in prerequisites:
            course_map[aft].append(bef)

        result = []
        
        while course_map:
            changed = False
            temp_dict = course_map.copy()
            for course, pres in temp_dict.items():
                if not pres:
                    course_map.pop(course)
                    result.append(course)
                    changed = True
                else:
                    for pre in pres:
                        if pre not in course_map:
                            pres.remove(pre)
                            changed = True
                    
            if not changed:
                return []
                
        return result
        