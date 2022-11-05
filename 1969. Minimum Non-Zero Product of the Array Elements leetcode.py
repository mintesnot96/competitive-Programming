# question
# 1969. Minimum Non-Zero Product of the Array Elements
# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/
class Solution(object):
    def minNonZeroProduct(self, p):
        MOD = 10**9+7
        max_num_mod = (pow(2, p, MOD)-1)%MOD
        pair_product_mod = (max_num_mod-1)%MOD  
        pair_cnt_mod_m_1 = (pow(2, p-1, MOD-1)-1) % (MOD-1)  
        return (max_num_mod*pow(pair_product_mod, pair_cnt_mod_m_1, MOD)) % MOD
