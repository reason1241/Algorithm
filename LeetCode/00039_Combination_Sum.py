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