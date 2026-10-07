from bin2dec import bin_to_dec

assert bin_to_dec("1") == 1
assert bin_to_dec("101") == 5
assert bin_to_dec("11111111") == 255
assert bin_to_dec("102") is None
print("All tests passed")