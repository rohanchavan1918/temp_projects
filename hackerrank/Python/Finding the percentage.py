from statistics import mean
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    q_score=student_marks[query_name]
    
    avg=mean(q_score)
    print(f"{avg:.2f}")
