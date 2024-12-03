from math import gcd

def phi(pq):
  return (p-1)*(q-1)

def f(e,p,q):
  return (1+gcd(e-1,p-1))*(1+gcd(e-1,q-1))
# Tóm tắt lại: đầu tiên ta sẽ tìm các số e sao cho f(e,p,q) là nhỏ nhất sau đó ta sẽ tính tổng các số này
def find_min_f_and_sum_e(p,q):
  phi_n=phi(p,q)
  valid_e=[]
  for e in range (phi_n):
    if gcd(e,phi_n)==1:
      valid_e.append(e) # tìm các số e thỏa mãn 1<e<phi(n) và gcd(e,phi(n))=1 
  min_f_value=float('inf')
  min_f_e_values=[]
  for e in valid_e:
    f_value=f(e,p,q)
    if f_value < min_f_value:
      min_f_value=f_value
      min_f_e_values=[e]  # vì giá trị e này cho ta f(e,p,q) bé hơn giá trị e trước đó cho nên ta sẽ đổi thành giá trị e này
    elif f_value==min_f_value:
      min_f_e_values.append(e)
  sum_of_e=sum(min_f_e_values)  
  return sum_of_e,min_f_value


p = 1009
q = 3643

print(f"Giá trị nhỏ nhất của f(e,p,q): {min_f_value}")
print(f"Tổng các số e thỏa mãn: {sum_of_e}")


