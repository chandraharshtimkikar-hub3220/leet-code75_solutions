class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        for a in asteroids:
            while st and a < 0 < st[-1]:
                if st[-1] < -a:
                    st.pop()
                    continue 
                if st[-1] == -a:
                    st.pop()
                break
            else:
                st.append(a)
        return st
                 
        