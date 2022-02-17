# Time Complexity O(n) 84 ms
# Space Complexity O(n) 14 MB
# dfs
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def _combinationSum(candidates: List[int], target: int) -> List[List[int]]:
            result = []

            for idx, candidate in enumerate(candidates):
                next_target = target - candidate

                if next_target < 0:
                    break
                elif next_target == 0:
                    result.append([candidate])
                else:
                    received = self.combinationSum(candidates[idx:], target - candidate)
                    if received:
                        result.extend([[candidate, *r] for r in received])
            return result
        candidates.sort()
        return _combinationSum(candidates, target)
    
# Time Complexity O(n) 108 ms
# Space Complexity O(n) 14 MB
# dfs
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def _combinationSum(candidates: List[int], target: int, path: List[int], result: List[int]):
            if target < 0:
                return
            elif target == 0:
                result.append(path)
                return
            for idx in range(len(candidates)): 
                _combinationSum(candidates[idx:], target - candidates[idx], path + [candidates[idx]], result)
        result = []
        _combinationSum(candidates, target, [], result)
        return result