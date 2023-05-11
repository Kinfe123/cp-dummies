class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        map_ = defaultdict(list)
        in_deg = defaultdict(int)

        for resp, ingr in zip(recipes , ingredients):
            in_deg[resp] = len(ingr)
            for each in ingr:
                map_[each].append(resp)
        
        
        q = deque(supplies)
        recipes = set(recipes)
        order = []
        #Since they are required without the pre requistes
        while q:
            s = q.popleft()
            #if the popped reaches to its parent we can safely say that it reaches
            if s in recipes:
                
                order.append(s)
            for nei in map_[s]:
                in_deg[nei]-=1
                if in_deg[nei] == 0:
                    #Now it is a valid a but need to check if it found in our recipe
                    q.append(nei)
        return order