class Solution:
    """
    @param asteroids: a list of integers
    @return: return a list of integers
    """

    def asteroidCollision(self, asteroids):
        # write your code here

        if self.valid(asteroids):
            return asteroids

        arr = self.helper(asteroids)
        print(arr)
        return self.asteroidCollision(arr)

    def valid(self, asteroids):
        for i in range(1, len(asteroids)):
            if asteroids[i - 1] * asteroids[i] < 0 and asteroids[i] < 0:
                return False

        return True

    def helper(self, asteroids):
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            if asteroid < 0:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroid)
                elif abs(stack[-1]) > abs(asteroid):
                    continue
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    stack.append(asteroid)
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()

        return stack