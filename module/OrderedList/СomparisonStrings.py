import OrderedList as OL


class СomparisonStrings(OL.OrderedList):
    def add_in_tail(self, item):
        item.value = item.value.strip()
        super().add_in_tail(item)
        print('ok')

    def comparison(self, val1, val2):
        if val1 > val2:
          return True
        else:
          return False

test = СomparisonStrings()
test.add_in_tail(OL.Node('hello'))
test.add_in_tail(OL.Node('  who are you'))
test.add_in_tail(OL.Node(' bay!  '))

print(test.head.value)
print(test.head.next.value)
print(test.head.next.next.value)

