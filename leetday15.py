class Solution:
    def inorderTraversal(self, root):
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left


            root = st.pop()
            res.append(root.val)

            root = root.right


        return res        