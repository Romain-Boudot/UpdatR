exports.getIndexObj = function (array, obj) {
  for (const i in array) {
    if (array[i] === obj) {
      return i
    }
  }
  return -1
}
