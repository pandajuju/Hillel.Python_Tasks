
def partition(seq, left_idx, right_idx):
    pivot = left_idx

    for i in range(left_idx+1, right_idx+1):
        if seq[i] < seq[left_idx]:
            pivot += 1
            seq[i], seq[pivot] = seq[pivot], seq[i]
    seq[left_idx], seq[pivot] = seq[pivot], seq[left_idx]
    return pivot



def quicksort(seq, left_idx, right_idx):

    if left_idx >= right_idx:
        return





    pivot = partition(seq, left_idx, right_idx)
    quicksort(seq, left_idx, pivot-1)
    quicksort(seq, pivot+1, right_idx)
