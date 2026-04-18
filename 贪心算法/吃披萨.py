class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        days = len(pizzas) // 4
        odd = (days + 1) // 2
        return sum(pizzas[:odd]) + sum(pizzas[odd + 1: odd + days // 2 * 2: 2])

