def is_overlapping(interval1, interval2):
 
    if interval1[1] <= interval2[0] or interval2[1] <= interval1[0]:
        return False
    else:
        return True


h1 = int(input("Година початку інтервалу першого свідка (h1): "))
m1 = int(input("Хвилина початку інтервалу першого свідка (m1): "))
h2 = int(input("Година кінця інтервалу першого свідка (h2): "))
m2 = int(input("Хвилина кінця інтервалу першого свідка (m2): "))

h3 = int(input("Година початку інтервалу другого свідка (h3): "))
m3 = int(input("Хвилина початку інтервалу другого свідка (m3): "))
h4 = int(input("Година кінця інтервалу другого свідка (h4): "))
m4 = int(input("Хвилина кінця інтервалу другого свідка (m4): "))

st1 = h1 * 60 + m1
end1 = h2 * 60 + m2
st2 = h3 * 60 + m3
end2 = h4 * 60 + m4

interval1 = (st1, end1)
interval2 = (st2, end2)

if is_overlapping(interval1, interval2):
    print("Обидва свідки можуть говорити правду.")
else:
    print("Свідки не можуть говорити правду одночасно.")
