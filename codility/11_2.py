def solution(A):
    A = sorted([A[i] for i in range(len(A))], reverse = True)
    
    answer = -1
    
    if len(A) >= 3:
        for p in range(len(A)-2):
            if A[p] + A[p+1] + A[p+2] < answer:
                break
            
            for q in range(p+1, len(A)-1):
                if A[p] + A[q] + A[q+1] < answer:
                    break
                
                for r in range(q+1, len(A)):
                    if A[p] >= A[q] + A[r] or A[p] + A[r] + A[q] < answer:
                        break
                    elif A[p] + A[r] > A[q]:
                        answer = A[p] + A[r] + A[q]
    
    
    return answer

#solution([i for i in range(100000)])