class Solution:
    def simplifyPath(self, path: str) -> str:
        components=path.split("/")
        st=[]
        for comp in components:
            if comp=="" or comp==".":
                continue
            if comp=="..":
                if st:
                    st.pop()
            else:
                st.append(comp)
        return "/" + "/".join(st)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna