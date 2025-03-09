#from classes.progress.ProgressProcessor import ProgressProcessor

#pp = ProgressProcessor(50, 100, 78)
#print(pp)

from utils.format import wrap_by_words

print(wrap_by_words(12*'a'+" "+10*"a", 15))
