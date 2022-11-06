import platform

print(platform.platform())

# Task 4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat.replace("Fast", "Gigabit"))

# Task 4.2
mac = "AAAA:BBBB:CCCC"
print(mac.replace(":", "."))

# Task 4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result1 = config.split()
result = result1[-1].split(",")
print(result)

# Task 4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
set1 = set(vlans)
result = sorted(set1)
print(result)

# Task 4.5
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
result1 = command1.split()
result11 = result1[-1].split(",")
set1 = set(result11)
result2 = command2.split()
result21 = result2[-1].split(",")
set2 = set(result21)
print(sorted(set1.intersection(set2)))

# Task 4.6
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
list1 = ospf_route.replace(",", "").replace("via", "").split()
list2 = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]
for list1, list2 in zip(list1, list2):
    print('{:20}{:20}'.format(list2, list1))

# Task 4.7 Не нашел как это можно сделать в уроках. Скрипт из гугла
mac = "AAAA:BBBB:CCCC"
result = ' '.join(format(ord(c), 'b') for c in mac)
print(result)

# Task 4.8
ip = "192.168.3.1"
oct1, oct2, oct3, oct4 = ip.split('.')
print(f'{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}')