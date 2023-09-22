#LinearSeaarchProduct takes list of products and return a list of indices of targeted product

def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices


products = ["apple", "mongo", "orange", "apple", "pineapple", "apple"]
target = "apple"
result = linearSearchProduct(products, target)
print(result)