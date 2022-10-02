bicycles = ['trek', "cannon-dale", 'rower']
print(bicycles[0].title())
print(bicycles[-1])

combined = f"combine two from list into string {bicycles[0]}+{bicycles[-1]}"
print(combined)

bicycles[0] = 'Giant'
bicycles.append("Trek")
print(bicycles)

motorcycles = []
motorcycles.append("Romet")
motorcycles.append("aAbb")
motorcycles.append('simson')
motorcycles.append('MZ')
motorcycles.insert(-1, "suzuki")
motorcycles_last = motorcycles.pop()
motorcycles_by_values = motorcycles.remove('simson')  # remove only first occurrence

motorcycles.sort()  # fist A-Z then a-z
motorcycles.sort(reverse=True)  # z-a Z-A
moto_sorted = sorted(motorcycles)  # keep original as it is
print(moto_sorted)
