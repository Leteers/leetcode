class Solution:
    def customSortString(self, order: str, s: str) -> str:
                    
        # order = 'cba'

        # s = 'aabc'
        dic_order = {i : symbol for i,symbol in enumerate(order)}
        string_symbols = {symbol : s.count(symbol) for symbol in s}

        new_string = ''

        for symbol in dic_order.keys():
            if dic_order[symbol] in string_symbols.keys():
                new_string += dic_order[symbol] * string_symbols.pop(dic_order[symbol])

        for symbol in string_symbols:
            new_string += symbol * string_symbols[symbol]
        return new_string
print(string_symbols)

print(dic_order)

print(new_string)