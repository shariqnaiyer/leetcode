def maxArea(height):
    start = 0
    end = len(height) - 1

    area1 = (end - start) * min(height[start], height[end])
    areal = [area1]
    while start < end:
        if height[start] <= height[end]:
            start += 1
            area = (end - start) * min(height[start], height[end])
            areal.append(area)

        if height[start] > height[end]:
            end -= 1
            area = (end - start) * min(height[start], height[end])
            areal.append(area)

    return max(areal)