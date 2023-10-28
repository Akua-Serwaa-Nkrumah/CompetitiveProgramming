class Solution:
    def combine(self, n: int, k: int) -> [int]:
        def is_valid_state(state):
            return len(state) == k

        def get_candidates(state):

            if len(state) == 0:
                res = set(range(1,n+1))
            else:
                res = set(range(max(list(state)),n+1))

            return res.difference(state)

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

            return

        def solve():
            solutions = []
            state = set()
            search(state,solutions)
            return solutions 

        return solve()