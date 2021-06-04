def lps(seq, i, j):
    if (i > j):
	    return 0

    if (i == j):
    	return 1
    if (seq[i] == seq[j] and i + 1 == j):
        return 2
    if (seq[i] == seq[j]):
	    return max(2+lps(seq,i+1,j-1),max(lps(seq, i, j - 1),
			lps(seq, i + 1, j))) 
 
        
    return max(lps(seq, i, j - 1),
			lps(seq, i + 1, j))

if __name__ == '__main__':
	seq = "GEEKSFORGEEFFKS"
	n = len(seq)
	print("The length of the LPS is",
				lps(seq, 0, n - 1))

