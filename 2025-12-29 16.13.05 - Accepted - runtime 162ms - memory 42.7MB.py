class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        import bisect
        
        potions.sort()
        n = len(potions)
        result = []
        
        for spell in spells:
            # We need spell * potion >= success
            # So potion >= success / spell
            # Find the minimum potion value that works
            min_potion = (success + spell - 1) // spell  # Ceiling division
            
            # Find the index of the first potion >= min_potion
            idx = bisect.bisect_left(potions, min_potion)
            
            # Count of valid potions
            result.append(n - idx)
        
        return result