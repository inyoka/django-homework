nums = [1,2,3]
sequences = [[1, 1, 2, 3, 1],[1, 1, 2, 4, 1],[1, 1, 2, 1, 2, 3]]

def contains_seq(nums, seq):
    for pos in range(len(seq)):
        if seq[pos:pos+len(nums)] == nums:
            return True
    return False

for seq in sequences:
    print(contains_seq(nums, seq))
