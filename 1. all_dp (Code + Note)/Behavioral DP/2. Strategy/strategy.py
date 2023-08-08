from typing import List

# 2. Strategy interface
class SortingStrategy:
    def sort(self, data: List[int]) -> List[int]:
        pass

# Concrete strategies
class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        # Implementation of bubble sort
        # ...
        return sorted(data)

class QuickSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        # Implementation of quick sort
        # ...
        return sorted(data)

class MergeSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        # Implementation of merge sort
        # ...
        return sorted(data)

# Context class
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort(self, data: List[int]) -> List[int]:
        return self.strategy.sort(data)

# Usage
data = [5, 2, 8, 1, 9]

# Create the sorting strategies
bubble_sort = BubbleSortStrategy()
quick_sort = QuickSortStrategy()
merge_sort = MergeSortStrategy()

# Create the sorter with a default strategy
sorter = Sorter(bubble_sort)

# Sort the data using the current strategy
sorted_data = sorter.sort(data)
print("Sorted using bubble sort:", sorted_data)

# Change the sorting strategy to quick sort
sorter.set_strategy(quick_sort)

# Sort the data using the new strategy
sorted_data = sorter.sort(data)
print("Sorted using quick sort:", sorted_data)

# Change the sorting strategy to merge sort
sorter.set_strategy(merge_sort)

# Sort the data using the new strategy
sorted_data = sorter.sort(data)
print("Sorted using merge sort:", sorted_data)
