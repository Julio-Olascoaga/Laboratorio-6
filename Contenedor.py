import random

def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

height = [random.randint(1, 10) for _ in range(10)]
print("Height array:", height)
print("Max water area:", max_area(height))
