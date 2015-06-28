formatter = "%r %r %r %r"
formatter2 = "boom boom boom boom"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter2, formatter, formatter2)
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
)