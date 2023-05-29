import heapq

# 空のヒープを作成
heap = []

# 要素をヒープに追加
heapq.heappush(heap, 4)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print("Heap:", heap)

# 最小の要素を取り出し
min_element = heapq.heappop(heap)
print("Minimum Element:", min_element)

print("Heap after pop:", heap)
