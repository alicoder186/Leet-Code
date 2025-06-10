class Solution:
    def isSameTree(self, p, q):
        is_p_null = p is None
        is_q_null = q is None

        if is_p_null and is_q_null:
            return True
        elif is_p_null or is_q_null:
            return False

        else:
            status = p.val == q.val
            status &= self.isSameTree(p.left, q.left)
            status &= self.isSameTree(p.right, q.right)
            return status

            

        