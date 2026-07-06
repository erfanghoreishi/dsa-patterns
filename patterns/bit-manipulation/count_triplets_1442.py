#1442. Count Triplets That Can Form Two Arrays of Equal XOR
def countTriplets(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        xor = 0
        for k in range(i, n):
            xor ^= arr[k]            # xor = XOR(arr[i..k])
            if xor == 0:
                # For a triplet we split i..k at some j into a = XOR(i..j-1) and
                # b = XOR(j..k). Then a ^ b == XOR(i..k), so a == b  <=>  XOR(i..k) == 0.
                # The split point j cancels out — it never appears in that condition.
                # So this one xor==0 is satisfied by EVERY valid j (i < j <= k), and
                # there are (k - i) of them. Hence count += (k - i), not += 1.
                # See notes/theory/algorithmic_concepts.md (7. XOR properties).
                count += (k - i)
    return count
